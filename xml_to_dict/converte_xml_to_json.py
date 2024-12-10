import json
import xmltodict


xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:mes="http://www.ebxml.org/namespaces/messageHeader" xmlns:sec="http://schemas.xmlsoap.org/ws/2002/12/secext" xmlns:ns="http://webservices.sabre.com/sabreXML/2011/10">
   <soapenv:Header>
      <mes:MessageHeader mes:id="" mes:version="">
         <!--Optional:-->
         <mes:From>
            <!--Zero or more repetitions:-->
            <mes:PartyId mes:type=""></mes:PartyId>
            <!--Optional:-->
            <mes:Role></mes:Role>
         </mes:From>
         <!--Optional:-->
         <mes:To>
            <!--Zero or more repetitions:-->
            <mes:PartyId mes:type=""></mes:PartyId>
            <!--Optional:-->
            <mes:Role></mes:Role>
         </mes:To>
         <!--Optional:-->
         <mes:CPAId></mes:CPAId>
         <!--Optional:-->
         <mes:ConversationId></mes:ConversationId>
         <!--Optional:-->
         <mes:Service mes:type=""></mes:Service>
         <!--Optional:-->
         <mes:Action></mes:Action>
         <!--Optional:-->
         <mes:MessageData>
            <!--Optional:-->
            <mes:MessageId></mes:MessageId>
            <!--Optional:-->
            <mes:Timestamp></mes:Timestamp>
            <!--Optional:-->
            <mes:RefToMessageId></mes:RefToMessageId>
            <!--Optional:-->
            <mes:TimeToLive></mes:TimeToLive>
            <!--Optional:-->
            <mes:Timeout></mes:Timeout>
         </mes:MessageData>
         <!--Optional:-->
         <mes:DuplicateElimination></mes:DuplicateElimination>
         <!--Zero or more repetitions:-->
         <mes:Description xml:lang=""></mes:Description>
         <!--You may enter ANY elements at this point-->
      </mes:MessageHeader>
      <sec:Security>
         <!--Optional:-->
         <sec:UsernameToken>
            <!--Optional:-->
            <sec:Username></sec:Username>
            <!--Optional:-->
            <sec:Password></sec:Password>
            <!--Zero or more repetitions:-->
            <sec:NewPassword></sec:NewPassword>
            <!--Optional:-->
            <Organization></Organization>
            <!--Optional:-->
            <Domain></Domain>
         </sec:UsernameToken>
         <!--Optional:-->
         <sec:SabreAth></sec:SabreAth>
         <!--Optional:-->
         <sec:BinarySecurityToken></sec:BinarySecurityToken>
      </sec:Security>
   </soapenv:Header>
   <soapenv:Body>
      <ns:SpecialServiceRQ ReturnHostCommand="" TimeStamp="" Version="">
         <!--Optional:-->
         <ns:SpecialServiceInfo>
            <!--Zero or more repetitions:-->
            <ns:AdvancePassenger SegmentNumber="">
               <!--Optional:-->
               <ns:Document ExpirationDate="" Number="" Type="">
                  <!--Optional:-->
                  <ns:IssueCountry></ns:IssueCountry>
                  <!--Optional:-->
                  <ns:NationalityCountry></ns:NationalityCountry>
                  <!--Optional:-->
                  <ns:Visa IssueDate="">
                     <!--Optional:-->
                     <ns:ApplicableCountry></ns:ApplicableCountry>
                     <!--Optional:-->
                     <ns:PlaceOfBirth></ns:PlaceOfBirth>
                     <!--Optional:-->
                     <ns:PlaceOfIssue></ns:PlaceOfIssue>
                  </ns:Visa>
               </ns:Document>
               <!--Optional:-->
               <ns:PersonName DateOfBirth="" DocumentHolder="" Gender="" LapChild="" NameNumber="">
                  <!--Optional:-->
                  <ns:GivenName></ns:GivenName>
                  <!--Optional:-->
                  <ns:MiddleName></ns:MiddleName>
                  <!--Optional:-->
                  <ns:Surname></ns:Surname>
               </ns:PersonName>
               <!--Optional:-->
               <ns:ResidentDestinationAddress Type="">
                  <!--Optional:-->
                  <ns:City></ns:City>
                  <!--Optional:-->
                  <ns:Country></ns:Country>
                  <!--Optional:-->
                  <ns:Street></ns:Street>
                  <!--Optional:-->
                  <ns:State></ns:State>
                  <!--Optional:-->
                  <ns:Zip></ns:Zip>
               </ns:ResidentDestinationAddress>
               <!--Optional:-->
               <ns:VendorPrefs>
                  <!--Optional:-->
                  <ns:Airline Hosted=""/>
               </ns:VendorPrefs>
            </ns:AdvancePassenger>
            <!--Zero or more repetitions:-->
            <ns:SecureFlight SegmentNumber="">
               <!--Optional:-->
               <ns:IssueCountry></ns:IssueCountry>
               <!--Optional:-->
               <ns:KnownTravelerNumber></ns:KnownTravelerNumber>
               <!--Optional:-->
               <ns:PersonName DateOfBirth="" Gender="" NameNumber="">
                  <!--Optional:-->
                  <ns:GivenName></ns:GivenName>
                  <!--Optional:-->
                  <ns:Surname></ns:Surname>
               </ns:PersonName>
               <!--Optional:-->
               <ns:RedressNumber></ns:RedressNumber>
               <!--Optional:-->
               <ns:VendorPrefs>
                  <!--Optional:-->
                  <ns:Airline Hosted=""/>
               </ns:VendorPrefs>
            </ns:SecureFlight>
            <!--Zero or more repetitions:-->
            <ns:Service SegmentNumber="" SSR_Code="">
               <!--Optional:-->
               <ns:PersonName NameNumber=""/>
               <!--Optional:-->
               <ns:Text></ns:Text>
               <!--Optional:-->
               <ns:VendorPrefs>
                  <!--Optional:-->
                  <ns:Airline Code="" Hosted=""/>
               </ns:VendorPrefs>
            </ns:Service>
         </ns:SpecialServiceInfo>
      </ns:SpecialServiceRQ>
   </soapenv:Body>
</soapenv:Envelope>
"""

# xml_parse = xmltodict.parse(xml)
# with open('/home/amauri/Downloads/PS195.xml', encoding='ISO-8859-1') as f:
#     xml = f.read()
json_converted = json.dumps(xmltodict.parse(xml), indent=4)
dict_converted = json.loads(json_converted)

# print(xml_parse)
# print(type(xml_parse))
# print(json_converted)
# print(type(json_converted))
print(dict_converted)
# print(type(dict_converted))

