import requests
import time
import random


r = requests.get(r"https://www.instagram.com/graphql/query/?query_hash=3913773caadd10357fba8b1ef4c89be3&variables=%7B%22id%22%3A%22427553890%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFBUUdXZW9RTmMzc2dycUdVcUN3N28xUHlmLXNtOUM5Rjk5a2pxWExSSUJZM1NQbHN1cFA2Y1hWazJ0OHZWVlJ0VGFaZkFSLXFiUTd0UmR2LXc0V194Tw%3D%3D%22%7D")


index = 1

while True:

    my_json = r.json()

    has_next = my_json["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]

    tam = len(my_json["data"]["user"]["edge_owner_to_timeline_media"]["edges"])


    
    for i in range(tam):
        print(f"{index} - {my_json['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['thumbnail_resources'][4]['src']}")

        index += 1
    
    if not has_next:
        break

    end_cursor = my_json["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"].replace("==", "")

    time.sleep(random.randint(3, 8))
    
    r = requests.get(f"https://www.instagram.com/graphql/query/?query_hash=3913773caadd10357fba8b1ef4c89be3&variables=%7B%22id%22%3A%22427553890%22%2C%22first%22%3A12%2C%22after%22%3A%22{end_cursor}%3D%3D%22%7D")



        