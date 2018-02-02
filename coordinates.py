#!/usr/bin/env python

import json
from random import uniform

countries_json = json.load(open('countries.geo.json'))

countries_data = countries_json['features']


def list_available_countries(data):
    return map(lambda country: country['id'], data)


def get_selected_country_data(data, country):
    return next(x for x in data if x['id'] == country)


def get_random_coordinates_within_bounds(bounds):
    x_coords = map(lambda bound: bound[0], bounds[0])
    y_coords = map(lambda bound: bound[1], bounds[0])

    max_x = max(x_coords)
    min_x = min(x_coords)

    max_y = max(y_coords)
    min_y = min(y_coords)

    print(min_x, max_x)
    print(min_y, max_y)

    latitude = uniform(min_y, max_y)
    longitude = uniform(min_x, max_x)

    print(latitude, longitude)
    return latitude, longitude


IRL_data = get_selected_country_data(countries_data, "DEU")
IRL_bounds = IRL_data['geometry']['coordinates']
get_random_coordinates_within_bounds(IRL_bounds)
