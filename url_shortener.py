import requests


api_key = "ca08497023ee898260bae6c99585beed42e23"
url = input("Enter your URl: ")
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

data = requests.get(api_url).json()["url"]

if len(url) > 250:
    print("Please insert the url at least with 250 characters")


if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)