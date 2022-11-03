from bs4 import BeautifulSoup
import requests
import json

def main(args):
    get_data = requests.get('https://shop.orea.uk/products/orea-v3-small-glossy-black-limited-edition-brewer-only')
    html_parse = BeautifulSoup(get_data.content,'html.parser')
    get_orea_data = html_parse.find('script',type="application/ld+json")
    parse_json = json.loads(get_orea_data.get_text())

    pretty_data = {
        "name": parse_json['name'],
        "url": parse_json['url'],
        "image": parse_json['image'][0],
        "is_available": True if parse_json['offers'][0]['availability'] == "http://schema.org/InStock" else False
    }
    
    return {
        'body': pretty_data
    }
