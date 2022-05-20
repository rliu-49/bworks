#!/usr/local/bin/python3

import xml.etree.ElementTree as ET
# import sys
import re

x = '''<?xml version="1.0" encoding="UTF-8"?>
<xsi:Event xmlns:xsi="http://schema.broadsoft.com/xsi" xmlns:xsi1="http://www.w3.org/2001/XMLSchema-instance" xsi1:type="xsi:SubscriptionEvent">
	<xsi:eventID>4c5542e5-3d6d-47d6-afcf-203adba158c5</xsi:eventID>
	<xsi:sequenceNumber>5</xsi:sequenceNumber>
	<xsi:clientId>bwcticlient.webex.com</xsi:clientId>
	<xsi:externalApplicationId>appId</xsi:externalApplicationId>
	<xsi:subscriptionId>99ee035c-9c41-4ba4-b9cd-6d6c956be44b</xsi:subscriptionId>
	<xsi:channelId>2390c868-c1b7-46b1-b943-b5e9e275901a</xsi:channelId>
	<xsi:targetId>TAC_Public1@ucaas.cisco.com</xsi:targetId>
	<xsi:eventData xsi1:type="xsi:CallHistoryEvent">
		<xsi:call>
			<xsi:callId>callhalf-227509:0</xsi:callId>
			<xsi:extTrackingId>295313b0-ab3b-416e-884b-7faaa8dbc4ee</xsi:extTrackingId>
			<xsi:networkCallId>1-118515@192.168.40.34</xsi:networkCallId>
			<xsi:personality>Terminator</xsi:personality>
			<xsi:state>Released</xsi:state>
			<xsi:releasingParty>localRelease</xsi:releasingParty>
			<xsi:remoteParty>
				<xsi:name>sipp</xsi:name>
				<xsi:address>sip:sipp@192.168.40.34:5061</xsi:address>
				<xsi:callType>Network</xsi:callType>
			</xsi:remoteParty>
			<xsi:startTime>1625225670467</xsi:startTime>
			<xsi:answerTime>1625225785968</xsi:answerTime>
			<xsi:releaseTime>1625225818008</xsi:releaseTime>
			<xsi:securityClassification>Unclassifiimport reee</xsi:securityClassification>
		</xsi:call>
	</xsi:eventData>
</xsi:Event>
'''

data ='''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>
   Two idly's with chutney
   </description>
    <calories>553</calories>
</food>
</metadata>
'''
#print(x)
p = re.compile('2021')

# for line in sys.stdin.readlines():
#tree = ET.parse('/users/riliu2/Documents/callhistoryEvent.xml')

root = ET.fromstring(x)
#print(x)
dir(root)

#root = tree.getroot()

for child in root:
    print(child.tag[33:], child.text)
    if child.tag[33:] == 'eventData':
        eventdataChild = child.findall('call')
        dir(eventdataChild)
        print(eventdataChild)
        # for child2 in eventdataChild:
        #print(child2.tag, child2.text)
    print(child.tag[33:], child.text)
