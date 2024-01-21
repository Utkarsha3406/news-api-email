import requests
from send_email import send_email

topic = "tesla"
api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=890603a55bfa47048e4490069ebee18c&" \
      "language=en"

# Make request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get a dictionary with data
    content = response.json()

    # Access the article titles and description
    body = ""
    for article in content["articles"][:20]:
        if article["title"] is not None:
            body = "Subject: Today's news" \
                   + "\n" +body + article["title"] +"\n" \
                   + article["description"] \
                   + "\n" + article["url"] + 2*"\n"

    # If your send_email function expects a string, skip the encoding
    # If it expects bytes, you can keep the encoding
    body = body.encode("utf-8")

    if body:
        send_email(message=body)
    else:
        print("No valid articles found.")
else:
    print(f"Failed to fetch news. Status code: {response.status_code}")
