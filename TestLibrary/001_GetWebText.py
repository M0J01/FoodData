
from requests import get

url = 'https://api.nal.usda.gov/ndb/reports/?ndbno=11090&type=f&format=json&api_key=swc6iwKitEP0BtugYQn8Wo4nwWtn4uHrMDQWpxTc'

response = get(url)

print(response.text)