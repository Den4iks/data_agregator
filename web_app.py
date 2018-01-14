from flask import Flask, Response, render_template, request
import pygal
import search_results_page
from car import Car
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import requests

url = 'https://www.autotrader.co.uk/car-search?sort=sponsored&radius=1500&postcode=se137fl&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&make=SEAT&model=LEON&price-to=4000&year-from=2009'

flask_app = Flask(__name__)


def get_data():
    rsp = requests.get(url)
    search_result_html = rsp.text
    soup = BeautifulSoup(search_result_html, 'html.parser')
    return soup


def generate_car_objects(html_cars):
    car_objects_list = []
    for html_car in html_cars:
        price = search_results_page.get_price_for_specific_car(html_car)
        advert_name = search_results_page.get_title_name_for_specific_car(html_car)
        description = search_results_page.get_description_for_specific_car(html_car)
        specs = search_results_page.get_key_spec_for_specific_car(html_car)
        link = search_results_page.get_link_for_specific_car(html_car)
        thumbnail = search_results_page
        car_objects_list.append(Car(price, advert_name, description, specs.get('milliage'), specs.get('year'),
                                    specs.get('engine_size'), specs.get('transmission'), specs.get('fuel_type'),
                                    thumbnail, link))
    return car_objects_list


def make_chart(cars):
    line_chart = pygal.Line(height=450,
                            width=1200,
                            show_y_guides=False,
                            show_x_guides=False,
                            y_title='Front requests/day',
                            legend_at_bottom=True)
    line_chart.x_label_rotation = 20
    line_chart.x_labels = get_milliage(cars)
    line_chart.y_title = 'Car price/year'
    for car in cars:
        line_chart.add(car.advert_name, get_prices(cars), dots_size=1)

    return line_chart


def get_price_in_decimal(price):
    return Decimal(sub(r'[^\d.]', '', price))



def get_milliage(cars):
    milliages = []
    for car in cars:
        milliages.append(car.milliage)

    return milliages


def get_prices(cars):
    prices = []
    for car in cars:
        prices.append(get_price_in_decimal(car.price))

    return prices

@flask_app.route('/charts')
def usage():

    return render_template('charts.html',
                           page='charts')


@flask_app.route('/chart/cars.svg')
def chart():
    soup = get_data()
    hrml_cars = search_results_page.get_all_search_results(soup)
    cars = generate_car_objects(hrml_cars)
    return make_chart(cars).render_response()


def server():
    flask_app.run(host='0.0.0.0', port=3333)
