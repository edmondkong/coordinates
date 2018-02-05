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


def inside_polygon(x, y, points):
    """
    Return True if a coordinate (x, y) is inside a polygon defined by
    a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].

    Reference: http://www.ariel.com.au/a/python-point-int-poly.html
    """
    points = points[0]
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


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

    point = tuple
    valid_point = False

    while not valid_point:
        point = get_random_point_within_polygon(country_polygon)

        if inside_polygon(point[0], point[1], country_polygon):
            valid_point = True

    return point

print(get_random_point_within_country(load_countries_data(), 'CHN'))
