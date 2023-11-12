import uuid
import json

uuid_list = []
for i in range(10):
    myuuid = uuid.uuid4()
    uuid_list.append(str(myuuid))

print(uuid_list)

# Specify the file path
json_file_path = "listuuid.json"

# Convert the list to JSON and write it to a file
with open(json_file_path, "w") as json_file:
    json.dump(uuid_list, json_file, indent=2)

print(f"List has been converted and written to {json_file_path}")


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
print("\n")
print(type(data_to_post))

access_token = get_access_token(client_id, client_secret, token_url)
if access_token:
    make_authenticated_post_request(api_url, data_to_post, access_token)
else:
    print("\n")
    print("Failed to obtain Bearer Token")
