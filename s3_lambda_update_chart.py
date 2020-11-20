import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'scb-aws-transactions'
    key = 'bennyCharts.json'
    s3Obj = s3.get_object(Bucket=bucket, Key=key)
    content = s3Obj['Body']  # get content from response body
    jsonObj = json.loads(content.read())  # from response body, parse json into py object
    # charts = jsonObject['charts']  # extract value of transactions key

    # test: create new chart entry
    file = "testing.csv"
    field = "apifield"
    chart = "column"
    series = [9,8,7,6,5,4,3,2,1]
    nuChart = {}
    nuChart['filename'] = file
    nuChart['fieldname'] = field
    nuChart['chartType'] = chart
    nuChart['seriesData'] = series

    # update the jsonObj
    jsonObj.append(nuChart)

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=str(json.dumps(jsonObj))
    )
