import streamlit as st

st.set_page_config(page_title="Inventory_Discrepancy", page_icon=":mag:", layout="wide")

# ------ HEADER SECTION ------
left_column, right_column = st.columns(2)

with st.container():
    
    
    st.markdown("***INVENTORY APP***")
    st.title("Expected_Stock Vs Counted_Stock")
    from PIL import Image
    st.subheader("Presentation by: Daniela Chambilla :yellow_heart:")
    image=Image.open("store3.png")
    st.image(image, use_column_width=True)

    st.write("How can you to verify the real amount of missing and suplus equipment in your wharehouse?")
    st.write("The goal is to take action to reduce the quantity of missing equipment, and also to improve the control of the warehouse")

