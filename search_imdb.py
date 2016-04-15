import requests
from bs4 import BeautifulSoup
import sys

def get_data(url):
    data = {}
    r = requests.get('http://www.imdb.com/search/title?title='+ url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.select('table.results > tr')

    # Top 3 results in search
    for i in range(1, 4):
        title_div = results[i].find('td', attrs= {'class' : 'title'})
        movie_title = title_div.find('a').text
        movie_year = title_div.find('span', attrs = {'class' : 'year_type'}).text
        movie_name = movie_title + ' ' + movie_year

        try:
            ratings = title_div.find('span', attrs = {'class': 'rating-rating'}).find('span', attrs = {'class', 'value'}).text
        except:
            ratings = None
            pass

        if (ratings):
            print (movie_name + ', Rating: ' + ratings)
        else:
            print (movie_name + ', No ratings yet!')

if __name__ == '__main__':
    url = sys.argv[1]
    get_data(url)
