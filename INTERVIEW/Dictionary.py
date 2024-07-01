########### Dictionary ########
#A dictionary is collection which is unordered and changable
#This is mutable

#exa
# mydic={101:"x",102:"y",103:"z"}
# print(mydic)

#nested

# dic={1:'geek',2:'for',3:{'a':'welcome','b':'python'}}
# print(dic)

#add key n value in empty dic
# d={}
# d[0]="geeks"
# d[1]="neet"
# d[3]="geet"
# print(d)

#accsess value
# Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# print(Dict['name'])
# print(Dict.get(3))

#del
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# del(dict[1])
# print(dict)
# del(dict)
# print(dict)

#####
# dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())
# print(dict1.popitem())
# print(dict1.update({3:"scalar"}))
# print(dict1)

#change value
mydic={'a':1,'b':2,'c':3}
# mydic['c']=10
# print(mydic)
# mydic['d']=20
# print(mydic)

#loop
# for i in mydic:
#     print(mydic[i])

#
for x,y in mydic.items():
    print(x,y)








