from bs4 import BeautifulSoup
import requests
from time import sleep


class AppStats:
    def __init__(self, title, package_name, developer, category, price, system, total_ratings, rating):
        self.title = title
        self.package_name = package_name
        self.developer = developer
        self.category = category
        self.price = price
        self.system = system
        self.total_ratings = total_ratings
        self.rating = rating

    def __str__(self):
        delim = '|'
        return self.title + delim + self.package_name + delim + self.developer + delim + self.category + delim + self.price + delim + self.system + delim + self.total_ratings + delim + self.rating


def get_stats_from_app_page(url):
    # https://www.androidrank.org/application/soundtrack_quiz_music_quiz/com.m123.soundtrackquiz?hl=en

    # get the package name from the url
    last_url_part = url.split('/')[-1]
    package_name = last_url_part.split('?')[0]

    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, features='lxml')
    tables = soup.select('table.appstat')
    stats_table = tables[0].text
    ratings_table = tables[1].text

    # stats_table will look like this:
    # Title:Facebook
    # Developer:Facebook
    # Category:Social
    # Price:Free
    # System:Android

    # ratings_table will look like this:
    # Rating scores
    #
    # Total ratings:78988863
    # Growth (30 days):0.46%
    # Growth (60 days):1.14%
    # Average rating:4.064

    for line in stats_table.splitlines():
        if line.startswith('Title'):
            title = line.split(':')[1]
        if line.startswith('Developer'):
            developer = line.split(':')[1]
        if line.startswith('Category'):
            category = line.split(':')[1]
        if line.startswith('Price'):
            price = line.split(':')[1]
        if line.startswith('System'):
            system = line.split(':')[1]

    for line in ratings_table.splitlines():
        if line.startswith('Total ratings'):
            total_ratings = line.split(':')[1]
        if line.startswith('Average rating'):
            rating = line.split(':')[1]

    app = AppStats(title, package_name, developer, category, price, system, total_ratings, rating)

    return app

app_urls_file = open('app_urls.txt', 'a')


def get_app_urls_on_page(url):
    print('get_app_urls_on_page: ' + url)
    base_url = 'https://www.androidrank.org'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, features='lxml')
    table = soup.find('table', 'table')
    links = table.findAll('a')

    all_app_urls = []
    for link in links:
        if link['href'].startswith('/application'):
            new_app_url = base_url + link['href']
            app_urls_file.write(new_app_url + '\n')
            all_app_urls.append(new_app_url)

    return all_app_urls


def get_all_page_urls():
    all_urls = []
    first_page = 'https://www.androidrank.org/listcategory?category=&price=all&hl=en'
    #all_urls.append(first_page)

    start_num = 16981
    while start_num <= 46201:
        next_url = 'https://www.androidrank.org/listcategory?category=&start=' + str(start_num) + '&sort=0&price=all&hl=en'
        all_urls.append(next_url)
        start_num += 20

    return all_urls

# print('Getting the url for every single page that lists apps...')
# all_page_urls = get_all_page_urls()
#
# print ('For every single page, getting every app url on the page...')
# for page_url in all_page_urls:
#     app_urls = get_app_urls_on_page(page_url)

print('for every app url, obtaining the stats...')
app_stats = []


with open('app_urls.txt') as f:
    app_urls = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
app_urls = [x.strip() for x in app_urls]

final_rusults_file = open('final_results.txt', 'a')
for url in app_urls:
    try:
        new_app = get_stats_from_app_page(url)
    except:
        print('----Timed out....waiting for 125s----')
        sleep(125)
        continue
    try:
        print(new_app)
        final_rusults_file.write(str(new_app) + '\n')
        app_stats.append(new_app)
    except:
        pass
