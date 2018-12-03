
# coding: utf-8

# ## imports for Python, Pandas, etc.

# In[1]:


import pandas as pd
import json
from pandas.io.json import json_normalize
import operator
import itertools
import seaborn as sns


# ****
# ## JSON exercise
# 
# Using data in file 'data/world_bank_projects.json' and the techniques demonstrated above,
# 1. Find the 10 countries with most projects
# 2. Find the top 10 major project themes (using column 'mjtheme_namecode')
# 3. In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

# # 1. Find the 10 countries with most projects.
# + First, I loaded the jason file onto Python then used pandas to convert it to a DataFrame.
# + To find out top 10 countries with most projects, I checked out column names and looked for the one I needed to use. The column "countryname" is the one we need.
# + Then I used for loop to count them
# + So the top 10 countries are: ("People's Republic of China", 19), ('Republic of Indonesia', 19), ('Socialist Republic of Vietnam', 17), ('Republic of India', 16), ('Republic of Yemen', 13), ('Kingdom of Morocco', 12), ('Nepal', 12), ("People's Republic of Bangladesh", 12), ('Republic of Mozambique', 11), ('Africa', 11).
# + Each tuple contains country name and number of projects with People's of Republic of China having the most projects.
# + The code is provided below.

# In[2]:


json_df = pd.read_json('Desktop/data_wrangling_json/data_wrangling_json/data/world_bank_projects.json')
print(json_df.shape)
print(json_df.columns) #find countryname to use

country_count = {}
country_list = list(json_df['countryname'])

for country in country_list:
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1

sorted_country = sorted(country_count.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_country[:10])


# # 2. Find the top 10 major project themes (mjtheme_namecode column).
# + First, I also converted the column into a list. Since, there are multiple lists in the list, I created another clean list by using extend method.
# + Then I used for loop to count the themes. Here I used the keyword "code" instead of "name" because there are missing values in "name".
# + The top 10 themes are: ('11', 250), ('10', 216), ('8', 210), ('2', 199), ('6', 168), ('4', 146), ('7', 130), ('5', 77), ('9', 50), ('1', 38). Each tuple contains theme code and number of counts.
# + According to the result, code 11 theme is the most popular with 250 projects.
# + You can see the code names in the questions below.

# In[3]:


print(json_df['mjtheme_namecode'].head(10))

mjtheme_list = list(json_df['mjtheme_namecode'])
mjtheme_list_clean = []

for entry in mjtheme_list:
    mjtheme_list_clean.extend(entry)
    
theme_count = {}
for i in range(len(mjtheme_list_clean)):
    if mjtheme_list_clean[i]['code'] in theme_count:
        theme_count[mjtheme_list_clean[i]['code']] += 1
    else:
        theme_count[mjtheme_list_clean[i]['code']] =1

sorted_theme = sorted(theme_count.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_theme[:10])


# # 3. Create a dataframe with the missing names filled in name.
# + First, I used json.load to read this json file as a text.
# + Then I used json_normalize function to create a DataFrame with two columns: code and name.
# + We can see that there are missing values in name.
# + I figured out what each code stands for and used for loop to replace any missing value with its corresponding name
# + Please see the DataFrame below.

# In[4]:


json_data = json.load(open('Desktop/data_wrangling_json/data_wrangling_json/data/world_bank_projects.json'))
theme_df = json_normalize(json_data, 'mjtheme_namecode')
print(theme_df.head())
print(theme_df.shape)

new_theme = theme_df

print(theme_df.loc[theme_df['code'] == '1'].head(1))
print(theme_df.loc[theme_df['code'] == '2'].head(1))
print(theme_df.loc[theme_df['code'] == '3'].head(1))
print(theme_df.loc[theme_df['code'] == '4'].head(1))
print(theme_df.loc[theme_df['code'] == '5'].head(1))
print(theme_df.loc[theme_df['code'] == '6'].head(1))
print(theme_df.loc[theme_df['code'] == '7'].head(1))
print(theme_df.loc[theme_df['code'] == '8'].head(1))
print(theme_df.loc[theme_df['code'] == '9'].head(1))
print(theme_df.loc[theme_df['code'] == '10'].head(1))
print(theme_df.loc[theme_df['code'] == '11'].head(2))

for i in range(1499):
    if new_theme.code.iloc[i] == '1':
        new_theme.name[i] = 'Economic management'
    elif new_theme.code.iloc[i] == '2':
        new_theme.name[i] = 'Public sector governance'
    elif new_theme.code.iloc[i] == '3':
        new_theme.name[i] = 'Rule of law'
    elif new_theme.code.iloc[i] == '4':
        new_theme.name[i] = 'Financial and private sector development'
    elif new_theme.code.iloc[i] == '5':
        new_theme.name[i] = 'Trade and integration'
    elif new_theme.code.iloc[i] == '6':
        new_theme.name[i] = 'Social protection and risk management'
    elif new_theme.code.iloc[i] == '7':
        new_theme.name[i] = 'Social dev/gender/inclusion'
    elif new_theme.code.iloc[i] == '8':
        new_theme.name[i] = 'Human development'
    elif new_theme.code.iloc[i] == '9':
        new_theme.name[i] = 'Urban development'
    elif new_theme.code.iloc[i] == '10':
        new_theme.name[i] = 'Rural development'
    elif new_theme.code.iloc[i] == '11':
        new_theme.name[i] = 'Environment and natural resources management'
        
print(new_theme.head(10))


# # Revision to 1.
# - This time, instead of writing loops, I used .value_counts() and it yields the same results

# In[10]:


json_df['countryname'].value_counts()[:10]


# # Revision to 2.
# - This time, instead of writing loops, I once again use .value_counts(). Since there are dicts nested in that column, we must reolad the json file using normalize.
# - To compare the corresponding theme names, we can find them above listed already.
# - And it yields the same results as well.

# In[17]:


themes = json_normalize(json_data, 'mjtheme_namecode')
print(themes.head())
themes['code'].value_counts()[:10]

