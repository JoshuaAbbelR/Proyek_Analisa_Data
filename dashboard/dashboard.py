!pip install matplotlib
!pip install seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')
all_df = pd.read_csv("all_data.csv")

def create_sum_product_df(df):
    sum_product_df = df.groupby("product_category_name_english")["order_item_id"].count().reset_index().sort_values(by="order_item_id", ascending=False)
    return sum_product_df

def create_bycity_df(df):
    bycity_df = df.groupby(by="customer_city").customer_id.nunique().reset_index().sort_values(by="customer_id", ascending=False)
    bycity_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
    return bycity_df

main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                (all_df["order_purchase_timestamp"] <= str(end_date))]

sum_product_df = create_sum_product_df(main_df)
bycity_df = create_bycity_df(main_df)

st.header('E-Commerce Dashboard')

st.subheader('Produk Terbaik dan Terburuk Berdasarkan Penjualan')

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(26, 8))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="order_item_id", 
    y="product_category_name_english", 
    data=sum_product_df.head(5), 
    palette=colors, ax=ax[0]
)
ax[0].set_title("Produk dengan Penjualan Terbaik", loc="center", fontsize=18)

sns.barplot(
    x="order_item_id", 
    y="product_category_name_english", 
    data=sum_product_df.tail(5).sort_values(by="order_item_id", ascending=True), 
    palette=colors, ax=ax[1]
)
ax[1].set_title("Produk dengan Penjualan Terburuk", loc="center", fontsize=18)
ax[1].invert_xaxis()

st.pyplot(fig)

st.subheader('Kota dengan Konsentrasi Pelanggan Terbesar')

fig, ax = plt.subplots(figsize=(10, 5))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="customer_count", 
    y="customer_city", 
    data=bycity_df.head(10), 
    palette=colors_, ax=ax
)
ax.set_title("Top 10 Kota dengan Pelanggan Terbanyak", fontsize=15)

st.pyplot(fig)

st.caption('E-Commerce Joshua - 2024')
