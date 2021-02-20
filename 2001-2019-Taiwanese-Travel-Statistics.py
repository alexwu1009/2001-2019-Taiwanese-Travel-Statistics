import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn ; seaborn.set()

data_report = pd.read_csv('https://gist.githubusercontent.com/ji394python/679a156b429829b9f1a4ff87c7f5b995/raw/7c297cfe89495e8185254ee82b25e1d99c8f7743/dataset.csv')

data_report['country'] = data_report['country'].str.replace('香港', 'HongKong')
data_report['country'] = data_report['country'].str.replace('義大利', 'Italy')
data_report['country'] = data_report['country'].str.replace('德國', 'Germany')
data_report['country'] = data_report['country'].str.replace('法國', 'France')
data_report['country'] = data_report['country'].str.replace('美國', 'USA')
data_report['country'] = data_report['country'].str.replace('加拿大', 'Canada')
data_report['country'] = data_report['country'].str.replace('紐西蘭', 'New Zealand')
data_report['country'] = data_report['country'].str.replace('英國', 'English')
data_report['country'] = data_report['country'].str.replace('澳門', 'Macao')
data_report['country'] = data_report['country'].str.replace('荷蘭', 'Netherlands')
data_report['country'] = data_report['country'].str.replace('越南', 'Vietnam')
data_report['country'] = data_report['country'].str.replace('泰國', 'Thailand')
data_report['country'] = data_report['country'].str.replace('菲律賓', 'Philippines')
data_report['country'] = data_report['country'].str.replace('中國大陸', 'China')
data_report['country'] = data_report['country'].str.replace('印尼', 'Idonesia')
data_report['country'] = data_report['country'].str.replace('澳大利亞', 'Australia')
data_report['country'] = data_report['country'].str.replace('新加坡', 'Singapro')
data_report['country'] = data_report['country'].str.replace('馬來西亞', 'Malaysia')
data_report['country'] = data_report['country'].str.replace('南韓', 'South Korea')
data_report['country'] = data_report['country'].str.replace('南非', 'South Africa')
data_report['country'] = data_report['country'].str.replace('瑞士', 'Switzerland')
data_report['country'] = data_report['country'].str.replace('日本', 'Japan')

first_year = data_report[data_report['date'].str.contains('2001')][['date', 'country', 'value']]
second_year = data_report[data_report['date'].str.contains('2002')][['date', 'country', 'value']]
third_year = data_report[data_report['date'].str.contains('2003')][['date', 'country', 'value']]
forth_year = data_report[data_report['date'].str.contains('2004')][['date', 'country', 'value']]
fifth_year = data_report[data_report['date'].str.contains('2005')][['date', 'country', 'value']]
sixth_year = data_report[data_report['date'].str.contains('2006')][['date', 'country', 'value']]
seventh_year = data_report[data_report['date'].str.contains('2007')][['date', 'country', 'value']]
eighth_year = data_report[data_report['date'].str.contains('2008')][['date', 'country', 'value']]
ninth_year = data_report[data_report['date'].str.contains('2009')][['date', 'country', 'value']]
tenth_year = data_report[data_report['date'].str.contains('2010')][['date', 'country', 'value']]
elevenst_year = data_report[data_report['date'].str.contains('2011')][['date', 'country', 'value']]
twelthrd_year = data_report[data_report['date'].str.contains('2012')][['date', 'country', 'value']]
thirthinth_year = data_report[data_report['date'].str.contains('2013')][['date', 'country', 'value']]
forthinth_year = data_report[data_report['date'].str.contains('2014')][['date', 'country', 'value']]
fifthinth_year = data_report[data_report['date'].str.contains('2015')][['date', 'country', 'value']]
sixteenth_year = data_report[data_report['date'].str.contains('2016')][['date', 'country', 'value']]
seventinth_year = data_report[data_report['date'].str.contains('2017')][['date', 'country', 'value']]
eightinth_year = data_report[data_report['date'].str.contains('2018')][['date', 'country', 'value']]
nintinth_year = data_report[data_report['date'].str.contains('2019')][['date', 'country', 'value']]

# Made a dictionary, one country has one color. It is more convenient to understand. 
colors = {
    'HongKong':'orange',
    'Italy':'green',
    'Germany':'chocolate',
    'France':'royalblue',
    'USA':'coral',
    'Canada':'dodgerblue',
    'New Zealand':'blue',
    'English':'gold',
    'Macao':'lightgreen',
    'Netherlands':'deeppink',
    'Vietnam':'burlywood',
    'Thailand':'goldenrod',
    'Philippines':'peru',
    'China':'red',
    'Idonesia':'sandybrown',
    'Australia':'forestgreen',
    'Singapro':'crimson',
    'Malaysia':'tomato',
    'South Korea':'mediumslateblue',
    'South Africa':'darkgoldenrod',
    'Switzerland':'deepskyblue',
    'Japan':'lightpink'
}

first_year = first_year.groupby('country')['value'].sum()
first_year = pd.DataFrame(first_year).reset_index()
first_year = first_year.sort_values('value', ascending=False)
first_year = first_year.reset_index(drop=True)

x = first_year['country'].values
y = first_year['value'].values

fig, axes = plt.subplots(figsize=(30, 15))
axes = plt.axes()
axes.set_title('2001-2019 Taiwanese Travel Statistics', fontsize=40)
axes.set_xlabel('Countries', fontsize=20)

axes.set_ylabel('Number of Traveling Population', fontsize=20)
axes.set_yticks(np.arange(0, 5000000, 1000000))
axes.set_yticklabels(['0', '0.5 million', '1.0 million', '1.5 million', '2.0 million'])
axes.set_ylim(0, 5000000)
axes.bar(x, y, color=[colors[x] for x in first_year['country']]) 
for xx, yy in enumerate(y):                                      
    axes.text(xx, yy, '{:,}'.format(int(yy)), ha='center', va='bottom', fontsize=13)
plt.show()
