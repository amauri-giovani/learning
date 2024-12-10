import zeep
from zeep import Client, Settings
from zeep import xsd


"""
SessionCreateRQ(POS: {Source: {PseudoCityCode: xsd:string}},
returnContextID: xsd:boolean,
_soapheaders={Security: ns2:Security,
MessageHeader: ns3:MessageHeader}) -> header: {Security: ns2:Security,
MessageHeader: ns3:MessageHeader},
body: {Success: {},
Warnings: {Warning: {Language: xsd:string,
ShortText: xsd:string,
Type: xsd:string,
Code: xsd:string,
DocURL: xsd:anyURI,
Status: xsd:string,
Tag: xsd:string,
RecordId: xsd:string}},
ConversationId: xsd:string,
Errors: {Error: {ErrorInfo: {Message: xsd:string},
ErrorCode: xsd:string,
Severity: xsd:string,
ErrorMessage: xsd:string}},
EchoToken: xsd:string,
TimeStamp: xsd:string,
Target: ns1:Target,
version: xsd:string,
SequenceNmbr: xsd:nonNegativeInteger,
PrimaryLangID: xsd:language,
AltLangID: xsd:language,
status: xsd:string}
"""

wsdl = "http://hom-gws.voegol.com.br/GWS/SessionCreateRQService.svc?wsdl"
# client = Client(wsdl=wsdl)

settings = Settings(strict=False, xml_huge_tree=True)
client = Client(wsdl=wsdl, settings=settings)
# client = Client(wsdl)
# client.service.SessionCreateRQ()
# client.service['SessionCreateRQ']()

# with client.settings(raw_response=True):
#     response = client.service.SessionCreateRQ(
#         "SessionCreateRQ",
#         "ECOMPONENT",
#     )
#
# print(response.content)




"""
<zeep.proxy.OperationProxy object>
    SessionCreateRQ(POS: {Source: {PseudoCityCode: xsd:string}},
returnContextID: xsd:boolean,
_soapheaders={Security: ns2:Security,
MessageHeader: ns3:MessageHeader}) -> header: {Security: ns2:Security,
MessageHeader: ns3:MessageHeader},
body: {Success: {},
Warnings: {Warning: {Language: xsd:string,
ShortText: xsd:string,
Type: xsd:string,
Code: xsd:string,
DocURL: xsd:anyURI,
Status: xsd:string,
Tag: xsd:string,
RecordId: xsd:string}},
ConversationId: xsd:string,
Errors: {Error: {ErrorInfo: {Message: xsd:string},
ErrorCode: xsd:string,
Severity: xsd:string,
ErrorMessage: xsd:string}},
EchoToken: xsd:string,
TimeStamp: xsd:string,
Target: ns1:Target,
version: xsd:string,
SequenceNmbr: xsd:nonNegativeInteger,
PrimaryLangID: xsd:language,
AltLangID: xsd:language,
status: xsd:string}
"""
