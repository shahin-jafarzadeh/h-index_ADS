import os
print(os.getpid())

import requests
import sys

ORCID_ID = sys.argv[1]

endpoint = "https://api.adsabs.harvard.edu/v1/search/query"

params = {
    "q": f"orcid:{ORCID_ID}",
    "fl": "citation_count",
    "sort": "citation_count desc",
    "rows": 200
}

headers = {
    "Content-type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer Your_ADS_API_Token"
}

# Make the API request
response = requests.get(endpoint, headers=headers, params=params)

papers = response.json()["response"]["docs"]

h_index = 0
for i, paper in enumerate(papers):
    if paper["citation_count"] >= i+1:
        h_index = i+1
    else:
        break

print(h_index)
