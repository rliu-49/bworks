#!/usr/bin/python

import time
import datetime
import socket
import os
import re
import smtplib
from email.mime.text import MIMEText

smtp_server = '10.83.154.68'
email_from = "webnms-admin@adventnet.com"
email_to = "jonmarte@cisco.com, teamsupport@broadsoft.com, rbarney@cisco.com, lauragri@cisco.com"
error_string = "Access Status: DB_NA"
errors = []
host = socket.gethostname()
dir = "/var/broadworks/logs/appserver/"
filestartswith = "XSLog2"

def initial_run():
    #print('Starting initial run.')
    subject = """Starting DB monitoring for host: %s""" % (host)
    payload = ""
    payload.join(('Starting DB monitoring for host: ', host, '\n'))
    payload.join((payload, 'Start time: ', getTime()))
    cv = getValue(filestartswith, dir, error_string)
    sendMail(subject, payload)

def getTime():
    rv = str(datetime.datetime.now())
    return rv

def getValue(file, dir, string):
    file = currentLog(file, dir)
    return len(find_in_file(string, file, True, True))

def sendMail(subject, payload):
    #print('Sending mail:\nSubject: %s\nPayload: %s' % (subject, payload))
    #print('Payload length: %s' % (len(payload)))
    msg = MIMEText(payload)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to
    server = smtplib.SMTP(smtp_server, 25)
    server.sendmail(email_from, email_to, msg.as_string())

def checkXSLog(string):
    #print('Starting Log Check.')
    file = currentLog(filestartswith, dir)
    errors = find_in_file(string, file, True, True)
    if len(errors) > 0:
        payload = ""
        subject = ("Error detected on host: %s in file: %s" % (host, file))
        #print('Error type: %s' % (type(errors)))
        for i in range(len(errors)):
            #print('Index value: %s' % i)
            #print('errors[%s] value: %s' % (i, errors[i]))
            payload.join((payload, 'File name:   ', (errors[i][2]), '\n'))
            payload.join((payload, 'Line number: ', (str(errors[i][0])), '\n'))
            payload.join((payload, 'Error Line:  ', (errors[i][1]), '\n'))
            #print('Payload: %s' % (payload))
        sendMail(subject, payload)

def currentLog(file, dir):
    files = [x for x in os.listdir(dir) if x.startswith(file)]
    newest = max(files, key=os.path.getctime)
    #print('Newest: %s' % (newest))
    return newest

def find_in_file(pattern, filename, regex=False, string=True):
    """
    Looks for pattern in filename and returns the line and line number as a list of tuples.
    Default is a straight string comparison, set regex True to use a regex search.
    Returns an empty list for nothing found.

    Input:
        pattern - RegEx or String to search for in the file
        filename - FILENAME of the file to search in
        regex - BOOLEAN of whether to use string matching or regex

    Output:
        return_list - a list of tuples representing (line number, line) for each line that contained PATTERN.
    """
    read = ''
    if string == True:
        read = 'r'
    else:
        read = 'rb'

    return_list = []
    if (pattern) and (filename):
        if regex:
            with open(filename, read, errors='ignore') as f:
                for num, line in enumerate(f):
                    if re.search(pattern, line) != None:
                        return_list.append((num, line, filename))
        else:
            with open(filename, read, errors='ignore') as f:
                for num, line in enumerate(f):
                    # try:
                    if pattern in line:
                        return_list.append((num, line, filename))
    if (pattern is None) and (filename):
        with open(filename, read, errors='ignore') as f:
            for num, line in enumerate(f):
                return_list.append((num, line, filename))

    return return_list

initial_run()

while True:
    cv = getValue(filestartswith, dir, error_string)
    time.sleep(10)
    nv = getValue(filestartswith, dir, error_string)
    if nv > cv:
        checkXSLog(error_string)


