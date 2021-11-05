import json
import requests
import urllib.parse as parse
import math
from yattag import Doc
from yattag import indent

'''print('Récupération des centres de la métrole de Lyon')
reponse_http = requests.get('https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=cov_covid19.covcentrevaccination_1&outputFormat=application/json; subtype=geojson&SRSNAME=EPSG:4326&startIndex=0&count=10&'+ parse.urlencode({'format':'json'}),headers={'Accept': 'application/json', 'User-Agent': 'Python'})
reponse_centre = reponse_http.json()
print(reponse_centre)
for feature in reponse['features']:
    nomcentre=feature['properties']['nom']
    print(f"{nomcentre[:15]}... : {feature['properties']['telephone']} ({feature['geometry']['coordinates'][0]},{feature['geometry']['coordinates'][1]})")
with open('sortie/centres.geojson', 'w', encoding='utf-8') as fichier : 
    fichier.write(json.dumps(reponse))

print('Récupération des hôpitaux de Lyon avec Here - Génération dun fichier GeoJSON')
reponse_http = requests.get('https://places.ls.hereapi.com/places/v1/discover/search?'+ parse.urlencode({
   'q':'hospital',
   'at':'45.76093,4.83366',
   'size':'5',
   'apiKey':'   YDPvDOCln94J7OXEi8GiV2pcMva4jU0TEqHhtRavjqg'
}), headers={'Accept': 'application/json', 'User-Agent': 'Python'})
reponse_GL = reponse_http.json()
print(reponse_GL)
for hopital in reponse ['results']['items']:
    nomHopital=hopital['title']
    adress=hopital['vicinity']
    print(f"{nomHopital[:18]}..., {adress[:30]}... ({hopital['position'][0]},{hopital['position'][1]})")

f = open('sortie/hopitaux.geojson', "w")
geojsons=[]

for hopital in reponse ['results']['items']:
   coord_lat=hopital['position'][0]
   coord_long=hopital['position'][1]
   hopital['position'][0]=coord_long
   hopital['position'][1]=coord_lat

for hopital in reponse ['results']['items']:
   geojsons.append(                                      
                   {
                     "type": "Feature",
                     "geometry":
                         {                  
                             "type": "Point",
                             "coordinates": hopital['position']
                         },
                     "properties":
                         {
                             "adresse": "{}".format(hopital['vicinity']),
                             "nom": "{}".format(hopital['title'])
                         }          
                   }
   
          )
geojson = {"type": "FeatureCollection",  "features":geojsons}
#print(geojson)

f.write(json.dumps(geojson))
f.close()

f1 = open("sortie/hopitaux.kml", "w")

doc, tag, text = Doc().tagtext()

source= open("sortie/hopitaux.geojson",'r+')

         # First we load existing data into a dict.
file_data = json.load(source)


doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

with tag('kml', ("xmlns","http://www.opengis.net/kml/2.2")):
   with tag('Document'):
       
       for feature in file_data['features']:
           with tag('Placemark'):
               with tag('nom'):
                   text(str(feature['properties']['nom']))
               with tag(str(feature['geometry']['type'])):
                   with tag('coordinates'):
                       text(str(feature['geometry']['coordinates'])[1:len(str(feature['geometry']['coordinates']))-1]+",0")
                   

print(doc.getvalue())


file=doc.getvalue()

f1.write(file)

source.close()
f1.close()'''

#Problème de clé API donc on est reparties des fichiers geojson !
f1 = open("sortie/hopitaux.geojson", "r")
reponse_Here = json.load(f1)

print(reponse_Here)

f2=open('sortie/centres.geojson', "r")
reponse_GL = json.load(f2)
print(reponse_GL)


for centre in reponse_GL['features']:
   print(f"{centre['properties']['nom']} \n")
   for hopital in reponse_Here ['features']:
       print(f"{hopital['properties']['nom']}")
       
       x_centre=centre['geometry']['coordinates'][0]
       y_centre=centre['geometry']['coordinates'][1]
       x_hopital=hopital['geometry']['coordinates'][0]
       y_hopital=hopital['geometry']['coordinates'][1]
       dist=math.sqrt( (x_centre-x_hopital)**2 * math.cos(y_hopital * math.pi / 180)**2 + (y_centre-y_hopital)**2 ) * 60 * 1852
       print(f"distance: {dist}")
       if dist>200:
           print("INVALID")
       else:
           print("VALID")
        




