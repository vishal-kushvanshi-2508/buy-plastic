

import requests
import json
import zipfile
import os
from store_data_database import *

cookies = {
    'SF-CSRF-TOKEN': 'b9ce9202-ad66-4342-b94a-ef08bd35255f',
    'fornax_anonymousId': 'ee356938-fb54-45c5-b62b-53b88f4e55bf',
    'athena_short_visit_id': 'c209068e-733d-417a-9bd4-429b09eebdd2:1777246043',
    'XSRF-TOKEN': 'c83fc652e55e0b72ca683f4ff3baef2376d2d936b2725bb5861c20f88a38d7d5',
    'SHOP_SESSION_TOKEN': 'd49a5274-9840-4371-ad89-9e0db846cfd1',
    '__cf_bm': '6OJf.Wm1Y0u_JdDZSHI.uWNmeaHjl0Yaaj0lYZRYVpM-1777246046.8367274-1.0.1.1-uFGIcn8F5gHE3udeAD.yoy9Yo8K_awGSpCKRqOh7h7Ixue7X_S5NNRxuNPoAHwehwRR5GDaI5rr_8PLhGrkrrY_l7u4m4Y.uV7XQKPg6cK0dyGqc8IWx5B_pFryR1KXV',
    '__kla_id': 'eyJjaWQiOiJZbUpsTWpZNVlXTXRZV0poWkMwMFlqa3hMV0ppT0dNdFl6TTJaVFE1TkRVNU16ZzMifQ==',
    'STORE_VISITOR': '1',
    '_fbp': 'fb.1.1777246045848.633336333532399196',
    '_ga': 'GA1.1.522542883.1777246047',
    '_gcl_au': '1.1.207847009.1777246047',
    'lastVisitedCategory': '50',
    '_ga_YBZ6F6339N': 'GS2.1.s1777246046$o1$g1$t1777246391$j51$l0$h0',
    '_ga_50BLGJTDSB': 'GS2.1.s1777246046$o1$g1$t1777246395$j22$l0$h943036257',
    'Shopper-Pref': '3059DD0834E160640A26BEC9F6DF7458934C20E0-1777851232149-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}



def price_detail(product_url, price_data, product_entity_id, folder_path, product_detail_data, variant_sku):

    cookies = {
        'SF-CSRF-TOKEN': 'b9ce9202-ad66-4342-b94a-ef08bd35255f',
        'fornax_anonymousId': 'ee356938-fb54-45c5-b62b-53b88f4e55bf',
        'athena_short_visit_id': 'c209068e-733d-417a-9bd4-429b09eebdd2:1777246043',
        'XSRF-TOKEN': 'c83fc652e55e0b72ca683f4ff3baef2376d2d936b2725bb5861c20f88a38d7d5',
        'SHOP_SESSION_TOKEN': 'd49a5274-9840-4371-ad89-9e0db846cfd1',
        '__cf_bm': '6OJf.Wm1Y0u_JdDZSHI.uWNmeaHjl0Yaaj0lYZRYVpM-1777246046.8367274-1.0.1.1-uFGIcn8F5gHE3udeAD.yoy9Yo8K_awGSpCKRqOh7h7Ixue7X_S5NNRxuNPoAHwehwRR5GDaI5rr_8PLhGrkrrY_l7u4m4Y.uV7XQKPg6cK0dyGqc8IWx5B_pFryR1KXV',
        '__kla_id': 'eyJjaWQiOiJZbUpsTWpZNVlXTXRZV0poWkMwMFlqa3hMV0ppT0dNdFl6TTJaVFE1TkRVNU16ZzMifQ==',
        'STORE_VISITOR': '1',
        '_fbp': 'fb.1.1777246045848.633336333532399196',
        '_ga': 'GA1.1.522542883.1777246047',
        '_gcl_au': '1.1.207847009.1777246047',
        'lastVisitedCategory': '50',
        '_ga_YBZ6F6339N': 'GS2.1.s1777246046$o1$g1$t1777246391$j51$l0$h0',
        '_ga_50BLGJTDSB': 'GS2.1.s1777246046$o1$g1$t1777246395$j22$l0$h943036257',
        'Shopper-Pref': '76A269C7967A3ED67C207C5E5615291D6A34AE38-1777851234378-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://buyplastic.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': f"{product_url}",
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-sf-csrf-token': 'b9ce9202-ad66-4342-b94a-ef08bd35255f',
        'x-xsrf-token': 'c83fc652e55e0b72ca683f4ff3baef2376d2d936b2725bb5861c20f88a38d7d5',
        # 'cookie': 'SF-CSRF-TOKEN=b9ce9202-ad66-4342-b94a-ef08bd35255f; fornax_anonymousId=ee356938-fb54-45c5-b62b-53b88f4e55bf; athena_short_visit_id=c209068e-733d-417a-9bd4-429b09eebdd2:1777246043; XSRF-TOKEN=c83fc652e55e0b72ca683f4ff3baef2376d2d936b2725bb5861c20f88a38d7d5; SHOP_SESSION_TOKEN=d49a5274-9840-4371-ad89-9e0db846cfd1; __cf_bm=6OJf.Wm1Y0u_JdDZSHI.uWNmeaHjl0Yaaj0lYZRYVpM-1777246046.8367274-1.0.1.1-uFGIcn8F5gHE3udeAD.yoy9Yo8K_awGSpCKRqOh7h7Ixue7X_S5NNRxuNPoAHwehwRR5GDaI5rr_8PLhGrkrrY_l7u4m4Y.uV7XQKPg6cK0dyGqc8IWx5B_pFryR1KXV; __kla_id=eyJjaWQiOiJZbUpsTWpZNVlXTXRZV0poWkMwMFlqa3hMV0ppT0dNdFl6TTJaVFE1TkRVNU16ZzMifQ==; STORE_VISITOR=1; _fbp=fb.1.1777246045848.633336333532399196; _ga=GA1.1.522542883.1777246047; _gcl_au=1.1.207847009.1777246047; lastVisitedCategory=50; _ga_YBZ6F6339N=GS2.1.s1777246046$o1$g1$t1777246391$j51$l0$h0; _ga_50BLGJTDSB=GS2.1.s1777246046$o1$g1$t1777246395$j22$l0$h943036257; Shopper-Pref=76A269C7967A3ED67C207C5E5615291D6A34AE38-1777851234378-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
    }

    url = f"https://buyplastic.com/remote/v1/product-attributes/{product_entity_id}"

    response = requests.post(url, cookies=cookies, headers=headers, data=price_data)

    data = response.json()
    
    # Save into ZIP
    with zipfile.ZipFile(f"{folder_path}\\{variant_sku}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr("products.json", json.dumps(data, indent=4))

    base_price = data.get("data").get("price").get("without_tax").get("value")  # you must provide this

    result = []

    for item in data.get("data").get("bulk_discount_rates"):
        min_qty = item["min"]
        max_qty = item["max"]
        discount = item["discount"]["value"]

        # calculate discounted price
        final_price = base_price * (1 - discount / 100)

        # format range text
        if max_qty == 0:
            qty_text = f"Buy {min_qty} or above"
        else:
            qty_text = f"Buy {min_qty} - {max_qty}"

        text = f'{qty_text} for ${final_price:.2f} each ({discount}% off)'
        result.append(text)

    product_detail_data["sku"] =  data.get("data").get("sku")
    product_detail_data["price"] = data.get("data").get("price").get("without_tax").get("formatted")
    product_detail_data["bulk_pricing"] = json.dumps(result)

    return product_detail_data


def fetch_product_detail(list_data : list):

    product_list_data = []

    for dict_data in list_data:

        product_table_id = dict_data.get("id") 
        sku = dict_data.get("sku") 
        category_name = dict_data.get("category_name") 
        product_entity_id = dict_data.get("product_entity_id") 

        product_name = dict_data.get("product_name") 
        product_url = dict_data.get("product_url") 
        print("id : ", product_table_id, product_url)

        folder = r"D:\vishal_kushvanshi\buy_plastic_request\variants_pages"
        folder_path = os.path.join(folder, str(sku))
        os.makedirs(folder_path, exist_ok=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJjaWQiOlsxXSwiY29ycyI6WyJodHRwczovL2J1eXBsYXN0aWMuY29tIl0sImVhdCI6MTc3NzM4MjcyOCwiaWF0IjoxNzc3MjA5OTI4LCJpc3MiOiJCQyIsInNpZCI6MTAwMTA1ODIzOSwic3ViIjoiQkMiLCJzdWJfdHlwZSI6MCwidG9rZW5fdHlwZSI6MX0.3X5ds2Fes7RGKxflm-EhYqohbIal4xxB6BI_gJ7Cb0YkNfqr_BIXavI5iw80cA3ScntGwCaudTU4z5aNMiHzeQ',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://buyplastic.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f"{product_url}",
            'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            'x-sf-csrf-token': 'b9ce9202-ad66-4342-b94a-ef08bd35255f',
            'x-xsrf-token': 'c83fc652e55e0b72ca683f4ff3baef2376d2d936b2725bb5861c20f88a38d7d5',
            # 'cookie': 'SF-CSRF-TOKEN=b9ce9202-ad66-4342-b94a-ef08bd35255f; fornax_anonymousId=ee356938-fb54-45c5-b62b-53b88f4e55bf; athena_short_visit_id=c209068e-733d-417a-9bd4-429b09eebdd2:1777246043; XSRF-TOKEN=c83fc652e55e0b72ca683f4ff3baef2376d2d936b2725bb5861c20f88a38d7d5; SHOP_SESSION_TOKEN=d49a5274-9840-4371-ad89-9e0db846cfd1; __cf_bm=6OJf.Wm1Y0u_JdDZSHI.uWNmeaHjl0Yaaj0lYZRYVpM-1777246046.8367274-1.0.1.1-uFGIcn8F5gHE3udeAD.yoy9Yo8K_awGSpCKRqOh7h7Ixue7X_S5NNRxuNPoAHwehwRR5GDaI5rr_8PLhGrkrrY_l7u4m4Y.uV7XQKPg6cK0dyGqc8IWx5B_pFryR1KXV; __kla_id=eyJjaWQiOiJZbUpsTWpZNVlXTXRZV0poWkMwMFlqa3hMV0ppT0dNdFl6TTJaVFE1TkRVNU16ZzMifQ==; STORE_VISITOR=1; _fbp=fb.1.1777246045848.633336333532399196; _ga=GA1.1.522542883.1777246047; _gcl_au=1.1.207847009.1777246047; lastVisitedCategory=50; _ga_YBZ6F6339N=GS2.1.s1777246046$o1$g1$t1777246391$j51$l0$h0; _ga_50BLGJTDSB=GS2.1.s1777246046$o1$g1$t1777246395$j22$l0$h943036257; Shopper-Pref=3059DD0834E160640A26BEC9F6DF7458934C20E0-1777851232149-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
        }

        json_data = {
            "query": """
            query GetProduct($entityId: Int!) {
            site {
                product(entityId: $entityId) {
                entityId
                name
                sku
                
                availabilityV2 {
                    status
                }

                inventory {
                    isInStock
                    aggregated {
                    availableToSell
                    }
                    hasVariantInventory
                }

                variants(first: 50) {
                    edges {
                    node {
                        entityId
                        sku
                        isPurchasable

                        options {
                        edges {
                            node {
                            entityId
                            displayName
                            values {
                                edges {
                                node {
                                    entityId
                                    label
                                }
                                }
                            }
                            }
                        }
                        }

                        inventory {
                        isInStock
                        aggregated {
                            availableToSell
                        }
                        }

                        metafields(
                        keys: ["backorder_configs"],
                        namespace: "backorder_v2",
                        first: 50
                        ) {
                        edges {
                            node {
                            id
                            entityId
                            key
                            value
                            }
                        }
                        }

                    }
                    }
                }

                productOptions {
                    edges {
                    node {
                        entityId
                        isRequired
                        ... on MultipleChoiceOption {
                        values {
                            edges {
                            node {
                                entityId
                                isDefault
                            }
                            }
                        }
                        }
                    }
                    }
                }

                metafields(
                    keys: ["backorder_configs"],
                    namespace: "backorder_v2",
                    first: 50
                ) {
                    edges {
                    node {
                        id
                        entityId
                        key
                        value
                    }
                    }
                }

                }
            }
            }
            """,
            "variables": {
                "entityId": int(product_entity_id)
            }
        }

        response = requests.post('https://buyplastic.com/graphql', cookies=cookies, headers=headers, json=json_data)

        data = response.json()
        
        
        # Save into ZIP
        with zipfile.ZipFile(f"{folder_path}\\variants_data.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr("products.json", json.dumps(data, indent=4))
        
        edge_list = data.get("data", {}).get("site", {}).get("product", {}).get("variants", {}).get("edges", [])

        for edge_dict in edge_list:
            variant_sku = edge_dict.get("node", {}).get("sku", {})

            options_edges = edge_dict.get("node", {}).get("options", {}).get("edges", [])   # your JSON list

            variant = {}

            price_data = {}

            for option in options_edges:
                node = option.get("node", {})

                option_id = node.get("entityId")   # 141, 140
                
                display_name = node.get("displayName")
                values_edges = node.get("values", {}).get("edges", [])

                for val in values_edges:
                    val_node = val.get("node", {})                    
                    label = val_node.get("label")

                    # Clean label (optional: remove quotes)
                    if label:
                        label = label.replace('"', '')

                    if display_name and label:
                        variant[display_name] = label

                    value_id = val_node.get("entityId")   # 231, 230

                    if option_id and value_id:
                        key = f"attribute[{option_id}]"
                        price_data[key] = str(value_id)

            price_data["action"] = "action"
            price_data["product_id"] = product_entity_id

            product_detail_data = {
                "product_url_id" : product_table_id,
                "category_name" : category_name,
                "product_entity_id" : product_entity_id,
                "product_name" : product_name,
                "product_url" : product_url,
                "variants" : json.dumps(variant)

            }



            # ------price_detail call---------
            single_product_dict = price_detail(product_url, price_data, product_entity_id, folder_path, product_detail_data, variant_sku)

            product_list_data.append(single_product_dict)

            if len(product_list_data) >= 200:
                insert_product_detail_table(list_data=product_list_data)
                product_list_data.clear()
                print("data is product_list_data ", len(product_list_data))

        update_buy_plastic_url_status(product_name, "success")

    insert_product_detail_table(list_data=product_list_data)




from concurrent.futures import ThreadPoolExecutor, as_completed

def run_threaded_fetch(buy_plastic_url_list, max_threads=5):

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [
            # pass ONE dict as list → because your function expects list
            executor.submit(fetch_product_detail, [dict_data] )
            for dict_data in buy_plastic_url_list
        ]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print("Thread error:", e)
    print("process done....")






def variants_data(data, child_sku):

    edge_list = data.get("data", {}).get("site", {}).get("product", {}).get("variants", {}).get("edges", [])

    for edge_dict in edge_list:

        if edge_dict.get("node", {}).get("sku") == child_sku:

            options_edges = edge_dict.get("node", {}).get("options", {}).get("edges", [])   # your JSON list

            variant = {}

            for option in options_edges:
                node = option.get("node", {})

                display_name = node.get("displayName")
                values_edges = node.get("values", {}).get("edges", [])

                for val in values_edges:
                    val_node = val.get("node", {})                    
                    label = val_node.get("label")

                    # Clean label (optional: remove quotes)
                    if label:
                        label = label.replace('"', '')

                    if display_name and label:
                        variant[display_name] = label
            break
    return variant


def read_file_usin_sku(list_data:list):
    print("data lenght : ", len(list_data))
    base_path = r"D:\vishal_kushvanshi\buy_plastic_request\variants_pages"

    read_file_data_list = []
    for dict_data in list_data:
        
        parent_id = dict_data.get("parent_id")
        parent_category_name = dict_data.get("parent_category_name")
        parent_product_entity_id = dict_data.get("parent_product_entity_id")
        parent_sku = dict_data.get("parent_sku")
        child_sku = dict_data.get("child_sku")
        child_id = dict_data.get("child_id")
        child_product_name = dict_data.get("child_product_name")
        child_product_url = dict_data.get("child_product_url")
        
        print("product data : ", parent_id, parent_category_name, parent_product_entity_id, parent_sku, child_sku, child_id, child_product_name, child_product_url)

        #  Step 1: Check parent folder
        parent_path = os.path.join(base_path, parent_sku)

        if not os.path.isdir(parent_path):
            print(" not file Parent folder not found:", parent_path)
            continue


        # -------check variants---------
        variant = {}

        variant_path = os.path.join(parent_path, f"variants_data.zip")
        if not os.path.isfile(variant_path):
            print(" not file  ZIP file not found:", variant_path)
            continue

        #  Step 3: Read JSON from ZIP
        try:
            with zipfile.ZipFile(variant_path, 'r') as zipf:

                # Check file exists inside ZIP
                if "products.json" not in zipf.namelist():
                    print("not file  products.json not found inside ZIP")
                    continue

                with zipf.open("products.json") as f:
                    variants_file_data = json.load(f)

                    with open("variants_file_data.json", "w", encoding='utf-8') as f :
                        json.dump(variants_file_data, f, indent=4)

                    variant = variants_data(variants_file_data, child_sku)

        except Exception as e:
            print(" Error reading variant_path:", e)



        # -------check price file-------
        #  Step 2: Build ZIP path
        zip_path = os.path.join(parent_path, f"{child_sku}.zip")

        if not os.path.isfile(zip_path):
            print(" not file ZIP file not found:", zip_path)
            continue

        #  Step 3: Read JSON from ZIP
        try:
            with zipfile.ZipFile(zip_path, 'r') as zipf:

                # Check file exists inside ZIP
                if "products.json" not in zipf.namelist():
                    print(" not file products.json not found inside ZIP")
                    continue

                with zipf.open("products.json") as f:
                    data = json.load(f)

                    with open("read_file_using_table.json", "w", encoding='utf-8') as f :
                        json.dump(data, f, indent=4)



                        product_detail_data = {
                            "product_url_id" : parent_id,
                            "category_name" : parent_category_name,
                            "product_entity_id" : parent_product_entity_id,
                            "parent_sku" : parent_sku,
                            "product_name" : child_product_name,
                            "product_url" : child_product_url,
                            "variants" : json.dumps(variant)

                        }

                        base_price = data.get("data").get("price").get("without_tax").get("value")  # you must provide this

                        result = []

                        for item in data.get("data").get("bulk_discount_rates"):
                            min_qty = item["min"]
                            max_qty = item["max"]
                            discount = item["discount"]["value"]

                            # calculate discounted price
                            final_price = base_price * (1 - discount / 100)

                            # format range text
                            if max_qty == 0:
                                qty_text = f"Buy {min_qty} or above"
                            else:
                                qty_text = f"Buy {min_qty} - {max_qty}"

                            text = f'{qty_text} for ${final_price:.2f} each ({discount}% off)'
                            result.append(text)

                        product_detail_data["child_sku"] =  data.get("data").get("sku")
                        product_detail_data["price"] = data.get("data").get("price").get("without_tax").get("formatted")
                        product_detail_data["bulk_pricing"] = json.dumps(result)

                        read_file_data_list.append(product_detail_data)

        except Exception as e:
            print(" Error reading ZIP:", e)


        if len(read_file_data_list) >= 200:
            insert_product_detail_using_file_table(list_data =read_file_data_list)
            read_file_data_list.clear()


        # break
    
    insert_product_detail_using_file_table(list_data =read_file_data_list)
    
