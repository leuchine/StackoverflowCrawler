import pandas as pd

f=pd.read_csv('answers.csv')
dic=set()
print(f['j'])
for i in f['i']:
    dic.add(str(i))
for i in f['j']:
    dic.add(str(i))
print(len(dic))
with open('userlist.txt','w') as fw:
    for i in dic:
        fw.write(str(i))
        fw.write('\n')
    
