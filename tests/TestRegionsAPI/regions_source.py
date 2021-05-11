import json
import math
import requests
from urllib import request


base_url = 'https://regions-test.2gis.com/1.0/regions'
correct_country_codes = ['ru', 'kz', 'kg', 'cz']
incorrect_country_codes = ['us', 'fr', 'ua', 0, 'gb']
correct_names_substring = ["рсК", "аКт", "ВЛади", 12345]
incorrect_names_substring = ['cр', 10, ""]
min_page_number = 1
default_page_number = 1
default_page_size = 15
correct_page_sizes = [5, 10, 15]
incorrect_page_sizes = [4, 6, 9, 11, "str", 14, 16]
params = {
    'by_substring': 'q=',
    'by_country_code': 'country_code=',
    'by_page': 'page=',
    'by_page_size': 'page_size='
}
params_default_values = {
    'by_substring': 'рск',
    'by_country_code': 'kz',
    'by_page': 2,
    'by_page_size': 5
}


def get_url_pattern(parameters_count: int = 0) -> str:
    return '{}' if parameters_count < 1 else '{}?{}{}' + '&{}{}' * (parameters_count - 1)


def get_regions() -> list:
    total = []
    total_id = set()
    page_number = min_page_number
    while True:
        regions = get_by_params(params['by_page'], page_number)
        if not regions:
            break
        for region in regions:
            region_id = region['id']
            if region_id not in total_id:
                total_id.add(region_id)
                total.append(region)
        page_number += 1
    return total


def get_total() -> int:
    return len(get_regions())


def get_response_body(*args, url: str = base_url) -> dict:
    """
    :param args: pairs param_type: str, param_value: str or int
    """
    url_pattern = get_url_pattern(len(args) // 2)

    try:
        return json.loads(
            request.urlopen(url_pattern.format(url, *args)).read().encode('utf-8')
        )
    except AttributeError:
        return json.loads(
            request.urlopen(url_pattern.format(url, *args)).read()
        )


def get_by_params(*args, correct=True,) -> list or dict:
    """
        :param args: pairs param_type: str, param_value: str or int
        :param correct: False if pass incorrect params
    """
    assert len(args) % 2 == 0

    return get_response_body(*args)['items'] if correct else get_response_body(*args)


def get_country_codes(countries: list) -> set:
    return set(map(lambda x: x['country']['code'], countries))


def get_page_count(page_size: int, total: int) -> int:
    return math.ceil(total / page_size)


def get_last_page_size(page_count: int, total: int) -> int:
    return total % page_count


def get_encoded_ascii(string: str) -> str:
    r = requests.get(base_url, params={f'{params["by_substring"]}': string})
    return r.url[r.url.find('=') + 1:]


if __name__ == '__main__':
    pass
