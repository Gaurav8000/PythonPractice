dict={"john":{"age":15,"class":"first","city":"pune"},
      "kiran":{"age":25,"class":"high","city":"mumbai"},
      "alize":{"age":70,"class":"middle","city":"baramati"}}
x=dict["kiran"]["age"]
print(x)

y=dict["alize"]["city"]
print(y)

dict["john"]["city"]="paris"
print(dict)

dict["kiran"]["experiance"]=12
print(dict)

