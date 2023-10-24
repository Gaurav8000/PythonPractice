dict={"brand":"ford",
      "model":"mustang",
      "year":1964 }
x=dict["model"]
print(x)
y=dict.get("year")
print(y)
z=dict.keys()
print(z)
dict.update({"year":2020})
print(dict)
########
dict.pop("model")
print(dict)
dict.update({"model":"mustag","type":"car"})
print(dict)
del dict["brand"]
print(dict)
#dict.setdefault({"color":"red"})
print(dict)
for  key,value in dict.items():
      print(key,value)
dict1={"car":"nano",
       "year":1995
}
dict1["car"]="creata"
for key,value in dict1.items():
    print(f'{key},{value}')