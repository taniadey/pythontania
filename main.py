import requests
import uuid

folder_names = [
    "Downstream, Renewables & Energy Solutions",
    "Integrated Gas and Upstream",
    "Corporate Functions",
    "Corporate Relations",
    "Finance",
    "Human Resources",
    "Legal",
    "Projects & Technology",
]

payload_dict = {
    "uniqueId": None,
    "name": None,
    "parentUniqueId": "f06b6cc7-e3fb-465b-8770-c5ed7e92e08a",
    "systemManaged": "False",
}


client_id = "da735963-60c2-4d03-ad7e-1273bc42b4c6"
client_secret = "mg0dF8_cTZ5SwO2PSDhx_g"
token_url = "https://shell-api-stg.unily.com/connect/token"
api_url = "https://shell-api-stg.unily.com/api/v1/media/folders"
payload_dict = {
    "uniqueId": "4046d2e5-0525-4638-b6c2-56004c760c7a",
    "name": "Check2",
    "parentUniqueId": "f06b6cc7-e3fb-465b-8770-c5ed7e92e08a",
    "systemManaged": False,
}


def get_access_token(client_id, client_secret, token_url, scope=""):
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    }

    response = requests.post(token_url, data=payload, verify=False)

    if response.status_code == 200:
        token_data = response.json()
        return token_data.get("access_token")
    else:
        print("\n")

        print(f"Error: {response.status_code}")
        print("\n")

        print(response.text)
        return None


def make_authenticated_post_request(url, data, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=data, headers=headers, verify=False)

    if response.status_code == 200:
        print("\n")

        print("POST request successful")
        print("\n")

        print(response.json())
    else:
        print("\n")

        print(f"Error: {response.status_code}")
        print("\n")

        print(response.text)


access_token = get_access_token(client_id, client_secret, token_url)
if access_token:
    for i in range(8):
        for key, value in payload_dict.items():
            if key == "uniqueId":
                payload_dict[key] = str(uuid.uuid4())
            if key == "name":
                payload_dict[key] = folder_names.pop(0)
            else:
                continue
            print(payload_dict)
            make_authenticated_post_request(api_url, payload_dict, access_token)
else:
    print("\n")
    print("Failed to obtain Bearer Token")
