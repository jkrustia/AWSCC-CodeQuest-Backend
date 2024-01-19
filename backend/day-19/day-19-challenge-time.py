import requests

api_url = "https://api.spacexdata.com/v5/launches/latest"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    launch_name = data.get("name", "No names found.")
    launch_date = data.get("date_local", "No dates found.")

    print("Latest SpaceX Launch Data")
    print("=========================")
    print(f"Mission Name: {launch_name}")
    print(f"Launch Date: {launch_date}")

else:
    print(f"Request failed with status code: {response.status_code}")