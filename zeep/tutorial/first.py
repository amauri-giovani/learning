from zeep import Client
from zeep import xsd

# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
wsdl = "http://service.e-component.com/GWSSeparado/SessionCreateRQService.svc?wsdl"
client = Client(wsdl)

with client.settings(raw_response=True):
    response = client.service.Method1('Zeep', 'is cool')

    # response is now a regular requests.Response object
    assert response.status_code == 200
    assert response.content

    print(response.status_code)
    print(response.content)