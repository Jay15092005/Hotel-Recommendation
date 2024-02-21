
import numpy as np
import pandas as pd 
import streamlit as st


def recommend_hotels(state, city, Categori , alchi):
    # Filter hotels based on user's preferences
    recommended_hotels = df[(df['State'] == state) & (df['City'] == city) & (df['Category'] == Categori) & (df["Alcohol"]==alchi)]    
    # Sort hotels by alcohol availability
    recommended_hotels = recommended_hotels.sort_values('Total Rooms', ascending=False)
    return recommended_hotels.iloc[:5,:]
# Test the function





df = pd.read_csv("csv_data.csv")
df.head()
unique_values = df.nunique()


# Converting 'Start Date' and 'Expiry Date' to datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'], dayfirst=True)
df['Expiry Date'] = pd.to_datetime(df['Expiry Date'], dayfirst=True)

# Checking the distribution of the 'Alcohol' column
alcohol_distribution = df['Alcohol'].value_counts(dropna=False)

# Checking the range of 'Start Date' and 'Expiry Date'
start_date_range = df['Start Date'].min(), df['Start Date'].max()
expiry_date_range = df['Expiry Date'].min(), df['Expiry Date'].max()

#First of all we need to fill the missing values with 'Unknown'
# Filling missing values in the 'Alcohol' column
df['Alcohol'].fillna('Unknown', inplace=True)

# Verifying the operation
df['Alcohol'].value_counts(dropna=False)



st.header("Hotel Recommendation Systumm")

state_df=(df["State"].unique()).tolist()
state=st.selectbox("Which State In You want To Go",state_df)


city_df=(df[df["State"]==state]["City"].unique()).tolist()
city=st.selectbox("Which City In You want To Go",city_df)


Categories=(df[df["City"]==city]["Category"].unique()).tolist()
Categori=st.selectbox("Which Type of Hotel You Want",Categories)

Alcohole=(df[df["Category"]==Categori]["Alcohol"].unique()).tolist()
alchi=st.selectbox("Type of Alcohole",Alcohole)

if st.button("Suggest Me"):
    st.table(recommend_hotels(state, city, Categori , alchi))
