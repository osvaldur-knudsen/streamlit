
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
pd.options.display.float_format = '{:,.0f}'.format


# Calc functions
def profit():
    df['profit'] = df['income'] - df['expenses']

#Streamlit layout
container1 = st.beta_container()
container2 = st.beta_container()
container3 = st.beta_container()


# Data
np.random.seed(10)
date_rng = pd.date_range(start='12/31/2018', end='12/31/2021', freq='Y').year
data = {'income':np.random.randint(50,100, size=(len(date_rng))),
       'expenses':np.random.randint(0,50, size=(len(date_rng)))}

# Assumptions
rev_growth = container3.slider('select income growth in 2022', min_value=0.0, max_value=0.2, value=0.1)

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

# Streamlit
container1.title('BigCo 2022 budget')
container1.write("Revenues growing at a steady pace")
container2.dataframe(df.transpose())
container2.write('')

option = container2.selectbox(
    'Select line item',
     df.columns)

container2.bar_chart(df[option])

