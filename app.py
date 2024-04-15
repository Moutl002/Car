import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px



st.header('Car Ads Analysis')
st.write('Filter the data below to see the ads by manufacturer')


df = pd.read_csv('C:\\Users\\marqu\\OneDrive\\Documents\\GitHub\\Car\\vehicles_us.csv')



model_car = df['model'].unique() 

selected_model = st.selectbox('Select the model of the car', model_car)

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider('Select the year of the car', min_value=min_year, max_value=max_year, value=(min_year, max_year))


actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df[(df.model == selected_model) & (df.model_year.isin(list(actual_range)))]

df_filtered 

st.header('Price Analysis')
st.write('Lets analyze what influences the price of the cars. Select the variables below to see the results')

list_for_hist = ['transmission', 'fuel', 'type', 'condition']

selected_type = st.selectbox('Select the variable to analyze', list_for_hist)

fig1 = px.histogram(df, x='price', color=selected_type)
fig1.update_layout(title= "<b> Price distribution by {}</b>".format(selected_type))

st.plotly_chart(fig1)


def age_category(x):
    if pd.isnull(x): return 'unknown'
    elif x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
    
    
df['age'] = 2024 - df['model_year']
    
df['age_category'] = df['age'].apply(age_category)

list_for_scatter = ['odometer', 'cylinders', 'is_4wd']

choice_for_scatter = st.selectbox('Price dependency on', list_for_scatter)

fig2 = px.scatter(df, x='price', y=choice_for_scatter, color='age_category', hover_data=['model_year'])
fig2.update_layout(title= "<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)