from bs4 import BeautifulSoup
import requests


def get_package_name(app_friendly_name):
    r = requests.get('https://play.google.com/store/search?q=' + app_friendly_name + '&c=apps')
    soup = BeautifulSoup(r.text, features='lxml')
    search_results = soup.findAll("div", {"class": "card no-rationale square-cover apps small"})
    first_result = search_results[0]
    package_name_of_first_result = first_result['data-docid']
    return package_name_of_first_result


def get_rating_by_app_package_name(app_package_name):
    r = requests.get('https://play.google.com/store/apps/details?id=' + app_package_name)
    soup = BeautifulSoup(r.text, features='lxml')
    average_rating = soup.select_one('div.BHMmbe').text
    return average_rating


def get_rating_by_simple_name(simple_app_name):
    package_name = get_package_name(simple_app_name)
    rating = get_rating_by_app_package_name(package_name)
    return package_name, rating

#package_name, rating = get_rating_by_simple_name('facebook')

