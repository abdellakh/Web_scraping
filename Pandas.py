import pandas as pd
df = pd.read_csv('pokemon_data.csv',delimiter=',')#pour lire le ficher 'pokemon-_data'

#pour lire ou afficher les données du tableau
df.head()

#read headers
df.columns

#read each columns you can also do that with df.Name
df['Name']

#read each Row
df.iloc[1:3]
#for index, row in df.iterrows() :
#	print(index,row['Name'])
df.loc[df['Type1']=='Fire']
df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison') & (df['HP']>70)]
#Sort values asc
df.sort_values('Name')

#Sort values desc (0 mean that the sort will be ascending and 1 mean the opposit)
df.sort_values('Name',ascending=False)
df.sort_values(['Type 1','HP'],ascending=[1,0])

#read a specific location: 2 for the Row and 1 for the columns
df.iloc[2,1]

# 	#	 Making changes
#creat a new column
df['Total']=df['Hp']+df['Attack']

#drop a specific column
df = df.drop(columns=['Total'])

#sum the values of the tables (axis=1 sum the verticul values if axis =0 sum the horizentel values)
df['Total']=df.iloc[:,4:10].sum(axis=1)

#Save Data if you chose to not save data with the indexes you can use (index=false)
df.to_csv('Modified.csv')#save to csv
df.to_excel('modified.xlsx')#seve to excel
df.to_csv('modified.txt',index=False,sep='\t')#sep mean to separate the values with a tab
