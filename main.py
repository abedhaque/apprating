from flask import Flask
from google_play_rating import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'apprating.azurewebsites.com/rating/<comma separated list of app names>...'


@app.route('/rating/<names_csv>')
def ratings(names_csv):
    names = names_csv.split(',')
    result = ''
    for name in names:
        package_name, rating = get_rating_by_simple_name(name)
        result = result + '<br/>' + str(package_name) + ': ' + str(rating)
    return result


if __name__ == "__main__":
    app.run()
