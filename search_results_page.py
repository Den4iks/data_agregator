def get_count_of_cars(soup):
    return soup.find(class_='js-results-count')


def get_count_of_pages(soup):
    html_result = soup.find(class_='paginationMini__count')
    return html_result.getText().split(' ')[3]


def get_all_search_results(soup):
    html_results = soup.find_all(class_='search-page__result')
    return html_results


def get_link_for_specific_car(soup):
    link_url = soup.find(class_='listing-fpa-link')['href']
    return link_url


def get_thumbnail_for_specific_car(soup):
    thumbnail = soup.find('img')['src']
    return thumbnail


def get_title_name_for_specific_car(soup):
    title = soup.find(class_='listing-title title-wrap').getText()
    return title


def get_description_for_specific_car(soup):
    description = soup.find(class_='listing-description')
    return description


def get_key_spec_for_specific_car(soup):
    specs = soup.find(class_='listing-key-specs').find_all('li')
    spec_dict = {
        'year': specs[0].getText(),
        'body_type': specs[1].getText(),
        'milliage': specs[2].getText(),
        'transmission': specs[3].getText(),
        'engine_size': specs[4].getText(),
        'power_bhp': specs[5].getText(),
        'fuel_type': specs[6].getText(),
    }
    return spec_dict


def get_price_for_specific_car(soup):
    price = soup.find(class_='vehicle-price').getText()
    return price


