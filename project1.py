#!/usr/bin/env python
# coding: utf-8

# This part import all the necessary libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# This part checks for null values or zero values
# Things like age , cost etc can't have zero values

# In[2]:


df= pd.read_csv('insurance.csv',na_values = "x")
null=df.isnull()
print(df.index)
x = 0

#checking for null values
for i in range(1338):
    for j in range(7):
        a =null.iloc[i,j]
        if a == True :
            print("Null value Detected at",i,j)
            x = 1

if x != 1:
    print("No null values present")
print("All columns are")
for i in df:
    print(i)

# checkzero function to check if there are zero values in a column
def chkzro (column):
    s = 0
    for i in range (1338):
        a = df.iloc[i,column]
        if a == 0 :
            print("0 value detected at",i,"in column",column)
        else:
            s = 1
    if s == 1 :
        print("No zero value detected in column",column)

chkzro(0)
chkzro(1)
chkzro(2)
chkzro(4)
chkzro(5)
chkzro(6)


# This part checks for how many males and females smoke

# In[3]:


# starting the analysis

# checking how many males smoke
b = 0
d = 0
c = 0
for i in range(1338):
    ab= df.iloc[i,0]
    ac= df.iloc[i,1]
    ad= df.iloc[i,4]
    if 0<ab<26 and ac == 'male'and ad == 'yes':
        b=b+1
    if  ac == 'male':
        d = d+1
print('Out of',d,'males')
print('Number of males between 0-25 that smoke are',b)

for i in range(1338):
    ab= df.iloc[i,0]
    ac= df.iloc[i,1]
    ad= df.iloc[i,4]
    if 25<ab<100 and ac == 'male' and ad == 'yes' :
        c=c+1
print('Number of males older than 25 that smoke are',c)

# for female
bf = 0
dfe = 0
cf = 0
for i in range(1338):
    ab= df.iloc[i,0]
    ac= df.iloc[i,1]
    ad= df.iloc[i,4]
    if 0<ab<26 and ac == 'female'and ad == 'yes':
        bf=b+1
    if  ac == 'female':
        dfe = d+1

print('Out of',dfe,'females')
print('Number of females between 0-25 that smoke are',bf)

for i in range(1338):
    ab= df.iloc[i,0]
    ac= df.iloc[i,1]
    ad= df.iloc[i,4]
    if 25<ab<100 and ac == 'female' and ad == 'yes' :
        cf=c+1

print('Number of females older than 25 that smoke are',cf)


# This part now plots the data for visualization

# In[4]:


all = [df.age,df.bmi]
plt.title('Age and Bmi ')
plt.boxplot(all,notch=True)
plt.show()
print('Boxplot shows us the outliers in BMI but there is no need to drop them as the values can be possible')

plt.figure()
plt.title('Children')
plt.boxplot(df.children)
plt.show()
print('We can also see the variation in children ')
print('''The box plot also shows us the IQR range , in simpler words the numbers where most of the values lie
For age it have elements more in the range 27 to 51''')


# In[5]:


print('PLot of values of cost of insurance and how many people have it')
print('This tells us most people prefer budget insurance the sweet spot for insurance is near 10000')
plt.xlabel('Cost of insurance')
plt.ylabel('Number of people')
plt.hist(df['charges'],bins=200,width=500)
plt.show()


# In[6]:


# print('Plot of age and bmi')
plt.xlabel('BMI')
plt.ylabel('Number of people')
plt.title('BMI of peoples')
plt.hist(df['bmi'],bins=100)
plt.show()


# In[7]:


# Now checking how much in average a smoker has to pay more than a non smoker
v=0
f=0
n=0
m=0
for i in range(1338):
    a = df.iloc[i,4]
    b = df.iloc[i,6]
    if a==1 or a=='yes':
        v=v+b
        n+=1
    else:
        f=f+b
        m+=1
print('Average value of cost of insurance for smokers is', int(v/n))
print('Average value of cost of insurance for non smokers is',int(f/m))
print('We can see that on average an smoker has to pay',int(v/n-f/m),'more than a non smoker for an insurance')


# In[8]:


#Average values
g=h=ia=j=gn=hn=inn=jn=0
for i in range(1338):
    a = df.iloc[i,5]
    b = df.iloc[i,6]
    if  a=='southeast':
        g = g + b
        gn+=1
    elif a=='southwest':
        h=h+b
        hn+=1
    elif a=='northeast':
        ia=ia+b
        inn+=1
    elif a=='northwest':
        j=j+b
        jn+=1

print('The average charge of insurance for southeast region is',int(g/gn))
print('The average charge of insurance for southwest region is',int(h/hn))
print('The average charge of insurance for northeast region is',int(ia/inn))
print('The average charge of insurance for northwest region is',int(j/jn))
cost = [g/gn,h/hn,ia/inn,j/jn]
ax = ['southeast','southwest','northeast','northwest']
plt.bar(ax,cost)
plt.show()




# In[9]:


plt.title('Cost of insurance relative to BMI')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.bar(df['bmi'],df['charges'])
plt.show()


# This prints the correlation matrix which help in visualizing relations between data

# In[10]:


# now to relation analysis
df['sex'] = df['sex'].map({'male':0,'female':1})
df['smoker'].unique()
df['smoker'] = df['smoker'].map({'no':0,'yes':1})
sns.heatmap(df.drop('region',axis = 1).corr(),annot=True)
print('''As we can see from the correlation matrix , the impoertant points to note 

Age does not have a significant impact on other aspects but a little impact on the charges
If your age is more you may have to pay more for an insurance

BMI does not have a significant impact on other aspects but a little impact on the charges
If your bmi is more you may have to pay more for an insurance

Sex has no significant impact

Smoking has the highest impact , there is an 80% chance of you paying more if you are an smoker
''')


# In[ ]:




