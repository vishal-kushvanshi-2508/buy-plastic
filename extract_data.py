



import requests
import json
import os
from urllib.parse import urlencode
from store_data_database import *
import requests
import gzip
# from lxml import html
import zipfile

import requests

cookies = {
    'SF-CSRF-TOKEN': '7fd921bf-8bdf-4221-baed-cf99b5370967',
    'fornax_anonymousId': 'bd977d00-96ba-4697-ab78-3d8f2a8fc27b',
    'athena_short_visit_id': 'e8a60749-759d-4276-971c-ffe9d8f0a437:1777178279',
    'XSRF-TOKEN': '352862af887980437fe0deb081ef2d7b547968be359675e96c73e0f032b4b253',
    'lastVisitedCategory': '86',
    'SHOP_SESSION_TOKEN': '6b77d88c-e5cf-4fb2-b2c1-8d86820b2218',
    '__cf_bm': 'yl1oLBr8N3AKihYfuzlDH4LFws6NVLvGoUsP2J3Ollo-1777178279.5130982-1.0.1.1-qYZBgS3akxusI45b3CIlEprFwYtRWO0Y82yPLsIcwCeMFGLlUpfr8oHKmNbliCt7kraIaRfUw1rGr0ouiLorPTonBSKXQVVPuhPxMZCrVqMMgzYBZLk4z3IWHOWLbaLv',
    'Shopper-Pref': 'E99A5A67FECF446F8858EB83EEE343C50C9C7C79-1777783082814-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJjaWQiOlsxXSwiY29ycyI6WyJodHRwczovL2J1eXBsYXN0aWMuY29tIl0sImVhdCI6MTc3NzI5NjMyNiwiaWF0IjoxNzc3MTIzNTI2LCJpc3MiOiJCQyIsInNpZCI6MTAwMTA1ODIzOSwic3ViIjoiQkMiLCJzdWJfdHlwZSI6MCwidG9rZW5fdHlwZSI6MX0.vZfMWsBzw-jAiOtIHpG7zg75PEdqmLAnzsapFBfGWVtLP32Yd4Fm3O7ArQ2EiF27A4N68oWphpmPOOKRdk1qIg',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://buyplastic.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://buyplastic.com/materials/sheets-profiles/',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'x-sf-csrf-token': '7fd921bf-8bdf-4221-baed-cf99b5370967',
    'x-xsrf-token': '352862af887980437fe0deb081ef2d7b547968be359675e96c73e0f032b4b253',
    # 'cookie': 'SF-CSRF-TOKEN=7fd921bf-8bdf-4221-baed-cf99b5370967; fornax_anonymousId=bd977d00-96ba-4697-ab78-3d8f2a8fc27b; athena_short_visit_id=e8a60749-759d-4276-971c-ffe9d8f0a437:1777178279; XSRF-TOKEN=352862af887980437fe0deb081ef2d7b547968be359675e96c73e0f032b4b253; lastVisitedCategory=86; SHOP_SESSION_TOKEN=6b77d88c-e5cf-4fb2-b2c1-8d86820b2218; __cf_bm=yl1oLBr8N3AKihYfuzlDH4LFws6NVLvGoUsP2J3Ollo-1777178279.5130982-1.0.1.1-qYZBgS3akxusI45b3CIlEprFwYtRWO0Y82yPLsIcwCeMFGLlUpfr8oHKmNbliCt7kraIaRfUw1rGr0ouiLorPTonBSKXQVVPuhPxMZCrVqMMgzYBZLk4z3IWHOWLbaLv; Shopper-Pref=E99A5A67FECF446F8858EB83EEE343C50C9C7C79-1777783082814-x%7B%22cur%22%3A%22USD%22%2C%22funcConsent%22%3Atrue%7D',
}


import requests
import json
import zipfile
import os

def plastic_category():
    print("------START---------")

    folder = r"D:\vishal_kushvanshi\buy_plastic_request\main_pages"
    os.makedirs(folder, exist_ok=True)

    url = "https://buyplastic.com/graphql"

    after_cursor = None
    all_products = []

    page_count = 1
    while True:
        json_data = {
            "query": """
            query Products($after: String) {
              site {
                products(first: 50, after: $after) {
                  pageInfo {
                    hasNextPage
                  }
                  edges {
                    cursor
                    node {
                      entityId
                      sku
                      name
                      path
                      brand { name }
                      categories {
                        edges {
                          node {
                            name
                            entityId
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
            """,
            "variables": {"after": after_cursor}
        }

        response = requests.post(url, headers=headers, cookies=cookies, json=json_data)
        data = response.json()

        # Save into ZIP
        with zipfile.ZipFile(f"{folder}\\main_page_{page_count}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr("products.json", json.dumps(data, indent=4))
        

        # with open("main_page_json.json", "w" , encoding='utf-8') as f:
        #     json.dump(data, f, indent=4)


        edges_list = data.get("data", {}).get("site", {}).get("products", {}).get("edges", [])

        if not edges_list:
            break

        for item in edges_list:
            node = item.get("node", {})

            #  safer category extraction (your code can crash here)
            category_name = None
            category_entity_id = None
            
            for dict_data in node.get("categories", {}).get("edges", []):
                if dict_data.get("node", {}).get("name") == "Materials" :
                    continue
                elif dict_data.get("node", {}).get("name") == "Weather Resistance" :
                    continue
                elif dict_data.get("node", {}).get("name") == "Fabrication" :
                    break
                category_entity_id = dict_data.get("node", {}).get("entityId")
                category_name = dict_data.get("node", {}).get("name")

                result = {
                    "category_entity_id": category_entity_id,
                    "category_name": category_name,
                    "product_entity_id": node.get("entityId"),
                    "sku": node.get("sku"),
                    "product_name": node.get("name"),
                    "product_url": "https://buyplastic.com" + node.get("path", ""),
                    "status": "pending"
                }

                all_products.append(result)

        #  next page cursor
        after_cursor = edges_list[-1]["cursor"]

        # stop condition
        if not data["data"]["site"]["products"]["pageInfo"]["hasNextPage"]:
            break
        page_count += 1
        # break

    print(f"Total products fetched: {len(all_products)}")

    #  Save ZIP
    # with open("output.json", "w" , encoding='utf-8') as f:
    #     json.dump(all_products, f, indent=4)

    print(" Data saved successfully")

    insert_buy_plastic_url_table(list_data =all_products)

