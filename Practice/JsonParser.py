import json
with open("sam.json") as file:
    json1 = json.load(file)
    res = dict(json1)
    print(res['store']['bicycle']['price'])
    print(res['store']['book'][1]['title'])

books = json1['store']['book']
print(books)

for bk in books:
    if bk['price'] < 10.00:
        print(bk)