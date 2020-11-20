import json
import boto3

s3 = boto3.client('s3')

print('Loading function...')

def lambda_handler(event, context):
    # 1. parse the query string parameters into a new chart object
    newChartObj = {}
    newChartObj['filename'] = event['queryStringParameters']['file']
    newChartObj['fieldname'] = event['queryStringParameters']['field']
    newChartObj['chartType'] = event['queryStringParameters']['chart']
    newChartObj['seriesData'] = event['queryStringParameters']['series']

    # 2. get a json object of chart-data from json file in s3
    bucket = 'scb-aws-transactions'
    key = 'bennyCharts.json'
    s3Obj = s3.get_object(Bucket=bucket, Key=key)
    content = s3Obj['Body']  # get content from response body
    jsonObj = json.loads(content.read())  # from response body, parse json into py object

    #3. update the jsonObj with the newChartObj and put it back in s3
    jsonObj.append(newChartObj)

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=str(json.dumps(jsonObj))
    )

    # 4. construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(newChartObj)

    # 4. return http response object
    return responseObject
