import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://forecast.weather.gov/product.php?site=NWS&issuedby=HUN&product=AFD&format=CI&version=1&glossary=1'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        pre_tag = soup.find('pre', class_='glossaryProduct')
        if pre_tag:
            text_content = pre_tag.get_text()
            return text_content
        else:
            print("No <pre class='glossaryProduct'> tag found in the HTML file.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    main()