
import streamlit as st
import pandas as pd

# Load data
stock_df = pd.read_csv('stock_list.csv')
orders_df = pd.read_csv('orders.csv')

st.set_page_config(page_title='Petals & Quartz Dashboard', layout='wide')
st.title("Petals & Quartz Business Dashboard")

# Sidebar
view = st.sidebar.radio("Go to", ["Inventory", "Sales", "Market Overview"])

if view == "Inventory":
    st.header("📦 Stock Inventory")
    stock_df["Low Stock"] = stock_df["Quantity"].apply(lambda x: "⚠️" if x < 3 else "")
    st.dataframe(stock_df)

    low_stock = stock_df[stock_df["Qty"] < 3]
    if not low_stock.empty:
        st.warning("Some items are low on stock!")
        st.table(low_stock[["Item", "Category", "Qty"]])

elif view == "Sales":
    st.header("🛒 Orders Summary")
    st.dataframe(orders_df)

    st.metric("Total Orders", len(orders_df))
    st.metric("Total VAT Collected", f"R{orders_df['Vat Total'].sum():.2f}")

elif view == "Market Overview":
    st.header("📊 Market Metrics")
    if "client/source" in stock_df.columns:
        summary = stock_df.groupby("client/source")[["Actual Selling Price", "Actual Profit"]].sum()
        st.bar_chart(summary)
    else:
        st.info("No market source data available.")

st.markdown("""---  
Built with ❤️ in Streamlit for Petals & Quartz""")
