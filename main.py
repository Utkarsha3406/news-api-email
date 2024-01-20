import requests

api_key = "f5c2405698424f49a3021adad460bd19"
url="https://newsapi.org/v2/everything?q=tesla&from=2023-12-20&sortBy=pub" \
    "lishedAt&apiKey=f5c2405698424f49a3021adad460bd19"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

