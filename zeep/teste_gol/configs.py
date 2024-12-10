security = {
    "UsernameToken": {
        "Username": "0470",
        "Password": "B2BGWS21",
        "Organization": "AAP",
        "Domain": "G3"}
}

header_create = {
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

header_close = {
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

pseudo_city_code = "HDQ"
