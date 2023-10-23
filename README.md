# Google Places API Data Retrieval and Display

This project demonstrates how to use the Chalice framework to create an AWS Lambda-powered API for retrieving data from the Google Places API and displaying it in an HTML table. Additionally, it provides a simple PHP-based frontend for interacting with the API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Chalice Installation](#chalice-installation)
- [Chalice Deployment](#chalice-deployment)
- [Usage](#usage)
- [Frontend](#frontend)
- [API Key](#api-key)
- [License](#license)

## Prerequisites

Before you get started, make sure you have the following requirements:

- [Python](https://www.python.org/downloads/)
- [Chalice](https://chalice.readthedocs.io/en/latest/)
- A web server or hosting environment to run the PHP frontend (e.g., Apache, Nginx).

## Chalice Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd google-places-api-chalice
   pip install chalice
   python -m venv venv
   source venv/bin/activate
   chalice deploy

   Note the API endpoint URL provided after deployment. You'll use this URL to interact with the API.
   ```

## Usage

This Chalice-powered AWS Lambda API provides two main endpoints for retrieving Google Places data:

Search for Places: You can search for places by sending a GET request to /{api_endpoint}/places/{query}, where {api_endpoint} is the URL provided after deployment and {query} is your search term.

Retrieve Place Details: To retrieve detailed information about a place, send a GET request to /{api_endpoint}/place/{place_id}, where {api_endpoint} is the URL provided after deployment and {place_id} is the unique identifier of the place.

## Frontend

The project includes a simple HTML/PHP frontend for interacting with the Chalice API. Place this code in a directory accessible by a web server:
Make sure to replace the placeholder in the <form> tag's action attribute with your API endpoint URL.

## API Key

To use the Google Places API, you need to obtain an API key. Follow the instructions in the Google Places API documentation to obtain a key. Replace the api_key variable in the Chalice code with your API key.

api_key = 'YOUR_API_KEY_HERE'

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize and expand this README as needed to provide more details about your project. Include examples, acknowledgments, and any other relevant information that helps users understand and use your code.

Please replace `https://github.com/pavitsingh87/googlemapsapi` with the URL of your actual repository and make any other necessary customizations to fit your project.
