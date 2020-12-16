
import pandas as pd
import numpy as np
from datetime import datetime
pd.options.display.float_format = '{:,.2f}'.format


# Calc functions
def profit():
    df['profit'] = df['income'] - df['expenses']

# Data
np.random.seed(10)
date_rng = pd.date_range(start='12/31/2018', end='12/31/2021', freq='Y').year
data = {'income':np.random.randint(50,100, size=(len(date_rng))),
       'expenses':np.random.randint(0,50, size=(len(date_rng)))}
growth = 0.21

# Assumptions
rev_growth = 0.21

# Dataframe
df = pd.DataFrame(data = data, index = date_rng )
df['profit'] = df['income'] - df['expenses']

# Projection dataframe
df_projection = pd.DataFrame(index = [pd.Timestamp('2022-12-31').year],
                            columns = df.columns)

df_projection.loc[2022, 'income'] =  df['income'].mean()*(1+rev_growth)
df_projection.loc[2022, 'expenses'] = (df['expenses']/df['income']).mean()*df_projection.loc[2022, 'income']


# Append dataframes
df = df.append(df_projection)
profit()
# df = df.columns.apply(pd.to_numeric(df))
df[list(df.columns)] = df[list(df.columns)].apply(pd.to_numeric)
print(df.transpose())

#Streamlit
import streamlit as st

st.title('BigCo 2021 budget')
st.write("Revenues growing at a steady pace")
st.dataframe(df.transpose())

option = st.selectbox(
    'Select line item',
     df.columns)

st.bar_chart(df[option])


