from bs4 import BeautifulSoup
import requests


def main():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    container = soup.find(id='ResultsContainer')
    jobs = container.find_all('div', class_='card-content')
    python_jobs = container.find_all(
        'h2', string=lambda text: 'python' in text.lower()
    )
    python_jobs_full = [job.parent.parent.parent for job in python_jobs]
    for job in python_jobs_full:
        title = job.find('h2', class_='title')
        company = job.find('h3', class_='company')
        location = job.find('p', class_='location')
        links = job.find_all('a')
        print(title.text.strip(),
              company.text.strip(),
              location.text.strip())
        print(links[1]['href'].strip())


if __name__ == '__main__':
    main()
