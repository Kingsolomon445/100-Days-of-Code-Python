from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
response.raise_for_status()
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')
movies_title= soup.find_all('h3', class_='title')
movies_list = [movie.get_text() for movie in movies_title]
movies_list = movies_list[::-1]
print(movies_list)

with open("movies.txt", 'w') as file:
    for movie in movies_list:
        file.write(movie + '\n')