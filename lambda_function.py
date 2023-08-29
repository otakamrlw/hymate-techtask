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

# the coordinate of hymate's office
latitude = "48.1558031"
longitude = "11.5290436"

url = "https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,snow_depth,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,direct_radiation,diffuse_radiation&past_days=2&forecast_days=1" % (latitude, longitude)
response = requests.get(url)
data_json = response.json()

s3 = boto3.resource('s3')

BUCKET_NAME = "hymate-weather-bucket"

today = date.today()
print("today's date: ", today)

def lambda_handler(event, context):
    print(data_json)
    
    request_id = context.aws_request_id

    bucket = s3.Bucket(BUCKET_NAME)
    object_key_name = f"{request_id}.json"

    # オブジェクトを生成
    obj = bucket.Object(object_key_name)

    # 対象のバケットにjsonデータをアップロード
    json_data = event
    r = obj.put(Body = json.dumps(json_data))

    return {
        'request_id': request_id,
        'statusCode': 200,
    }
