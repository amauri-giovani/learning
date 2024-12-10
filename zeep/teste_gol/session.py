from zeep import Client


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
        self.security = security
        self.header = header
        self.pseudo_city_code = pseudo_city_code

    def create(self):
        try:
            client = Client(URLsWSDL['session_create'])

            self.response = client.service.SessionCreateRQ(
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

            if self.response.body.status == "Approved":
                print(f"\nSessão criada com sucesso\n"
                      f"BinarySecurityToken: {self.response.header.Security.BinarySecurityToken}")
                return self.response.header.Security.BinarySecurityToken
        except:
            print("Problemas na criação da sessão!!!")

    def close(self):
        # try:
        client = Client(URLsWSDL['session_close'])

        response = client.service.SessionCloseRQ(
            POS={
                "Source": {
                    "PseudoCityCode": self.pseudo_city_code
                }
            },
            _soapheaders={
                "Security": {
                    "BinarySecurityToken": str(self.response.header.Security.BinarySecurityToken),
                    # "SabreAth": "",
                    # "UsernameToken": {
                    #     "Username": "0470",
                    #     "Password": "B2BGWS21",
                    #     "Organization": "AAP",
                    #     "Domain": "G3",
                    # }
                },
                "MessageHeader": {
                    "From": {"PartyId": 'WebServiceClient'},
                    "To": {"PartyId": 'WebServiceSupplier'},
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

        print(f"\nSessão fechada com sucesso\n"
              f"BinarySecurityToken: {response.header.Security.BinarySecurityToken}")


s = SessionGol(security, header, pseudo_city_code)
s.create()
s.close()
