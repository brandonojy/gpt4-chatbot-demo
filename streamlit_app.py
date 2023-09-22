#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import numpy as np
import pprint
import pandas as pd
import time
# import plotly.graph_objects as go

# empty dataframe hidden until user inputs data
df = pd.DataFrame()


# In[7]:


st.title('CSE Calcul ASC 2023')
st.write('')


# In[ ]:


# add some space between photo and instructions
st.write('')
st.subheader('vous pouvez saisir vos informations pour le calcul ASC')


# In[9]:


# Function to convert 
copper = 1/100
silver = 1/10
electrum = 1/2
gold = 1
platinum = 10


def getCoins(coins, amount, coinIndex = 0):
    
    amount = float(amount)
    if amount == 0:
        return [] # all done! You did it!
    if coinIndex >= len(coins):
        return None # don't have enough money / coins
    
    # names of coins to print later
    coinNames = ['', 'Copper', 'Silver']
    
    # start calculations
    coin = coins[coinIndex] # 1= gold, 2= platinum, ...
    coinIndex += 1 
    # First, take as may as possible from first listed coin (will start at Index 1 (gold))
    canTake = int(min(amount / coin['value'], coin['count']))
    
    #Reduce the number taken from this coin until success
    for count in np.arange(canTake, -1.0, -1):  # take away 1 until count reaches 0
        
        # Recurse to decide how many to take from next coin
        change = getCoins(coins, amount - coin['value'] * count, coinIndex)
        if change != None: # Success! We are done!
            if count: # Register this number for this coin
                return change + [{'Coin Name': coinNames[coinIndex], 'Amount': int(count)}]
            return change


# In[ ]:


# create placeholders to clear inputs when clicking "start over" button
placeholder_c = st.empty()
placeholder_s = st.empty()



# In[9]:


# have user input the amount they have for each coin

userNumCopper = placeholder_c.number_input('Revenu de reference 2023 (sur les revenus 2022): ', min_value= 0)
userNumSilver = placeholder_s.number_input('Nombre de parts ', min_value= 1)



# In[ ]:


# tell user how much they have in gold pieces

totalGold = (userNumCopper / userNumSilver / 12) 
totalGold = round(totalGold)

st.subheader(f'Votre Quotient Familial {totalGold:,d} .')


# In[ ]:


st.write('')

if totalGold > 2200:
    st.write('Vous avez l\'enveloppe standard de 183 euros.')
    st.write('Pas besoin de venir nous voir :) ')
elif totalGold <= 2200:
   st.write('Vous avez une enveloppe de 250 euros.')
elif numCoins <= 1700:
    st.write('Vous avez une enveloppe de 350 euros.')
elif numCoins <= 1200:
    st.write('Vous avez une enveloppe de 450 euros.')
else: 
    st.write('Vous avez une enveloppe bonifiée.')
    st.write('Vous pouvez venir nous voir!! :) ')


# In[ ]:


# ask how much they are trying to spend
st.header('Gold you would like to spend')
placeholder_u = st.empty()
userSpendGold = placeholder_u.number_input('How much gold do you want to spend? ', min_value= 0, value= 0)


# In[8]:


if userSpendGold > totalGold:
    st.write('You do not have enough money. Sorry!')
    st.write(f'Total Gold: {totalGold}')
    st.write(f'Gold you need: {userSpendGold}')
    
else:
# code below works fast but prioritizes gold and plat first
#     coins = [

#     { "value":  silver, "count":  userNumSilver },
#     { "value":  copper, "count": userNumCopper } 
#     ]
    coins = [
    { "value":  copper, "count": userNumCopper },
    { "value":  silver, "count":  userNumSilver },

    ]
    
    
    result = getCoins(coins, userSpendGold)
    
    df = pd.DataFrame(result)
    # don't show index numbers?
    df.index = [''] * len(df)


# In[ ]:


numCoins = userNumCopper + userNumSilver
if numCoins == 0:
    st.write('')
elif numCoins >= 5000:
    st.write('Looks like your massive heap of coins caught the eyes of a dragon. Please be patient for your total as we distract the dragon.')
elif numCoins >= 4000:
    st.write('Oh no. A kobold ran off with a bag of your coins. '     'Please be patient while we get it back and determine your total.')
elif numCoins >= 3000:
    st.write("Whoa! Our goblins aren't the brightest, so it may take them a while to count.")


# In[5]:


# show table after data is entered
table_placeholder = st.empty()


if not df.empty:
    table_placeholder.table(df)
    # create plotly table without index
#     fig = go.Figure(data= [go.Table(
#         header = dict (values = list(df.columns)), 
#         cells = dict(values= [df['Coin Name'], df['Amount']]))
#         ])
#     fig.update_layout(margin = dict(l= 20, r= 20, t= 20, b= 0))
#     table_placeholder.plotly_chart(fig)
    
    


# In[ ]:


# create dividing line to separate calculations from reset
st.write('-------------------------')


# In[ ]:


# create columns to right align restart button
col1, col2, col3 = st.columns([1,1,.5])
click_clear = col3.button('Start Again')

# set fields back to 0 when clicking button
if click_clear:

    userNumCopper = placeholder_c.number_input('Enter number of Copper: ', 
                                               min_value= 0, value= 0, key= 'redo')
    userNumSilver = placeholder_s.number_input('Enter number of Silver: ', 
                                               min_value= 0, value= 0, key= 'redo1')

    col3.write('The values have been reset')
    st.balloons()


# In[10]:


### Try to get progress bar to work
# def get_results(coins, userSpendGold):
#     # start progress bar
# #     my_bar = st.progress(0)
    
# #     for percent_complete in range(100):
# #         time.sleep(0.1)
# #         my_bar.progress(percent_complete + 1)
    
#     result = getCoins(coins, userSpendGold)
#     wait_message = col_3.text('A goblin ran off with your gold. Hold please while we get it back.')
# #     df = pd.DataFrame(result)
# #     # don't show index numbers?
# #     df.index = [''] * len(df)
#     return result


# In[ ]:


# try to get radio button to work
# radio button to select emcumberance or not
# encumb = st.radio(
#     'With or without encumberance?', 
#     ('Encumbered - get rid of as many coins and weight as possible', 
#      "UnEncumbered - weight doesn't matter and you just want the results fast"))


# In[ ]:


# FUTURE FEATURES
# table as plotly table
# "Run" button so whole page isn't run when user hits 'Enter' to get table
# create wait message / progress bar / spinner while table is being calculated / created


# In[ ]:


# terminal 
# jupyter nbconvert   --to script Streamlit_code.ipynb
# streamlit run app.py
