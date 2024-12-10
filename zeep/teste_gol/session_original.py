from zeep import Client
from zeep.transports import Transport
from zeep.wsse import BinarySignature
from requests import Session
from requests.auth import HTTPBasicAuth, AuthBase


# BinarySignature()

security = {
    "UsernameToken": {
        "Username": "0470",
        "Password": "B2BGWS21",
        "Organization": "AAP",
        "Domain": "G3"}
}

header = {
    "From": {"PartyId": {}},
    "To": {"PartyId": {}},
    "CPAId": "G3",
    "ConversationId": "ECOMPONENT",
    "Service": "SessionCreateRQ",
    "Action": "SessionCreateRQ",
    "MessageData": {
        "MessageId": "teste@e-component.com",
        "Timestamp": "2020-01-01T00:00:00Z"
    }
}

pseudo_city_code = "HDQ"


def get_value_in_dict(security, key):
    value = None
    for k in security.keys():
        value = security[k].get(key)
    return value


URLsWSDL = {
    "session_create": "http://hom-gws.voegol.com.br/GWS/SessionCreateRQService.svc?wsdl",
    "session_close": "http://hom-gws.voegol.com.br/GWS/SessionCloseRQService.svc?wsdl",
}


class SessionGol:
    def __init__(self, security, header, pseudo_city_code):
        # self.username = get_value_in_dict(security, 'Username')
        # self.password = get_value_in_dict(security, 'Password')
        # self.organization = get_value_in_dict(security, 'Organization')
        # self.domain = get_value_in_dict(security, 'Domain')
        self.security = security
        self.header = header
        self.pseudo_city_code = pseudo_city_code

        # self.session = Session()
        # self.session.auth = HTTPBasicAuth(self.username, self.password)

    def create(self):
        try:
            client = Client(URLsWSDL['session_create'])

            self.response_create = client.service.SessionCreateRQ(
                POS={
                    "Source": {
                        "PseudoCityCode": self.pseudo_city_code
                    }
                },
                _soapheaders={
                    "Security": self.security,
                    "MessageHeader": {
                        "From": {"PartyId": {}},
                        "To": {"PartyId": {}},
                        "CPAId": "G3",
                        "ConversationId": "ECOMPONENT",
                        "Service": "SessionCreateRQ",
                        "Action": "SessionCreateRQ",
                        "MessageData": {
                            "MessageId": "teste@e-component.com",
                            "Timestamp": "2020-01-01T00:00:00Z"
                        }
                    }
                }
            )

            if self.response_create.body.status == "Approved":
                print(f"\nSessão criada com sucesso\n"
                      f"BinarySecurityToken: {self.response_create.header.Security.BinarySecurityToken}")
                return self.response_create.header.Security.BinarySecurityToken
        except:
            print("Problemas na criação da sessão!!!")

    def close(self):
        # try:
        client = Client(URLsWSDL['session_close'])

        self.response_close = client.service.SessionCloseRQ(
            POS={
                "Source": {
                    "PseudoCityCode": self.pseudo_city_code
                }
            },
            _soapheaders={
                "Security": {
                    "BinarySecurityToken": str(self.response_close.header.Security.BinarySecurityToken),
                    # "UsernameToken": {
                    #     "Username": "0470",
                    #     "Password": "B2BGWS21",
                    #     "Organization": "AAP",
                    #     "Domain": "G3",
                    # }
                },
                "MessageHeader": {
                    "From": {"PartyId": {'WebServiceClient'}},
                    "To": {"PartyId": {'WebServiceSupplier'}},
                    "CPAId": "G3",
                    "ConversationId": "ECOMPONENT",
                    "Service": "SessionCloseRQ",
                    "Action": "SessionCloseRQ",
                    "MessageData": {
                        "MessageId": "ecomponent@ecomponent.com",
                        "Timestamp": "2020-05-13T20:42:06"
                    }
                }
            }
        )

        # if response.body.status == "Approved":
        print(f"\nSessão fechada com sucesso\n"
              f"BinarySecurityToken: {self.response_close.header.Security.BinarySecurityToken}")
        # return self.response_close.header.Security.BinarySecurityToken
        # except:
        #     print("Problemas para fechar a sessão!!!")


s = SessionGol(security, header, pseudo_city_code)
s.create()
s.close()

"""Security(
    UsernameToken: {
    Username: xsd:string,
    Password: xsd:string,
    NewPassword: xsd:string[],
    Organization: xsd:string,
    Domain: xsd:string
},
    SabreAth: xsd:string,
    BinarySecurityToken: xsd:string
)
"""