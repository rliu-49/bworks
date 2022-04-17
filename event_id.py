""" while (<>) {
	$time = $1 if /^202[0-9]\.\d{2}\.\d{2} (\S+)/ ;
	#AS XSLogs
	
	if (/Received From/) {
	    ($ignore, $fromhost) = split(/:/) if /Received From/;
    }
	elsif (/OCI-C Bytes IN/) {
		chomp($fromhost = (split / /)[5]);
	}
     
	if  (/SubscriptionEvent.*eventID>([^<]+)/) {
		$event{$1} = $1;
		$sent{$1}=$time;
		
		
	}
	
	if (/^\s+<(?:xsi:)?eventID>([^<]+)</|/EventResponse.*<(?:xsi:)?eventID>([^<]+)</ ) {
		$event{$1} = $1;
		$from{$1} = $fromhost;
		$recv{$1} = $time if /^\s+<(?:xsi:)?eventID>([^<]+)</|/EventResponse.*<(?:xsi:)?eventID>([^<]+)</ ;
		

	}
	

}
foreach $k (keys(%event)) {
	print "$k $sent{$k} $recv{$k} ", timestamp_ms($recv{$k})  - timestamp_ms($sent{$k}), " $from{$k} \n" if $recv{$k};
	push(@not_ack, $k) unless $recv{$k};
}
print "not acked ---@not_ack\n";

#print values %recv,"\n";

sub timestamp_ms
{
	$time = shift;
	($hour, $min, $sec ,$msec) = split(/:/, $time);
	$time_ms = ($hour * 3600 + $min * 60 + $sec) * 1000 + $msec;
	return $time_ms;
} """

import re
import sys
import xml.etree.ElementTree as et
import datetime

xslog = 'XSLog2021.03.09-15.19.50.txt'

def get_event_id(line):
    '''return eventID tag value'''
    root = et.fromstring(line)
    return root[0].text

lines = []
rx1 = re.compile('(^202[0-9]\.\d{2}\.\d{2}) (\S+).*xsi-events')
rx2 = re.compile('^\s+<(?:xsi:)?eventID>([^<]+)</|/EventResponse.*<(?:xsi:)?eventID>([^<]+)<')
rx3 = re.compile('<xsi:Event xsi1:type="xsi:SubscriptionEvent"')

sent = {}
recv = {}
dt = None

with open(xslog, 'r', encoding='iso-8859-1') as x:
    file = x.readlines()
    for line in file:
        m = re.match(rx1, line)
        event_response = re.match(rx2, line)
        event_match = re.match(rx3, line)
        if m:
             #print(f'{m.group(1)} {m.group(2)}')
             date_time = f'{m.group(1)} {m.group(2)}'
             dt = datetime.datetime.strptime(date_time, '%Y.%m.%d %H:%M:%S:%f')
             #print(dt)
        elif event_response:
            #print(f'{event_response.group(1)}')
            id = event_response.group(1)
            recv[id] = dt
        elif event_match:
            #print(f'event sent', get_event_id(line))
            id = get_event_id(line)
            sent[id] = dt
    print(len(recv))
    #print(recv)
    print(len(sent))
    recv_set = set(recv.keys())
    sent_set = set(sent.keys())
    
    for k,v in recv.items():
        if k in sent_set:
            time_diff = recv[k] - sent[k]
            print(f'{k} {time_diff.microseconds / 1000}')
    print('difference= ' ,sent_set.difference(recv_set))




