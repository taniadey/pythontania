import uuid
import requests

foldername_list = [
    "Downstream, Renewables & Energy Solutions",
    "Integrated Gas and Upstream",
    "Corporate Functions",
    "Corporate Relations",
    "Finance",
    "Human Resources",
    "Legal",
    "Projects & Technology",
]
uuid_list = []
for i in range(10):
    myuuid = uuid.uuid4()
    uuid_list.append(myuuid)

print(uuid_list)


def get_access_token(client_id, client_secret, token_url, scope=""):
    # Prepare the payload for the token request
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    }

    # Make the token request
    response = requests.post(token_url, data=payload, verify=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        token_data = response.json()
        # Extract and return the access token
        return token_data.get("access_token")
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def make_authenticated_post_request(url, data, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=data, headers=headers, verify=False)

    if response.status_code == 200:
        print("POST request successful")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


# Example usage
client_id = "da735963-60c2-4d03-ad7e-1273bc42b4c6"
client_secret = "mg0dF8_cTZ5SwO2PSDhx_g"
token_url = "https://shell-api-stg.unily.com/connect/token"
api_url = "https://shell-api-stg.unily.com/api/v1/media/folders"  # Replace with your API endpoint
data_to_post = {
    "uniqueId": "4046d2e5-0525-4638-b6c2-56004c760c7a",
    "name": "Check2",
    "parentUniqueId": "f06b6cc7-e3fb-465b-8770-c5ed7e92e08a",
    "systemManaged": False,
}


access_token = get_access_token(client_id, client_secret, token_url)

if access_token:
    make_authenticated_post_request(api_url, data_to_post, access_token)
else:
    print("Failed to obtain Bearer Token")
