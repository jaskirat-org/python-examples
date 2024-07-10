API_KEY = "abcd1234" 

def access_api(endpoint):
  url = f"https://api.example.com/{endpoint}"
  headers = {"Authorization": f"Bearer {API_KEY}"}
  response = requests.get(url, headers=headers)

access_api("users")
