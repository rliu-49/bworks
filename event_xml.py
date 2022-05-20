
import xml.etree.ElementTree as et

s = '<xsi:Event xsi1:type="xsi:SubscriptionEvent" xmlns:xsi="http://schema.broadsoft.com/xsi" xmlns:xsi1="http://www.w3.org/2001/XMLSchema-instance"><xsi:eventID>af5e0081-ac31-4d06-8c7d-658a25b47d7e</xsi:eventID><xsi:sequenceNumber>169</xsi:sequenceNumber><xsi:userId>N2822581R_ENTAdmin@nipt.telstra.com</xsi:userId><xsi:externalApplicationId>bc_tws_tipt01_mel_p</xsi:externalApplicationId><xsi:subscriptionId>d76534ad-0abc-412e-95a2-a648ef279bb7</xsi:subscriptionId><xsi:channelId>2cd6688d-32ff-46a2-9f77-c08a6f81f057</xsi:channelId><xsi:targetId>0282764713@telstra.com</xsi:targetId><xsi:eventData xsi1:type="xsi:CallForwardingBusyEvent"><xsi:info><xsi:active>false</xsi:active></xsi:info></xsi:eventData></xsi:Event>'
root = et.fromstring(s)
x = {child.tag[33:]: child.text for child in root}
print(x['targetId'])
ns = {'bworks': 'http://schema.broadsoft.com/xsi'}
tree = root.find('bworks:eventData', ns)
print(tree)
for child in tree:
    print(child.tag, child.text)

for k, v in x.items():
    if k == 'eventData':
        print(type(v))
        for child in v:
            print(child.tag, child.text)

        '''ed_root = et.fromstring(v)
        ed = {child.tag[33:]: child.text for child in ed_root}
        print(ed)'''
    else:
        print(f'{k} {v}')
