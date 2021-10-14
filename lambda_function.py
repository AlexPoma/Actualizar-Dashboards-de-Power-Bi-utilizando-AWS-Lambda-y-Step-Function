import json
import requests

def lambda_handler(event, context):

    json_pbi = {
        "WorkSpace": f"{event['WorkSpace']}",
        "GroupId": f"{event['GroupId']}",
        "DashBoard": f"{event['DashBoard']}",
        "DatasetId": f"{event['DatasetId']}"
    }
    
    print(json_pbi)
    
    api_url = "Replace with your HTTP URL"
    response = requests.post(api_url, json = json_pbi)
    print('Response: ' + str(response))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }