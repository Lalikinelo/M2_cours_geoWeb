#########################################################
#
#ecrite un fichier geojson avec 1 point , methode chaine de caracteres
#
#########################################################
import json

# hanoi

# w: erase and write || x : create new file
f = open("hanoi.geojson", "w")
file="{\n  \"type\": \"Feature\",\n  \"geometry\": \n {\"type\": \"Point\",\n \"coordinates\": [105.84,21.033]\n},\n  \"properties\": {\n    \"name\": \"Hanoi\"\n}\n}"

f.write(file)
f.close()

#########################################################
#
#ecrite un fichier geojson avec plusieurs points, methode bibli json
#
#########################################################

# villes afrique du sud

f = open("villes_afriquedusud.geojson", "w")
file={ 
      "type": "FeatureCollection",  "features": 
          [ 
              {
                  "type": "Feature",
                  "geometry": 
                      {                  
                          "type": "Point",
                          "coordinates": [-26.204,28.0343]
                      },
                  "properties": 
                      {
                          "name": "Johannesbourg "
                      }           
              }, 
              {
                  "type": "Feature",
                  "geometry": 
                      {
                          "type": "Point",
                          "coordinates": [-33.9248,18.4197]
                      },
                  "properties": 
                      {
                          "name": "Le cap"
                      }
              }
          ]
     }


f.write(json.dumps(file))
f.close()

"""
#open and read the file :
f = open("villes_afriquedusud.geojson", "r")
print(f.read()) 
f.close()

"""

#########################################################
#
# insertion d'un point dans un geojson existant
#
#########################################################




data = open("hanoi.geojson", "r")


source= open("villes_vietnam.geojson",'r+')

          # First we load existing data into a dict.
file_data = json.load(source)


new_data = json.load(data)


        # Join new_data with file_data inside emp_details
file_data["features"].append(new_data)
print(file_data)

        # Sets file's current position at offset.
source.seek(0)
        # convert back to json.
json.dump(file_data, source, indent = 4)







