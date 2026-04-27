


from extract_data import *
import time
from store_data_database import *
# from car_detail import *
from product_detial import *


def main():
    # # -------first operation-----------
    # # create table for kia_location_url
    # create_buy_plastic_url_table()
    # print("table and db create")

    # # extract_store_urls data  
    # plastic_category()


    # # # -------second operation-----------
    # # fetch_kia_location_url_table data 
    # buy_plastic_url_list = fetch_buy_plastic_url_table()

    
    # # # Create table 
    # create_product_detail_table()

    # # # # # call process_kia_data
    # # fetch_product_detail(list_data= buy_plastic_url_list)

    # # thread with
    # run_threaded_fetch(buy_plastic_url_list)



    # # # -------third operation-----------

    product_detail_list = fetch_product_detail_table()

    # create table
    create_product_detail_using_file_table()

    read_file_usin_sku(list_data = product_detail_list)











if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("time different  : ", end - start)