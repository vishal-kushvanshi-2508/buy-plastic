

from typing import List, Tuple
import mysql.connector # Must include .connector


table_name = "product_url"
DB_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : "actowiz",
    "port" : "3306",
    "database" : "buy_plastic_request_db"
}

def get_connection():
    try:
        ## here ** is unpacking DB_CONFIG dictionary.
        connection = mysql.connector.connect(**DB_CONFIG)
        ## it is protect to autocommit
        connection.autocommit = False
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

def create_db():
    connection = get_connection()
    # connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS buy_plastic_request_db;")
    connection.commit()
    connection.close()
# create_db()

def create_buy_plastic_url_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query =  f"""
                CREATE TABLE IF NOT EXISTS {table_name}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                category_entity_id INT,
                category_name VARCHAR(200),
                product_entity_id INT,
                sku VARCHAR(200),
                product_name VARCHAR(200),
                product_url TEXT,
                status VARCHAR(200)
        ); """
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Table creation failed")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

batch_size_length = 100
def data_commit_batches_wise(connection, cursor, sql_query : str, sql_query_value: List[Tuple], batch_size: int = batch_size_length ):
    ## this is save data in database batches wise.
    batch_count = 0
    for index in range(0, len(sql_query_value), batch_size):
        batch = sql_query_value[index: index + batch_size]
        cursor.executemany(sql_query, batch)
        batch_count += 1
        connection.commit()
    return batch_count


def insert_buy_plastic_url_table(list_data : list):
    connection = get_connection()
    cursor = connection.cursor()
    if not list_data:
        return
    dict_data = list_data[0]
    columns = ", ".join(list(dict_data.keys()))
    values = "".join([len(dict_data.keys()) * '%s,']).strip(',')
    parent_sql = f"""INSERT INTO {table_name} ({columns}) VALUES ({values})"""
    try:
        product_values = []
        for dict_data in list_data:
            product_values.append( (
                dict_data.get("category_entity_id"),
                dict_data.get("category_name"),
                dict_data.get("product_entity_id"),
                dict_data.get("sku"),
                dict_data.get("product_name"),
                dict_data.get("product_url"),
                dict_data.get("status")
            ))

        try:
            batch_count = data_commit_batches_wise(connection, cursor, parent_sql, product_values)
            print(f"Parent batches executed count={batch_count}")
        except Exception as e:
            print(f"batch can not. Error : {e} ")

        cursor.close()
        connection.close()

    except Exception as e:
        ## this exception execute when error occur in try block and rollback until last save on database .
        connection.rollback()
        # print(f"Transaction failed, rolled back. Error: {e}")
        print("Transaction failed. Rolling back")
    except:
        print("except error raise ")
    finally:
        connection.close()

def fetch_buy_plastic_url_table():
    connection = get_connection()
    cursor = connection.cursor()
    # query = f"SELECT * FROM product_url where id = 2 or id= 3 ;"
    query = f"""SELECT *
                FROM {table_name} p
                WHERE status = 'pending'
                AND id in (select min(id) as id  from {table_name} where status = 'pending' group by product_name 
                );"""
 
 
    cursor.execute(query)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        data = {
            "id": row[0],
            "category_entity_id": row[1],
            "category_name": row[2],
            "product_entity_id": row[3],
            "sku": row[4],
            "product_name": row[5],
            "product_url": row[6],
            "status": row[7]
        }
        result.append(data)

    cursor.close()
    connection.close()
    return result


def update_buy_plastic_url_status(product_name, status):
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = f"UPDATE {table_name} SET status = %s  WHERE product_name = %s ;"
    values = (status, product_name)
    cursor.execute(sql_query, values)
    connection.commit()
    cursor.close()
    connection.close()




# ------------------second table-------------
car_detail_table_name = "product_detail"

def create_product_detail_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query =  f"""
                CREATE TABLE IF NOT EXISTS {car_detail_table_name}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_url_id INT,
                category_name VARCHAR(255),
                product_entity_id INT,
                product_name VARCHAR(255),
                product_url TEXT,
                variants JSON,
                sku VARCHAR(255),
                price VARCHAR(255),
                bulk_pricing JSON
        ); """
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Table creation failed")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()




def insert_product_detail_table(list_data : list):
    print("-----insert_movie_details_table--------")
    connection = get_connection()
    cursor = connection.cursor()
    if not list_data:
        return
    dict_data = list_data[0]
    columns = ", ".join(list(dict_data.keys()))
    values = "".join([len(dict_data.keys()) * '%s,']).strip(',')
    parent_sql = f"""INSERT INTO {car_detail_table_name} ({columns}) VALUES ({values})"""
    try:
        product_values = []
        for dict_data in list_data:
            product_values.append( (
                dict_data.get("product_url_id"),
                dict_data.get("category_name"),
                dict_data.get("product_entity_id"),
                dict_data.get("product_name"),
                dict_data.get("product_url"),
                dict_data.get("variants"),
                dict_data.get("sku"),
                dict_data.get("price"),
                dict_data.get("bulk_pricing")
            ))


        try:
            batch_count = data_commit_batches_wise(connection, cursor, parent_sql, product_values)
            print(f"Parent batches executed count={batch_count}")
        except Exception as e:
            print(f"batch can not. Error : {e} ")

        cursor.close()
        connection.close()

    except Exception as e:
        ## this exception execute when error occur in try block and rollback until last save on database .
        connection.rollback()
        # print(f"Transaction failed, rolled back. Error: {e}")
        print("Transaction failed. Rolling back")
    except:
        print("except error raise ")
    finally:
        connection.close()





def fetch_product_detail_table():
    connection = get_connection()
    cursor = connection.cursor()
    # query = f"SELECT * FROM product_url where id = 2 or id= 3 ;"
    query = f"""SELECT 
        p.id AS parent_id,
        p.category_name AS parent_category_name,
        p.product_entity_id AS parent_product_entity_id,
        p.sku AS parent_sku,
        c.sku AS child_sku,
        c.id AS child_id,
        c.product_name AS child_product_name,
        c.product_url AS child_product_url
        FROM product_url p
        JOIN product_detail c 
        ON c.product_url_id = p.id ;"""
 
 
    cursor.execute(query)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        data = {
            "parent_id": row[0],
            "parent_category_name": row[1],
            "parent_product_entity_id": row[2],
            "parent_sku": row[3],
            "child_sku": row[4],
            "child_id": row[5],
            "child_product_name": row[6],
            "child_product_url": row[7]
        }
        result.append(data)

    cursor.close()
    connection.close()
    return result



#------third table------------ 

product_using_file_table_name = "product_detail_using_file"

def create_product_detail_using_file_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query =  f"""
                CREATE TABLE IF NOT EXISTS {product_using_file_table_name}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_url_id INT,
                category_name VARCHAR(255),
                product_entity_id INT,
                parent_sku VARCHAR(255),
                product_name VARCHAR(255),
                product_url TEXT,
                variants JSON,
                child_sku VARCHAR(255),
                price VARCHAR(255),
                bulk_pricing JSON
        ); """
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Table creation failed")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def insert_product_detail_using_file_table(list_data : list):
    print("-----insert_movie_details_table--------")
    connection = get_connection()
    cursor = connection.cursor()
    if not list_data:
        return
    dict_data = list_data[0]
    columns = ", ".join(list(dict_data.keys()))
    values = "".join([len(dict_data.keys()) * '%s,']).strip(',')
    parent_sql = f"""INSERT INTO {product_using_file_table_name} ({columns}) VALUES ({values})"""
    try:
        product_values = []
        for dict_data in list_data:
            product_values.append( (
                dict_data.get("product_url_id"),
                dict_data.get("category_name"),
                dict_data.get("product_entity_id"),
                dict_data.get("parent_sku"),
                dict_data.get("product_name"),
                dict_data.get("product_url"),
                dict_data.get("variants"),
                dict_data.get("child_sku"),
                dict_data.get("price"),
                dict_data.get("bulk_pricing")
            ))


        try:
            batch_count = data_commit_batches_wise(connection, cursor, parent_sql, product_values)
            print(f"Parent batches executed count={batch_count}")
        except Exception as e:
            print(f"batch can not. Error : {e} ")

        cursor.close()
        connection.close()

    except Exception as e:
        ## this exception execute when error occur in try block and rollback until last save on database .
        connection.rollback()
        # print(f"Transaction failed, rolled back. Error: {e}")
        print("Transaction failed. Rolling back")
    except:
        print("except error raise ")
    finally:
        connection.close()
