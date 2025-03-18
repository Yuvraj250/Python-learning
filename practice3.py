d = {}
type(d)
d1 = {'key':"sudh"}
d1
d2 = {'nmae':"Sudhanshu","email":"yuvi250102@gmail.com","number":1236}
d2
d3 = {234:"sudh",True:2434,"_123":"YUVI"}
d3
#in dictionary there is no concept like indexing
d3[True]
d3[1]
d4 = {'name':"sudh",'mail_id': "ss@gmail.com","name":123}
d4["name"]#key should be unique ,if its duplicate then it overwrite last value|
d5 = {"Comapny" : 'Yuvraj ',"assignment":['yu','vi',1], "assist":(1,2,3,400)}
d5
d5["assignment"][2]
d6 = {"number" :[2,3,4,5,34],'assignment':(1,2,3,4,5,6),'launch_date':{12,14,18},"class_time":{'webdev': 8,'Data Science Master':8,"DSA":7}}
d6["class_time"]["DSA"]
d6['mentor']=["Sudhanshu","Krish","Anurag"]#adding new key
d6
del d6['number']
d6
d6.keys()
list(d6.keys())
list(d6.values())
list(d6.items())
d6.pop('assignment')#you should put key as argument otherwise key error
d6
marks = input("Enter your marks")
marks
if marks >= 80 :
    print("You will be a part if A0 batch")
elif marks >= 60 and marks < 80:
    print("You will be a part of A1 batch")
else :
    print("You will be a part of A3 batch ")
 