from loguru import logger
import pandas as pd 
import numpy as np
import itertools 
import time

pd.set_option('use_inf_as_na', True)

resource=[]
material=[]

# Resource : Material yang dihasilkan dan energi yang dibutuhkan
data={
"tree":{"log":4,"stick":3,"energy":10},
"grass4":{"grass":2,"energy":4},
"fir tree 17":{"fir cones":1,"log":1,"energy":17},       #fb indo 
"fir tree 27":{"fir cones":2.5,"log":1.5,"energy":27},   #fb indo 
"fir tree 44":{"fir cones":3,"log":2.5,"energy":44},     #fb indo 
"fir tree 84":{"fir cones":4.5,"log":3.5,"energy":84},   #fb indo 
"fir tree 119":{"fir cones":6,"log":5.5,"energy":119},   #fb indo 
"grass5":{"grass":3,"energy":5}
}

for i in data: 
    resource.append(i)
    for j in data[i]:
        material.append(j)

index=(list(set(material)))
column=resource 

df=pd.DataFrame(columns=column,index=index)
df=df.reindex(sorted(df.columns),axis=1)

for i in data: 
    for j in data[i]:
        df.at[j,i]=data[i][j]

df.fillna(0,inplace=True)
#print(df)

# Inputan dari user
userInput={
"grass":5,
"fir cones":5
}

# Rakit df user 
userInputList=[]
dfUser=pd.DataFrame(columns=["need"],index=df.index)
for i in userInput: 
    dfUser.loc[i, "need"]=userInput[i]
    userInputList.append(i)

dfUser.fillna(0,inplace=True)
srUser=dfUser.iloc[:,0]

df2=df.copy()

# Check angka maximum kombinasi 
dfComb=df.loc[userInputList, :]
#print(dfComb)

for i in userInput: 
    dfComb.loc[i, :]=userInput[i]/dfComb.loc[i, :]

df2=dfComb.apply(np.ceil)
df2.fillna(0,inplace=True)
#df2.drop("energy",axis=0,inplace=True)
df2=df2.reindex(sorted(df.columns),axis=1)

required=df2.astype("int").max(axis=0).to_list()
combination=[list(range(0,i+1)) for i in required]

required2 = [i+1 for i in required]

required3=[]
for i, j in enumerate(required2):
    temp=1
    for k in required2[i:]:
        temp=temp*k 
    required3.append(temp)

srReq=pd.Series(required3)
#print(required)
#print(combination)

# Generate kombinasi lengkap 
logger.info("Combination start")
combination2=list(list(tup) for tup in (itertools.product(*combination)))
logger.info("Combination done")

#print(combination2)

# Check tiap kombinasi 
result=[]
hitung=0

startTime=time.time()
i=0
while i<len(combination2):
    #print(i, combination2[i])
    df3=df.copy()
    #df3.drop("energy",axis=0,inplace=True)
    #for j,k in enumerate(list(df3.columns)): 
        #df3[k]=df3[k]*i[j]
    df3=df3*combination2[i]
    total=df3.sum(axis=1,skipna=True)
    #df3["total"]=total
    #df3=pd.concat([df3,dfUser],axis=1,sort=False)
    #check= np.where(df3["total"] >= df3["need"], True, False)
    check= np.where(total>=srUser, True, False) 
    #print("check")
    #df3["check"]=check
    #a=df3["check"].all()
    #print(df3)
    a=check.all()
    if a: 
        #print(a)
        hitung+=1
        combination2[i].append(total.at["energy"])
        result.append(combination2[i])
        #srMod=i % srReq         
        #try: 
            #position=srMod[srMod==0].index[0]
            #i=(i + (srReq.iat[position])) - (i % (srReq.iat[position]))
            #continue
        #except:
            #i=(i + (srReq.iat[-1])) - (i % (srReq.iat[-1]))
            #continue
        for q,w in enumerate(required3):
            remainder=i % w 
            if remainder ==0:
                #print(required3)
                #print(q)
                i=(i+ w) - (i % w)
                #print(temp10)
                #i=temp10
                
                break 
        if remainder==0:
            continue
        i=(i+required3[:1][0]) - (i % (required3[:1][0]))
        #i=temp11
        continue
        #i.append(df3.loc["energy","total"])
    i+=1


endTime=time.time()
   #print(total)

dfColumns=df.columns 
temp=pd.Index(["energy"])
dfColumns=dfColumns.append(temp)
#print(dfColumns)
resultDf=pd.DataFrame(result,columns=dfColumns)
resultDf.sort_values(by=["energy"],inplace=True)


print(resultDf)

diffTime=endTime-startTime 
diffTime="{0:.2f}".format(diffTime)
print(hitung)
print(diffTime)
print(diffTime/60)

#5 5 1580 solution 






