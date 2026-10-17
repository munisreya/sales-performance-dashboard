import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configure the web page
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Performance & Revenue Optimization Dashboard")

# 2. Load the data
@st.cache_data
def load_data():
    return pd.read_csv('data/cleaned/superstore_cleaned.csv')

df = load_data()

# 3. Create a Sidebar Filter (Slicer)
st.sidebar.header("Filter Data")
regions = df['Region'].unique()
selected_regions = st.sidebar.multiselect("Select Region(s):", options=regions, default=regions)

# Filter the dataframe based on sidebar selection
filtered_df = df[df['Region'].isin(selected_regions)]

# 4. Top Row: KPI Cards
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")

st.divider()

# 5. Middle Row: Charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    # Fixed warning here:
    fig1 = px.bar(region_sales, x='Sales', y='Region', orientation='h', color='Region', template="plotly_dark")
    st.plotly_chart(fig1, width='stretch')

with col_right:
    st.subheader("Profit by Category")
    cat_profit = filtered_df.groupby('Category')['Profit'].sum().reset_index()
    # Fixed warning here:
    fig2 = px.bar(cat_profit, x='Category', y='Profit', color='Category', template="plotly_dark")
    st.plotly_chart(fig2, width='stretch')

# 6. Bottom Row: Donut Chart
st.subheader("Impact of Discounts on Profit")
discount_profit = filtered_df.groupby('Discount')['Profit'].sum().reset_index()
# Fixed warning here:
fig3 = px.pie(discount_profit, values='Profit', names='Discount', hole=0.5, template="plotly_dark")
st.plotly_chart(fig3, width='stretch')