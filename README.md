# hymate-techtask

# 1. API call with AWS cloud
## Task
The task below is to be performed in a serverless mindset. Everything can and has to be done using AWS Cloud resources. The resources itself don’t have to be implemented on AWS, but the code has to be written as if it was. The candidate must indicate what services are needed in each step and explain why the chosen service is the best choice. The code has to be usable in the pointed services without changes.

Using an Open-Meteo API method, design a code that is capable of making requests on a fixed interval, and saving the responses. The request has to get 3 days of hourly forecast every day starting from two days before (today-2), and store the data for later fast access and usage. You may perform any data transformations you see fit, provided you explain the reason.
The API documentation can be found at: https://open-meteo.com/

Information required: Temperature, Relative humidity, Rain, Snowfall, Snow Depth, Cloudcover, Direct Solar Radiation, Diffuse Solar Radiation

## Solution
To implement an API call in a server-less setup, I used AWS Lambda, Amazon S3 bucket, and EventBridge with cron.
lamda_function.py is deployed on AWL Lambda, which is connected to S3 bucket to store the response of Open-Meteo API calls in JSON format.
I assume that we need weather forecast data every morning. Therefore, I configured EventBridge with crom so that the lamda_function.py is executed at 8 am every day and the result is stored in S3 bucket with today's date as the file name e.g. 2023-08-29.json.
The resource is implemented in my AWS account and we can discuss more details when we meet.

# Usage

