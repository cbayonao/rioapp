import json
import mechanicalsoup
import lxml

def lambda_handler(event, context):
    browser = mechanicalsoup.StatefulBrowser()
    url = 'http://entidadesintegradas.co/Registro/faces/Index?60N5MP1O=1'
    entint = browser.open(url=url)
    # print('{}'.format(type(browser)))


    body = {
        "message": f'{ entint }',
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
