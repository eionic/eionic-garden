import requests
import json

def find_grants(api_url, query):
    params = {
        'query': query,
        'api_key': 'YOUR_API_KEY'
    }
    response = requests.get(api_url, params=params)
    return response.json()

def main():
    api_url = 'https://api.grant.gov/search'
    query = 'artificial life'
    grants = find_grants(api_url, query)
    for grant in grants['results']:
        print(grant['title'])

if __name__ == '__main__':
    main()