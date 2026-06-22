### m06/wikigame3.py
import requests
import json

def grab_links(title):
    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'https'
    hostname = 'en.wikipedia.org'
    path = '/w/api.php'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'action': 'parse',
             'page': title,
             'prop': 'links',
             'section': 0,
             'format': 'json'
    }

    response = requests.get(url, params=query, headers={'user-agent':'cs32x educational demo'})

    # Read the response body in JSON format
    j = response.json()

    print()

    # Print titles of links from response body
    links_data = j["parse"]["links"]
    links = [l["*"] for l in links_data if l["ns"] == 0]
    for i, link in enumerate(links):
        print(i, link)
    
    print()

    return links

def main():
    # Print a welcome message
    # Grab the player's start and goal articles

    # Loop until goal article is reached
        # Grab and print the article titles linked within the current article
        # Ask the player to select the next article
        # Update the current article to the title the player selected

    # Print a congratulatory message

if __name__ == '__main__':
    main()