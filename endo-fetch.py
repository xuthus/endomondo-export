import requests
import json
import time
import simplejson

url = "https://www.endomondo.com"

headers = {
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    'Cookie': "_pxvid=8a0ddc84-cc07-11e9-8df2-0242ac120005; acceptCookies=1; EndomondoApplication_AUTO=; EndomondoApplication_AUTH=\"03C5C19DDA8806297131452FDF125012Geo%2FFv8GZS6iwfznjCdZ%2BrOTv%2B%2BiFvD4GSAb5f8FH2TCuL3XreYGdiW6EFN1l4E5woHjf9gUAKh%2FOVBYiqY%2FPepqOBXBxWQXTBlK7i5zOuY%3D\"; EndomondoApplication_USER=\"xuthus%40yandex.ru\"; CSRF_TOKEN=vpp5iavdh39ejirnv4ge45hp13; USER_TOKEN=4D5F863EEBEA5EE50F6157B028BE9441NFWs0Ki%2BrWrNj5p%2BM1ZoxKTgTRfmFQq1bBq3jBdL6MrW5AJrSPCtZQE%2F0RNTFr%2Bo2AnftrgkCWtrButRyBC65o29leItpgsnRZWs%2BN%2FYHZk%3D; JSESSIONID=B9CE828BA7C7310E1EAF3E0410DA18C5; AWSELB=13FDC17D1C2B68745BCB41EBB6BDDC3DB8274D93D6797D6E0363C55C4CE08D156BB62D54D9352B5710EB296F3617DAF82F303C3A2CB45EB3F96E7351D857D387B23F3D62FEB915F8B5B489E027B5FB8178E7870C24",
    'DNT': "1",
    'Referer': "https://www.endomondo.com/home",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.107",
    'x-csrf-token': "vpp5iavdh39ejirnv4ge45hp13",
    'Cache-Control': "no-cache",
    'Postman-Token': "afff7a10-2c52-4836-88fe-1d0ffcaee637,668dd1bb-a846-4b59-9235-130006945fb0",
    'Host': "www.endomondo.com",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}


offset = int(time.time()) * 1000

next = "/rest/v1/feeds/subscriptions?expand=feed:full&limit=10&offset=%s" % offset


workouts = []

count = 0
while len(next) > 10:
    count += 1
    print("Request: %s..." % count)
    print(next)
    response = requests.request("GET", "{}{}".format(url, next), headers=headers)
    payload = json.loads(response.text)
    cnt = 0
    for workout in payload["data"]:
        cnt += 1
        workouts.append(workout)
    if cnt == 0:
        break
    next = payload["paging"]["next"]


with open('workouts-all.json', 'w') as f:
    simplejson.dump(workouts, f)