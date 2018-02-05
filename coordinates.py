#!/usr/bin/env python

import json
from random import uniform


def load_countries_data():
    return json.load(open('countries.geo.json'))['features']


def list_available_countries(data):
    return map(lambda country: country['id'], data)


def get_country_polygon(data, country):
    polygon = next(x for x in data if x['id'] == country)['geometry']['coordinates']

    # Return the Polygon
    if len(polygon) == 1:
        return next(x for x in data if x['id'] == country)['geometry']['coordinates']

    # Return the largest Polygon in a MultiPolygon
    return max(next(x for x in data if x['id'] == country)['geometry']['coordinates'], key=len)


def get_random_point_within_polygon(polygon):
    x_points = map(lambda bound: bound[0], polygon[0])
    y_points = map(lambda bound: bound[1], polygon[0])

    min_x = min(x_points)
    max_x = max(x_points)

    min_y = min(y_points)
    max_y = max(y_points)

    random_point = uniform(min_x, max_x), uniform(min_y, max_y)

    return random_point


# TODO: Accept country input in alpha_2 or alpha_3 ISO code (use pycountry)
def get_random_point_within_country(data, country):

    country_polygon = get_country_polygon(data, country)

    return get_random_point_within_polygon(country_polygon)
