import streamlit as st

st.set_page_config(page_title="Inventory_Discrepancy", page_icon=":mag:", layout="wide")

# ------ HEADER SECTION ------
left_column, right_column = st.columns(2)

with st.container():
    
    st.subheader("Hi, I am Daniela Chambilla :yellow_heart:")
    st.markdown("***INVENTORY APP***")
    st.title("Expected_Stock Vs Counted_Stock")
    st.subheader("")