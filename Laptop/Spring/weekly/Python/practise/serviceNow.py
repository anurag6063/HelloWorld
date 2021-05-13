#Need to install requests package for python
#easy_install requests
import requests
import json

# Set the request parameters
url = 'https://broadcomcsmdev.service-now.com/api/avts2/fetchproductcases/Notes/BCM84794'

# Eg. User name="admin", Password="admin" for this code sample.
#user = 'anurag6063@gmail.com'
#pwd = '@Matrixm6063'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization":"Basic YXBpLWFkbWluOjEyMw=="}

# Do the HTTP request
response = requests.get(url, headers=headers  )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
#print(data)

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
