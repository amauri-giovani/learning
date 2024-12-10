from zeep import Client
from zeep import xsd

wsdl = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"
client = Client(wsdl)

with client.settings(raw_response=True):
    response = client.service.NumberToDollars(dNum=10)

    # response is now a regular requests.Response object
    assert response.status_code == 200
    assert response.content

print(response.content)