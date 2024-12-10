from zeep import Client
from zeep import xsd

# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
wsdl = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

client = Client(wsdl)
element = client.get_element("ns0:NumberToDollars")
obj = element(dNum=10)
print(obj)
# with client.settings(raw_response=True):
#     response = client.service.Method1('Zeep', 'is cool')
#
#     # response is now a regular requests.Response object
#     assert response.status_code == 200
#     assert response.content
#
#     print(response.status_code)
#     print(response.content)