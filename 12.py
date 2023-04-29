import requests
from bs4 import BeautifulSoup
import csv
import time


def scrape_movies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts_list = soup.find('ul', {'class': 'scripts-list'})
    a_elements = scripts_list.find_all('a')
    return [a.text for a in a_elements]



with open('movies.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    header = ['Movie Name']
    writer.writerow(header)

    for page in range(1, 4):
        url = f'https://subslikescript.com/movies?page={page}'
        movies = scrape_movies(url)
        for movie in movies:
            row = [movie]
            writer.writerow(row)
        print(f'Page {page}: {movies}\n')
        time.sleep(15)
