import random,time,os

#read 
text=""
users=[]
servers=[]
commands=[]
dates=[]

text_new=[]
with open("log/bot_user_log.txt","r") as f:
  text=f.readlines()
for i in range(len(text)):
  text_new.append(str(text).split(",")[i])
print(text_new[0])