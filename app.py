from chalice import Chalice
import requests
from urllib.parse import unquote

app = Chalice(app_name='getLatLongScarping')

# Define the API key
#List of all Keys
api_key = ''


def get_place_ids(api_key, query, num_results=1000):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": api_key,
    }

    place_ids = []
    while len(place_ids) < num_results:
        response = requests.get(base_url, params=params)
        result = response.json()

        if result["status"] == "OK" and result.get("results"):
            places = result["results"]
            place_ids += [place["place_id"] for place in places]

            # Check if there are more results
            next_page_token = result.get("next_page_token")
            if not next_page_token:
                break

            # Set the next page token for the next request
            params["pagetoken"] = next_page_token
        else:
            print(f"Error: {result['status']} - {result.get('error_message', '')}")
            break

    return place_ids

def get_place_details(api_key, place_id):
    base_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    result = response.json()

    if result["status"] == "OK":
        place_details = result["result"]
        return place_details
    else:
        print(f"Error: {result['status']} - {result.get('error_message', '')}")
        return None

@app.route('/places/{p}', methods=['GET'])
def get_places(p):
    query = unquote(p)
    
    place_ids = get_place_ids(api_key, query, num_results=1000)

    if place_ids:
        # results = []
        table_html = "<table id='example'><thead><tr><th>Place ID</th><th>Place Name</th><th>Address</th><th>Phone Number</th></tr></thead><tbody>"

        for place_id in place_ids:
            place_details = get_place_details(api_key, place_id)
            if place_details:
                table_html += "<tr>"
                table_html += f"<td>{place_id}</td>"
                table_html += f"<td>{place_details['name']}</td>"
                table_html += f"<td>{place_details['formatted_address']}</td>"
                table_html += f"<td>{place_details.get('formatted_phone_number', 'N/A')}</td>"
                table_html += "</tr>"
                # result_row = {
                #     'Place ID': place_id,
                #     'Place Name': place_details['name'],
                #     'Address': place_details['formatted_address'],
                #     'Phone Number': place_details.get('formatted_phone_number', 'N/A'),
                #     # ... Include other fields as needed ...
                # }
                # results.append(result_row)
        table_html += "</tbody></table>"
        # Return an HTML response
        return table_html
        # return results  # Return the list of results as JSON
    else:
        return {"error": "No results found"}  # Return an error response
