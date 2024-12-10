from zeep import Client, Transport


wsdl = "http://hom-gws.voegol.com.br/GWS/SessionCreateRQService.svc?wsdl"
# session = Session()
# session.auth = HTTPBasicAuth("0470", "B2BGWS21")
# client = Client(wsdl, transport=Transport(session=session))
client = Client(wsdl)

# element = client.get_element("ns2:Security")

# element = client.service.SessionCreateRQ(
#     UsernameToken={"Username": "0470", "Password": "B2BGWS21", "Organization": "AAP", "Domain": "G3"},
#     From={"PartyId": {}}, To={"PartyId": {}}, CPAId="G3", ConversationId="ECOMPONENT", Service="SessionCreateRQ",
#     Action="SessionCreateRQ", MessageData={"MessageId": "teste@e-component.com", "Timestamp": "2020-01-01T00:00:00Z"},
#     POS={"Source": {"PseudoCityCode": "HDQ"}}
# )
# print(element)


security = client.get_element("ns2:Security")
obj1 = security(
    UsernameToken={"Username": "0470", "Password": "B2BGWS21", "Organization": "AAP", "Domain": "G3"}
)
# print(obj1)

message_header = client.get_element("ns3:MessageHeader")
obj2 = message_header(
    From={"PartyId": {}}, To={"PartyId": {}}, CPAId="G3", ConversationId="ECOMPONENT", Service="SessionCreateRQ",
    Action="SessionCreateRQ", MessageData={"MessageId": "teste@e-component.com", "Timestamp": "2020-01-01T00:00:00Z"}
)
# print(obj2)

# session_create_rq = client.get_element("ns1:SessionCreateRQ")
# obj3 = session_create_rq(
#     POS={"Source": {"PseudoCityCode": "HDQ"}}
# )
# print(obj3)

response = client.service.SessionCreateRQ(
    POS={"Source": {"PseudoCityCode": "HDQ"}},
    _soapheaders={"Security": obj1, "MessageHeader": obj2}
)

# print("=" * 50, "\n")
# print(response)

# SessionCreateRQ(POS: {Source: {PseudoCityCode: xsd:string}}, returnContextID: xsd:boolean,
# _soapheaders={Security: ns2:Security, MessageHeader: ns3:MessageHeader})
#
# -> header: {Security: ns2:Security, MessageHeader: ns3:MessageHeader},
# body: {Success: {}, Warnings: {Warning: {Language: xsd:string, ShortText: xsd:string, Type: xsd:string,
# Code: xsd:string, DocURL: xsd:anyURI, Status: xsd:string, Tag: xsd:string, RecordId: xsd:string}},
# ConversationId: xsd:string, Errors: {Error: {ErrorInfo: {Message: xsd:string}, ErrorCode: xsd:string,
# Severity: xsd:string, ErrorMessage: xsd:string}}, EchoToken: xsd:string, TimeStamp: xsd:string,
# Target: ns1:Target, version: xsd:string, SequenceNmbr: xsd:nonNegativeInteger, PrimaryLangID: xsd:language,
# AltLangID: xsd:language, status: xsd:string}


# element = client.get_element('ns1:SessionCreateRQ')
# obj = element(_value_1={'item_1_a': 'foo', 'item_1_b': 'bar'})

# with client.settings(raw_response=True):
#     response = client.service.SessionCreateRQ(
#         # obj1,
#         # obj2,
#         obj3
#
#     )

# response is now a regular requests.Response object
# assert response.status_code == 200
# assert response.content

# print(response.status_code)
# print(response.content)

params = {
    "CPAId": "G3",
    "ConversationId": "ECOMPONENT",
    "Service": "SessionCreateRQ",
    "Action": "SessionCreateRQ",
    "MessageId": "teste@e-component.com",
    "Timestamp": "2020-01-01T00:00:00Z",
    "Username": "0470",
    "Password": "B2BGWS21",
    "Organization": "AAP",
    "Domain": "G3"
}
# ns2:Security(UsernameToken: {Username: xsd:string, Password: xsd:string, NewPassword: xsd:string[], Organization: xsd:string, Domain: xsd:string}, SabreAth: xsd:string, BinarySecurityToken: xsd:string)

"""with client.settings(raw_response=True):
    # response = client.service.SessionCreateRQ(**params)
    response = client.service.SessionCreateRQ(
        # POS={"Source": {"PseudoCityCode": "HDQ"}},
        # returnContextID="true",
        # _soapheaders={
        #     Security: ns2:Security,
        #     MessageHeader: ns3:MessageHeader}
    )

    # response is now a regular requests.Response object
    assert response.status_code == 200
    assert response.content

print(response.content)"""
