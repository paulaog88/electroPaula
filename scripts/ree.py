import requests
from pprint import pprint
import pandas as pd
import xml.etree.ElementTree as ET
import zipfile
import StringIO
import os
try:
    rows, columns = os.popen('stty size', 'r').read().split()
    pd.set_option('display.width', int(columns))
except Exception as e:
    print e
    print 'No adapted pandas to display size'
    pass


def xml2df(xml_data):
    root = ET.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
            all_records.append(record)
    return pd.DataFrame(all_records)


def get_list_archives(token):
    headers = {'Accept': 'application/json; application/vnd.esios-api-v1+json',
               'Content-Type': 'application/json',
               'Host': 'api.esios.ree.es',
               'Authorization': 'Token token=' + token,
               'Cookie': ''
               }

    host ='https://api.esios.ree.es'

    r = requests.get(host+'/archives', headers=headers)

    with open('archivos.json', 'wt') as out:
        pprint(archives, stream=out)
    quit()


def get_archive(token, archive, start_date, end_date):
    headers = {'Accept': 'application/json; application/vnd.esios-api-v1+json',
               'Content-Type': 'application/json',
               'Host': 'api.esios.ree.es',
               'Authorization': 'Token token=' + token,
               'Cookie': ''
               }

    params = {'start_date': start_date,
              'end_date': end_date}


    host ='https://api.esios.ree.es'

    r = requests.get(host+'/archives/'+str(archive), params=params, headers=headers)

    print r

    return r



def download_archive(archive, start_date, end_date):
    params = {'start_date': start_date,
              'end_date': end_date}

    host ='https://api.esios.ree.es'

    r = requests.get(host+'/archives/'+str(archive)+'/download/', params=params)

    print r

    return r



token = '69ccbeb51a4e6e9daf0b8897d9bf242d7651e74558349bceb4f600580f9e6f63'

#~ headers = {'Accept': 'application/json; application/vnd.esios-api-v1+json',
           #~ 'Content-Type': 'application/json',
           #~ 'Host': 'api.esios.ree.es',
           #~ 'Authorization': 'Token token=' + token,
           #~ 'Cookie': ''
           #~ }


#~ parameters = {'start_date':'2017-10-01',
              #~ 'end_date':'2017-11-30'}


#~ host ='https://api.esios.ree.es'

#~ r = requests.get(host+'/archives', headers=headers)

#~ print r
#~ archives = r.json()
#~ pprint(archives)




#~ archives = get_list_archives(token)


#~ r = get_archive(token, 29, '2017-10-01', '2017-11-30')
r = download_archive(20, '2017-10-01', '2017-10-29')

if zipfile.is_zipfile(StringIO.StringIO(r.content)):
    print 'Zip file:'
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    for fileName in z.namelist():
        print fileName
        if fileName[-3:] == 'xls':
            print 'xls file'
            openedFile = z.open(fileName)
            df = pd.read_excel(openedFile)
            print df
        elif fileName[-3:] == 'xml':
            print 'xml file'
            openedFile = z.read(fileName)
            df = xml2df(openedFile)
            print df
else:
    print 'Not zip file:'
    df = pd.read_excel(StringIO.StringIO(r.content))
    print df
