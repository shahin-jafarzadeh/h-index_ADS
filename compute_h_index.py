import os
import requests
import sys

# Print the process ID (for tracking purposes)
print(os.getpid())

# Get the ORCID_ID from the command line argument
ORCID_ID = sys.argv[1]

# Define the endpoint and parameters for the ADS API
endpoint = "https://api.adsabs.harvard.edu/v1/search/query"

params = {
    "q": f"orcid:{ORCID_ID}",
    "fl": "citation_count",
    "sort": "citation_count desc",
    "rows": 200
}

# Define headers including the API token (replace 'Your_ADS_API_Token' with your actual token)
headers = {
    "Content-type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer Your_ADS_API_Token"
}

# Make the API request
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()  # Check if the request was successful (status code 200)
    
    # Parse the response as JSON
    papers = response.json()["response"]["docs"]

    # Calculate the h-index
    h_index = 0
    for i, paper in enumerate(papers):
        if paper["citation_count"] >= i + 1:
            h_index = i + 1
        else:
            break

    # Print the h-index
    print(h_index)

except requests.exceptions.RequestException as e:
    # Handle any request-related errors, such as server issues
    print(f"ADS server down temporarily!")
