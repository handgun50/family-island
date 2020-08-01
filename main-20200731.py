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
df2.fillna(0,inplace=True)
#df2.drop("energy",axis=0,inplace=True)
df2=df2.reindex(sorted(df.columns),axis=1)

required=df2.max(axis=0).to_dict()
combination=[]

for i in required: 
    temp=list(range(0,int(required[i])+1))
    combination.append(temp)

#print(required)
#print(combination)

# Generate kombinasi lengkap 
logger.info("Combination start")
combination2=list(list(tup) for tup in (itertools.product(*combination)))
logger.info("Combination done")

#print(combination2)

# Check tiap kombinasi 
result=[]

logger.info("Pd start")
for i in combination2:
    df3=df.copy()
    #df3.drop("energy",axis=0,inplace=True)
    for j,k in enumerate(list(df3.columns)): 
        df3[k]=df3[k]*i[j]
    total=df3.sum(axis=1,skipna=True)
    df3["total"]=total
    df3=pd.concat([df3,dfUser],axis=1,sort=False)
    check= np.where(df3["total"] >= df3["need"], True, False)
    df3["check"]=check
    a=df3["check"].all()
    #print(df3)
    if a: 
        #print(a)
        i.append(df3.loc["energy","total"])
        result.append(i)

logger.info("pd end")
   #print(total)

dfColumns=df.columns 
temp=pd.Index(["energy"])
dfColumns=dfColumns.append(temp)
#print(dfColumns)
resultDf=pd.DataFrame(result,columns=dfColumns)
resultDf.sort_values(by=["energy"],inplace=True)


print(resultDf)

#5 5 1580 solution 

for i in firtree17(1...12):
    if alltrue break
    for j in firtree34(1...10):
        if alltrue break
        for k in firtree78(1...25):
            if alltrue break 

y=25

temp=[]
def asdf(yy, nn): 
    global temp
    print("a")
    def loop_rec(y, n):
        global temp, x
        if n >= 1:
            for x in range(y):
                temp.append(x)
                print(temp)
                loop_rec(y, n - 1)
    loop_rec(yy,nn)
    

def collect_folders(start, depth=-1)
    """ negative depths means unlimited recursion """
    folder_ids = []

    # recursive function that collects all the ids in `acc`
    def recurse(current, depth):
        folder_ids.append(current.id)
        if depth != 0:
            for folder in getChildFolders(current.id):
                # recursive call for each subfolder
                recurse(folder, depth-1)

    recurse(start, depth) # starts the recursion
    return folder_ids
    
df3=pd.DataFrame()


hold=0

def fillCombo(position, number):
    global hold 
    print(position, number, hold)
    if position>=hold:
        combo[position]=number
        hold=position
    else: 
        combo[position]=number
        hold=position
        for i in range(position+1,len(df.columns)):
            print("as")
            combo[i]=0

combo=[]
for i in df.columns:
    combo.append(0)

master=[]
def asd(length, rep): 
    repfixed=rep
    def loops(length, rep, repfixed):
        global df, dfUser, master, combo
        if rep>= 1:
            for x in range(length):
                columnPosition=repfixed-rep
                fillCombo(columnPosition, x)
                #print(combo)
                #print(columnPosition, x)
                df3=df.copy()
                for i,j in enumerate(combo):
                    df3.iloc[:,i]=df3.iloc[:,i]*combo[i]
                total=df3.sum(axis=1,skipna=True)
                df3["total"]=total
                df3=pd.concat([df3,dfUser],axis=1,sort=False)
                check= np.where(df3["total"] >= df3["need"], True, False)
                df3["check"]=check
                print(df3)
                a=df3["check"].all()
                                #print(columnPosition, x)
                if a: 
                    master.append(df3.loc["energy","total"])
                    #print(df3.loc["energy","total"])
                    break
                loops(length, rep - 1,repfixed)
    loops(length,rep, repfixed)

asd(3,len(df.columns))



