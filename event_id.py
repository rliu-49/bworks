def main(file):
    import re
    import sys
    import xml.etree.ElementTree as et
    import datetime

    xslog = file

    def get_event_id(line):
        '''return eventID tag value'''
        root = et.fromstring(line)
        eventID = root.find('{http://schema.broadsoft.com/xsi}eventID')
        return eventID.text

    rx1 = re.compile(r'(^20[12-9][0-9].\d{2}.\d{2}) (\S+).*xsi-events')
    rx2 = re.compile(r'^\s+<(?:xsi:)?eventID>([^<]+)</|/EventResponse.*<(?:xsi:)?eventID>([^<]+)<')
    rx3 = re.compile(r'<xsi:Event xsi1:type="xsi:SubscriptionEvent"')

    sent = {}
    recv = {}
    dt = None

    with open(xslog, 'r', encoding='iso-8859-1') as x:
        # with open(xslog, 'r') as x:
        #file = x.readlines()
        for line in x:
            m = re.match(rx1, line)
            event_response = re.match(rx2, line)
            event_match = re.match(rx3, line)
            if m:
                #print(f'{m.group(1)} {m.group(2)}')
                date_time = f'{m.group(1)} {m.group(2)}'
                dt = datetime.datetime.strptime(date_time, '%Y.%m.%d %H:%M:%S:%f')
                # print(dt)
            elif event_response:
                # print(f'{event_response.group(1)}')
                id = event_response.group(1)
                recv[id] = dt
            elif event_match:
                #print(f'event sent', get_event_id(line))
                id = get_event_id(line)
                sent[id] = dt
        print(len(recv))
        # print(recv)
        print(len(sent))

        recv_set = set(recv.keys())
        sent_set = set(sent.keys())
        #sent_recv = [x for x in recv_set.intersection(sent_set)]

        for k in recv_set.intersection(sent_set):
            time_diff = recv[k] - sent[k]
            print(f'{k} {time_diff.microseconds / 1000}')

        print('difference= ', sent_set.difference(recv_set))


if __name__ == '__main__':
    import sys
    try:
        main(sys.argv[1])
    except IndexError:
        "Reuqires XSLog file"
