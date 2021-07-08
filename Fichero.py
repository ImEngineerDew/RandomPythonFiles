import json


pais = 
	  {
	    "Nombre": "España",
            "Poblacion": 46700000,
	    "Per capita": 38700
	  },
          {
	     "Nombre":"Colombia",
             "Poblacion": 55600000,
	     "Per capita": 7500
          }


print(pais)
print(type(pais))  

#convertir diccionario a Python
json_pais =  json.loads(pais)
print(json_pais["Nombre"])
