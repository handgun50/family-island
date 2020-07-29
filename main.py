import pandas as pd 
import numpy as np
import itertools

pd.set_option('use_inf_as_na', True)

resource=[]
material=[]

# Hasil dari setiap tebasan dan energy yang digunakan
data={
"tree":{"log":4,"stick":3,"energy":10},
"grass4":{"grass":2,"energy":4},
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
"grass":3,
"stick":3 
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
print(dfComb)

for i in userInput: 
    dfComb.loc[i, :]=userInput[i]/dfComb.loc[i, :]

df2=dfComb.apply(np.ceil)
df2.fillna(0,inplace=True)
df2.drop("energy",axis=0,inplace=True)
df2=df2.reindex(sorted(df.columns),axis=1)

required=df2.max(axis=0).to_dict()
combination=[]

for i in required: 
    temp=list(range(0,int(required[i])+1))
    combination.append(temp)

#print(required)
#print(combination)

# Generate kombinasi lengkap
combination2=list(itertools.product(*combination))

#print(combination2)

# Check tiap kombinasi
for i in combination2:
    df3=df.copy()
    #df3.drop("energy",axis=0,inplace=True)
    for j,k in enumerate(list(df3.columns)): 
        df3[k]=df3[k]*i[j]
    total=df3.sum(axis=1,skipna=True)
    df3["total"]=total
    df3=pd.concat([df3,dfUser],axis=1,sort=False)
    check= np.where(df3["total"] >= df3["need"], "Good", "Bad")
    df3["check"]=check
    print(df3)
    #print(total)
    




