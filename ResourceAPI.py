import requests
import time
import sys

api_base_url = "https://demo.threedy.io"

request_url = api_base_url + "/api/resource/v1/request"
status_url = api_base_url + "/api/resource/v1/status"

# List of URLs of resources to be transcoded
data_urls = [
    "urn:x-i3d:examples:catia:bike",
    "https://this-file-does-not-exist.jt",
]

# Prepare transcoding payload by putting every URL into a dictionary
uri_elements = []
for url in data_urls:
    uri_element = {"uri": url}
    uri_elements.append(uri_element)
transcoding_payload = {"elements": uri_elements}

print("Initiating transcoding process...")

request_response = requests.post(request_url, json=transcoding_payload)

# Exit if the request was unsuccessful
if request_response.status_code != 200:
    print("Request failed with status code:", request_response.status_code)
    sys.exit(1)

# Get the list of resources being transcoded
all_resources = request_response.json()["handles"]
# Initialize sets to keep track of successfully and unsuccessfully transcoded resources
transcoded_resources = set()
failed_resources = set()

# Poll the status endpoint until all resources have either been transcoded or failed
while len(transcoded_resources | failed_resources) < len(all_resources):

    print("Checking transcoding status...")
    # Check the status of the transcoding process
    status_response = requests.post(status_url, json=request_response.json())

    # Exit the program if the request was unsuccessful
    if status_response.status_code != 200:
        print("Failed to get transcoding status with status code:", status_response.status_code)
        sys.exit(1)

    status_data = status_response.json()
    resource_status_responses = status_data["resources"]

    # Check the status of each resource and update the corresponding sets
    for i, resource in enumerate(resource_status_responses):
        if resource["status"] == "closed" and i not in transcoded_resources:
            print(f"Resource {i}: transcoded!")
            transcoded_resources.add(i)
        elif resource["status"] in {"warning", "error"} and i not in failed_resources:
            print(f"resource {i}: {resource['status']}")
            failed_resources.add(i)
        else:
            print(f"Resource {i}: {resource['status']}")

    # Pause before the next poll
    time.sleep(1)

# Print the URLs of the successfully and unsuccessfully transcoded resources
print("\nSuccessfully transcoded:")
for i in transcoded_resources:
    print(data_urls[i])

print("Transcoding failed:")
for i in failed_resources:
    print(data_urls[i])