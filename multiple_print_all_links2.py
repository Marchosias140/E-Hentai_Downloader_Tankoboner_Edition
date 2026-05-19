import requests
from bs4 import BeautifulSoup

def get_all_links(urls):
    for url in urls:
        try:
            # Send a GET request to the URL
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Check for HTTP errors

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all 'a' tags that have an 'href' attribute
            links = soup.find_all('a', href=True)

            print(f"--- Results for: {url} ---")
            print(f"Found {len(links)} links.\n")
            
            for link in links:
                address = link['href']
                print(address)
            
            print("\n" + "="*30 + "\n")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while accessing {url}: {e}\n")

if __name__ == "__main__":
    # Add as many URLs as you like to this list
    target_urls = [





        
    ]
    
    get_all_links(target_urls)
