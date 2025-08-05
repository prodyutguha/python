import requests
from requests.auth import HTTPBasicAuth
import json

# Jira config
jira_domain = "kloudguardian.atlassian.net"
email = "prodyut@kloudguardian.com"
api_token = "ATATT3xFfGF0ZzuSGTPDDOgK2ecvGU_eWbjmB9y5drsITP6nxHNZ8SQ7c0UmxnffbKeJN3YR-kSozT4G5AIeQHm0O5PNwLvlqtkFCTAtpaMu4FPGhwypvFGR3cVfZMtCwHDoTY-dTdJ3hK4Zze_Z_Q-lw_1bo4V33trirz0Gxz8O3LYKb3dXAE8=65651183"

# JQL query (customize this!)
jql_query = "project = Azure AND status = 'To Do'"

# API URL
url = f"https://{jira_domain}/rest/api/3/search"

# Headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Query parameters
params = {
    "jql": jql_query,
    "maxResults": 10
}

# Make the request
response = requests.get(
    url,
    headers=headers,
    params=params,
    auth=HTTPBasicAuth(email, api_token)
)

if response.status_code == 200:
    data = response.json()
    issues = data.get("issues", [])
    for issue in issues:
        key = issue["key"]
        summary = issue["fields"]["summary"]
        print(f"{key}: {summary}")
else:
    print(f"Failed to fetch issues: {response.status_code}")
    print(response.text)
