#!/usr/bin/env python

import json
from random import uniform
from geojson import Point


def load_countries_data():
    return json.load(open('countries.geo.json'))['features']


def list_available_countries(data):
    return map(lambda country: country['id'], data)


def get_country_polygon(data, country):
    return next(x for x in data if x['id'] == country)['geometry']['coordinates']


def get_random_point_within_polygon(polygon):
    x_points = map(lambda bound: bound[0], polygon[0])
    y_points = map(lambda bound: bound[1], polygon[0])

    min_x = min(x_points)
    max_x = max(x_points)

    min_y = min(y_points)
    max_y = max(y_points)

    random_point = Point(uniform(min_x, max_x), uniform(min_y, max_y))

    return random_point

