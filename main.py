import pprint
import requests

url = "https://howmanydayssincemontaguestreetbridgehasbeenhit.com"
api_route = "/api/chumps/"

response = requests.get(url + api_route)

print(response.status_code, "\n")
res = response.json()
newest = res[0]

feasts = []

for meal in res:
    feasts.append(
        {
            "date": meal["date"],
            "localised_date": meal["localised_date"],
            "url": meal["url"],
            "image": url + meal["media"][0]["url"],
            "streak": meal["streak"]
        }
    )

latest_feast = feasts[0]

print("#################################")
print("###### MONTY STREET BRIDGE ######")
print("######    DIETARY LOG      ######")
print("#################################\n")
#
# print(f'Name: {newest["name"]}')
# print(f'Slug: {newest["slug"]}')
# print(f'Date: {newest["date"]}')
# print(f'Date Order: {newest["date_order"]}')
# print(f'Thanks: {newest["thanks"]}')
# print(f'Localised Date: {newest["localised_date"]}')
# print(f'URL: {newest["url"]}')
# print(f'Media:\n\tType: {newest["media"][0]["media_type"]}\n\tURL: {url + newest["media"][0]["url"]}\n\tMedia Order: {newest["media"][0]["media_order"]}')
# print(f'Streak: {newest["streak"]}')
#
pprint.pp(feasts)