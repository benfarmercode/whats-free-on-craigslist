import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


CRAIGSLIST_SEARCH_URL_TEMPLATE = '{url_location}/search/zip?query={query}&s={result_index}'
CRAIGSLIST_IMG_URL_TEMPLATE = 'https://images.craigslist.org/{}_300x300.jpg'
CRAIGSLIST_GEO_URL = 'https://geo.craigslist.org/iso/us'


# PUBLIC ###
def craigslist_create_search_url(search_obj):
    url = CRAIGSLIST_SEARCH_URL_TEMPLATE.format(
            url_location=search_obj.location,
            query=quote_plus(search_obj.search),
            result_index=search_obj.result_index,
    )
    return url


def craigslist_search(url):
    # CREATE Beautiful Soup PARSER OBJECT https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    soup = create_html_parser_object(url)

    # GET ALL RESULTS AS AN ARRAY
    results = get_array_of_results(soup)
    total_results = get_total_results_count(soup)
    listings_data = []

    # ITERATE THROUGH RESULTS AND STORE DATA TO DB - Data: Title, Url, Price, and Image
    for result in results:
        result_listing_data = parse_result_for_listing_data(result)
        listings_data.append(result_listing_data)

    return listings_data, total_results


def craigslist_get_geo_locations():
    soup = create_html_parser_object(CRAIGSLIST_GEO_URL)
    locations_list = soup.find(class_='geo-site-list').find_all('li')
    locations_data = []
    for location in locations_list:
        name = location.contents[0].string
        url = location.contents[0]['href']
        locations_data.append((name, url))

    return locations_data


# PRIVATE ###
def create_html_parser_object(url):
    return BeautifulSoup(requests.get(url).text, features="html.parser")


def get_array_of_results(soup):
    return soup.find_all('li', {'class': 'result-row'})


def get_total_results_count(soup):
    return soup.find('span', {'class': 'totalcount'}).text


def get_result_title(result):
    return result.find(class_='result-title').text


def get_result_url(result):
    return result.find('a').get('href')


def get_result_hood(result):
    if (result.find(class_='result-hood')) is not None:
        hood = result.find(class_='result-hood').text
        hood = hood.replace("(", "").replace(')', '')
    else:
        hood = "unspecified"
    return hood


def get_result_image_url(result):
    if get_result_image_ids(result):
        # get first id only
        image_id = get_result_image_ids(result).split(',')[0]
        # remove first two characters of ID so URL works
        image_id = image_id[2:]
        # format url
        image_url = CRAIGSLIST_IMG_URL_TEMPLATE.format(image_id)
    else:
        image_url = 'https://craigslist.org/images/peace.jpg'
    return image_url


def get_result_image_ids(result):
    return result.find(class_='result-image').get('data-ids')


def parse_result_for_listing_data(result):
    title = get_result_title(result)
    url = get_result_url(result)
    image_url = get_result_image_url(result)
    hood = get_result_hood(result)

    listing_data = {
        'title': title,
        'url': url,
        'image_url': image_url,
        'hood': hood,
    }

    return listing_data

