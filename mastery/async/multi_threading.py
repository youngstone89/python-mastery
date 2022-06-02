import requests
import time
from concurrent.futures import ProcessPoolExecutor


def fetch_url_data(pg_url):
    try:
        resp = requests.get(pg_url)
    except Exception as e:
        print(f"Error occured during fetch data from url{pg_url}")
    else:
        return resp.content


def get_all_url_data(url_list):
    with ProcessPoolExecutor() as executor:
        resp = executor.map(fetch_url_data, url_list)
    return resp


if __name__ == '__main__':
    url = "https://www.velotio.com/careers"
    for ntimes in [1, 10, 50, 100, 500]:
        start_time = time.time()
        responses = get_all_url_data([url] * ntimes)
        print(
            f'Fetch total {ntimes} urls and process takes {time.time() - start_time} seconds')
