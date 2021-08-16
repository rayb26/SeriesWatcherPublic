# Code created by Rayhan Biju 2021
from urllib.request import urlopen

import requests

import json

from lxml.html import parse

url = "https://imdb8.p.rapidapi.com/title/find"

headers = {
    # add your api keys here from rapidapi
}



def get_items_as_dict(title):
    query_str = {"q": title}
    response_data = requests.request("GET", url, headers=headers, params=query_str)
    json_data = json.loads(response_data.text)

    query_param = {"tconst": get_id(title), "currentCountry": "US"}
    specified_url = "https://imdb8.p.rapidapi.com/title/get-overview-details"

    response_data_image = requests.request("GET", specified_url, headers=headers, params=query_param)

    if '400' in response_data_image.text:
        return {'id': "Not Found",
         'number_of_episodes': "Not Found",
         'image': "Not Found",
         'description': "Not Found"
         }
    json_data_image = json.loads(response_data_image.text)

    if 'plotOutline' in json_data_image:
        description = json_data_image['plotOutline']['text']

    if 'results' not in str(json_data) or 'title' not in str(json_data_image) or 'plotOutline' not in str(json_data_image):
        return "Not Found"

    try:
        id = str(json_data['results'][0]['id'].split("title/")[1].split("/")[0])
        number_of_episodes = str(json_data['results'][0]['numberOfEpisodes'])
        image = json_data_image['title']['image']['url']
    except IndexError:
        return "Not Found"

    return {'id': id,
            'number_of_episodes': number_of_episodes,
            'image': image,
            'description': description
            }

def get_id(title):
    query_str = {"q": title}
    response_data = requests.request("GET", url, headers=headers, params=query_str)

    json_data = json.loads(response_data.text)

    if 'results' not in json_data:
        return "Not Found"

    try:
        return str(json_data['results'][0]['id'].split("title/")[1].split("/")[0])
    except IndexError:
        return "Not Found"


def get_number_of_episodes(title):
    query_str = {"q": title}
    response_data = requests.request("GET", url, headers=headers, params=query_str)

    json_data = json.loads(response_data.text)

    if 'numberOfEpisodes' not in response_data.text:
        return "Not Found"

    return str(json_data['results'][0]['numberOfEpisodes'])

def get_coming_soon():
    specified_url = "https://imdb8.p.rapidapi.com/title/get-coming-soon-tv-shows"
    query_param = {"currentCountry": "US"}

    response_data = requests.request("GET", specified_url, headers=headers, params=query_param)

    json_data = json.loads(response_data.text)

    coming_soon_titles = []
    for data in json_data:
        coming_soon_titles.append(data.split("title/")[1].split("/")[0])

    return coming_soon_titles


def convert_id_to_titles(title_list):
    new_list_titles = []

    for title_id in title_list:
        new_list_titles.append(__convert_coming_soon_title__(title_id))

    return new_list_titles


def __convert_coming_soon_title__(title_id):

    url_to_go = 'https://www.imdb.com/title/{title_id}/'.format(title_id=title_id)

    page = urlopen(url_to_go)
    page_data = parse(page)

    return page_data.find(".//title").text.split('"')[1].split('"')[0]


def get_link_coming_soon(title_id):
    return 'https://www.imdb.com/title/{title_id}/'.format(title_id=title_id)
