
info = {
    "name" : "mahesh" ,
    "age" : "30" ,
    "location" : "pune" ,
    "skills" : "python"
}

for keys in info.keys():
    print(keys)

for val in info.values():
    print(val)    

for k ,v in info.items():
    print(f"{k} : {v}")


for k in info:
    print(k)

#for k,v in info :
#   print(f"{k} : {v}")           

for k in info :
    print(f"{k} : {info[k]}")


for k in info:
    print(info[k])


print(len(info))


for k in range(len(info)):
    print(k)
#    print(info[k])


# while

keys=list(info.keys())
print(keys)
print(type(keys))

i=0
while i <len(keys):
    k=keys[i]
    print(f"{k} : {info[k]}")
    i=i+1