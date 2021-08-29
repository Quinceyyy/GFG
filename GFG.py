
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('dataset_gfg.csv')

df.replace(',','', regex=True, inplace=True)

cols = ['Spend in $','Visits','Orders','Revenue in $']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

df.loc[df['Channel name'].str.startswith('App install network'), 'Channel Type'] = 'App install network'
df.loc[df['Channel name'].str.startswith('Web channel'), 'Channel Type'] = 'Web channel'
df.loc[df['Paid/Free'] == 'Free', 'Channel Type'] = 'Free'
df = df.set_index('Week')

df['CR'] = df['Orders']/df['Visits']*100
df['ABS'] = df['Revenue in $']/df['Orders']
df['CIR'] = df['Spend in $']/df['Revenue in $']
df


df_grouped = df.groupby(by=['Channel Type','Week']).sum().reset_index()


df_grouped['CR'] = df_grouped['Orders']/df_grouped['Visits']*100
df_grouped['ABS'] = df_grouped['Revenue in $']/df_grouped['Orders']
df_grouped['CIR'] = df_grouped['Spend in $']/df_grouped['Revenue in $']

df_grouped = df_grouped.set_index('Week')
df_grouped


f, axs = plt.subplots(4,3,figsize=(15,15))
f.tight_layout(pad=5.0)
plt.subplot(4,3,1)
plt.gca().title.set_text('Conversion Rate (CR)')
plt.gca().set_ylabel('App Network', size='large')
plt.xticks([42,43])
df[df['Channel Type']=='App install network'].groupby('Channel name')['CR'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,2)
plt.gca().title.set_text('Average Basket Size (ABS)')
plt.xticks([42,43])
df[df['Channel Type']=='App install network'].groupby('Channel name')['ABS'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,3)
plt.gca().title.set_text('Cost to Income Ratio (CIR)')
plt.xticks([42,43])
df[df['Channel Type']=='App install network'].groupby('Channel name')['CIR'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,4)
plt.gca().set_ylabel('Web Channel', size='large')
plt.xticks([42,43])
df[df['Channel Type']=='Web channel'].groupby('Channel name')['CR'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,5)
plt.xticks([42,43])
df[df['Channel Type']=='Web channel'].groupby('Channel name')['ABS'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,6)
plt.xticks([42,43])
df[df['Channel Type']=='Web channel'].groupby('Channel name')['CIR'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,7)
plt.gca().set_ylabel('Free' , size='large')
plt.xticks([42,43])
df[df['Channel Type']=='Free'].groupby('Channel name')['CR'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,8)
plt.xticks([42,43])
df[df['Channel Type']=='Free'].groupby('Channel name')['ABS'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,9)
plt.xticks([42,43])
df[df['Channel Type']=='Free'].groupby('Channel name')['CIR'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 

plt.subplot(4,3,10)
plt.gca().set_ylabel('Overall' , size='large')
plt.xticks([42,43])
df_grouped.groupby('Channel Type')['CR'].plot(kind='line', legend=True, ax=plt.gca(),use_index=True) 
plt.subplot(4,3,11)
plt.xticks([42,43])
df_grouped.groupby('Channel Type')['ABS'].plot(kind='line', legend=True, ax=plt.gca()) 
plt.subplot(4,3,12)
plt.xticks([42,43])
df_grouped.groupby('Channel Type')['CIR'].plot(kind='line', legend=True, ax=plt.gca()) 
plt.show()


