import requests
import pandas as pd

def search_yelp(client_id, api_key, term, location, radius):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    params = {
        'term': term,
        'location': location,
        'radius': radius,
        'categories': 'libraries,bookstores',
        'sort_by': 'distance'
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()['businesses']
    
    results = []
    
    for business in data:
        result = {
            'Name': business['name'],
            'Address': 'Insert_address '.join(business['location']['display_address']),
            'Website': business['url'],
            'Phone': business['phone']
        }
        results.append(result)

    return results

def main():
    client_id = 'Yelp_Client_ID'
    api_key = 'Your_Yelp_API'
    location = 'insert location'
    radius = 40000  # Maximum allowed radius in meters (about 24.85 miles)

    data = search_yelp(client_id, api_key, '', location, radius)

    df = pd.DataFrame(data)
    df.to_csv('bookstores_and_libraries.csv', index=False)

if __name__ == '__main__':
    main()
