from loguru import logger
import pandas as pd 
import numpy as np
import itertools

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
        df.loc[j,i]=data[i][j]

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

df2=df.copy()

# Check angka maximum kombinasi 
dfComb=df.loc[userInputList, :]
#print(dfComb)

for i in userInput: 
    dfComb.loc[i, :]=userInput[i]/dfComb.loc[i, :]

df2=dfComb.apply(np.ceil)
df2.dropna(axis=1,how="all",inplace=True) # buang kolom bila semua nan
#df2.fillna(0,inplace=True)

required=df2.max(axis=0)
required=required+1
constraint=required.astype(int).to_list()

dfMod=df[df2.columns]

hold=0

def fillCombo(position, number):
    global hold 
    #print(position, number, hold)
    if position>=hold:
        combo[position]=number
        hold=position
    else: 
        combo[position]=number
        hold=position
        combo[position+1:]=[0 for z in combo[position+1:]]
        #for i in range(position+1,len(dfMod.columns)):
            #combo[i]=0

combo=[]
for i in dfMod.columns:
    combo.append(0)

hitung=0

master=[]
def generate(rep): 
    #repfixed=rep
    def loops(rep):
        global dfMod, dfUser, master, combo, constraint, repfixed, hitung
        if rep>= 1:
            for x in range(constraint[repfixed-rep]):
                #columnPosition=repfixed-rep
                fillCombo(repfixed-rep, x)
                #print(combo)
                #print(columnPosition, x)
                df3=dfMod.copy()
                #for i,j in enumerate(combo):
                    #df3.iloc[:,i]=df3.iloc[:,i]*combo[i]
                df3=df3*combo
                total=df3.sum(axis=1,skipna=True)
                df3["total"]=total
                df3=pd.concat([df3,dfUser],axis=1,sort=False)
                check= np.where(df3["total"] >= df3["need"], True, False)
                #df3["check"]=check
                #print(df3)
                #a=df3["check"].all()
                hitung+=1
                a=check.all()
                                #print(columnPosition, x)
                if a: 
                    master.append(df3.loc["energy","total"])
                    #print(df3.loc["energy","total"])
                    #print("break")
                    break
                loops(rep - 1)
    loops(rep)

logger.info("Start")
repfixed=len(dfMod.columns)
generate(repfixed)
logger.info("End")
print(hitung)


