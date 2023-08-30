#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:43:53 2023

@author: takayuki
"""

import json
import boto3
import requests
from datetime import date

print("Libraries import done.")


# the coordinate of hymate's office
latitude = "48.1558031"
longitude = "11.5290436"

# call API from Open-Meteo to get weatehr forecast
url = "https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,snow_depth,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,direct_radiation,diffuse_radiation&past_days=2&forecast_days=1" % (
    latitude, longitude)
response = requests.get(url)
data_json = response.json()

# choose which bucket you want to use
BUCKET_NAME = "hymate-weather-bucket"
s3 = boto3.resource('s3')


def lambda_handler(event, context):

    # get request ID
    request_id = context.aws_request_id

    # declare file name based on today's date
    today = date.today()
    file_name = f"{today}.json"

    bucket = s3.Bucket(BUCKET_NAME)
    obj = bucket.Object(file_name)

    # upload json to the bucket
    r = obj.put(Body=json.dumps(data_json))

    return {
        'request_id': request_id,
        'statusCode': 200,
    }
