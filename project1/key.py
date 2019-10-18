import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "eQMPpVGHwnK4lJEym9l91Q", "isbns": "9781632168146"})
print(res.json())
