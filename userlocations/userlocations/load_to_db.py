#!/usr/bin/env python
import os
import csv
import sys

from locations.models import County, Ward, Location

county_data = open(os.path.join(os.path.dirname(__file__), 'data', 'userdata_county.csv'))
ward_data = open(os.path.join(os.path.dirname(__file__), 'data', 'userdata_ward.csv'))
location_data = open(os.path.join(os.path.dirname(__file__), 'data', 'userdata_location.csv'))

def load_counties():
    with county_data:
        reader = csv.DictReader(county_data, fieldnames=['num', 'name'])
        for row in reader:
            county = County(name=row['name'],
                            num=row['num'])
            county.save()

def load_wards():
    with ward_data:
        reader = csv.DictReader(ward_data, fieldnames=['num', 'name', 'countynum'])
        for row in reader:
            ward = Ward(name=row['name'],
                        num=row['num'])
            try:
                ward.county = County.objects.get(num=row['countynum'])
            except:
                pass
            else:
                ward.save()

def load_locations():
    with location_data:
        reader = csv.DictReader(location_data, fieldnames=['num', 'name', 'wardnum', 'countynum', 'lat', 'lon'])
        for row in reader:
            location = Location(name=row['name'],
                                num=row['num'],
                                lat=row['lat'],
                                lon=row['lon'])
            try:
                location.ward = Ward.objects.get(num=row['wardnum'])
            except:
                pass
            else:
                location.save()
            
