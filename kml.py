# -*- coding: utf-8 -*-
"""
###################################################

                Single placemark

@author: lkiener
###################################################
"""

import yattag 
from yattag import Doc
import json


f = open("hanoi.kml", "w")

doc, tag, text = Doc().tagtext()

        

doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

with tag('kml', ("xmlns","http://www.opengis.net/kml/2.2")):
    with tag('Document'):
        with tag('Placemark'):
            with tag('name'):
                text('Hanoi')
            with tag('Point'):
                with tag('coordinates'):
                    text('105.84,21.033,0')
                
 
    print(doc.getvalue())

file=doc.getvalue()

f.write(file)
f.close()


"""
###################################################

                several placemark

@author: lkiener
###################################################
"""

f = open("villes_afriquedusud.kml", "w")

doc, tag, text = Doc().tagtext()

        

doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

with tag('kml', ("xmlns","http://www.opengis.net/kml/2.2")):
    with tag('Document'):
        with tag('Placemark'):
            with tag('name'):
                text('Johannesbourg')
            with tag('Point'):
                with tag('coordinates'):
                    text('28.0343,-26.204,0')
        with tag('Placemark'):
            with tag('name'):
                text('Le Cap')
            with tag('Point'):
                with tag('coordinates'):
                    text('18.4197,-33.9248,0')        
 
    print(doc.getvalue())




file=doc.getvalue()

f.write(file)
f.close()




"""
###################################################

                conversion geojson kml
                
@author: lkiener
###################################################
"""



f1 = open("villes_vietnam_exo_gen_from_geojson.kml", "w")

doc, tag, text = Doc().tagtext()

source= open("villes_vietnam_exo.geojson",'r+')

          # First we load existing data into a dict.
file_data = json.load(source)

print("\n"+str(file_data))

print("\n"+str(type(file_data)))



doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

with tag('kml', ("xmlns","http://www.opengis.net/kml/2.2")):
    with tag('Document'):
        
        for feature in file_data['features']:
            with tag('Placemark'):
                with tag('name'):
                    text(str(feature['properties']['name']))
                with tag(str(feature['geometry']['type'])):
                    with tag('coordinates'):
                        text(str(feature['geometry']['coordinates'])[1:len(str(feature['geometry']['coordinates']))-1]+",0")
                    

print(doc.getvalue())


file=doc.getvalue()

f1.write(file)

source.close()
f1.close()

#for i in range(file_data.count('Point')):
#    print(i)



"""
###################################################

  Sérialisation en KML de données stockées dans geojson
                
@author: lkiener
###################################################
"""

f1 = open("trip.kml", "w")

doc, tag, text = Doc().tagtext()

source= open("trip.geojson",'r+')

          # First we load existing data into a dict.
file_data = json.load(source)

print("\n\n")

text_coord=""
nb_coord=0


doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

with tag('kml', ("xmlns","http://www.opengis.net/kml/2.2")):
    with tag('Document'):
        
        for feature in file_data['features']:
            with tag('Placemark'):
                with tag('name'):
                    text(str(feature['properties']['Name']))
                with tag(str(feature['geometry']['type'])):
                    with tag('coordinates'):
                        for coord in feature['geometry']['coordinates']:
                            nb_coord+=1
                            if type(coord) is list:
                                for sub_coord in coord:
                                        text_coord+=str(sub_coord)+","
                                text(text_coord[:-1]+"\n")
                                text_coord=""
                                        #text_line_coord=text_line_coord+str(sub_coord)+"\n"
                            if type(coord) is float:
                                text_coord+=str(coord)+","
                                if(nb_coord==3):
                                    text(text_coord[:-1])
                                    text_coord=""
                                    nb_coord=0
                            
                        
                                


print(doc.getvalue())


file=doc.getvalue()

f1.write(file)

source.close()
f1.close()

  
  
  
  