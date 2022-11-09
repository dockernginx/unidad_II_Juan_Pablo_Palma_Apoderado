import requests
response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=1bd496dc7d4b4177ad37aec088993c83")
print(response.status_code)
print(response.content)