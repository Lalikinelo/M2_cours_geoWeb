# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:13:23 2021

@author: lkiener
"""

import http.client
import json
import urllib.parse as parse
import requests


#############################################################
#
#       Un premier service simple non cartographique
#
#############################################################

"""
connection_Linguatools = http.client.HTTPConnection("lt-nlgservice.herokuapp.com")

verbe = input("write an Infinitive verb : ")

connection_Linguatools.request("GET","https://lt-nlgservice.herokuapp.com/rest/english/conjugate?verb="+verbe)

response_http=connection_Linguatools.getresponse()

response_Linguatools=json.loads(bytes.decode(response_http.read()))

if response_Linguatools['result'][-17:]=='nicht im Lexikon.':
   print("ce mot n'estiste pas dans le Lexikon")
else:
    for conjugated_forms in response_Linguatools['conjugation_tables']['indicative']:
        if conjugated_forms["heading"]=="simple past":
            for conj in conjugated_forms["forms"]:
                print("\n"+conj[0]+" "+conj[1])
    


#############################################################
#
#       Service de géocodage
#
#############################################################   

connection_nominatim = http.client.HTTPSConnection("nominatim.openstreetmap.org")

adresse = input("saisie ton adresse: ")


connection_nominatim.request("GET","/search?"+parse.urlencode({'q': adresse, 'format':'json'}),'',{'Accept':'application/json','User-Agent':'Python'})
                           


response_http=connection_nominatim.getresponse()
response_nominatim=json.loads(bytes.decode(response_http.read()))
print("Lat : {}  Lon: {}".format(response_nominatim[0]['lat'],response_nominatim[0]['lon']))




#############################################################
#
#       module request
#
#############################################################   

r = requests.get('https://lt-nlgservice.herokuapp.com/rest/english/conjugate?verb=change')  
#print(r.url)
#print(r.text)

if r.json()['result'][-17:]=='nicht im Lexikon.':
   print("ce mot n'estiste pas dans le Lexikon")
else:
    for conjugated_forms in r.json()['conjugation_tables']['indicative']:
        if conjugated_forms["heading"]=="simple past":
            for conj in conjugated_forms["forms"]:
                print("\n"+conj[0]+" "+conj[1])
                
"""
               
r = requests.get("https://nominatim.openstreetmap.org/search?"+parse.urlencode({'q':"10 rue docteur laennec Caluire", 'format':'json'}),headers={'Accept':'application/json','User-Agent':'Python'})
print("Lat : {}  Lon: {}".format(r.json()[0]['lat'],r.json()[0]['lon']))

