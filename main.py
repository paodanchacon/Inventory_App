from ast import Nonlocal
import streamlit as st
from PIL import Image
import pandas as pd
st.set_page_config(page_title="Inventory_Discrepancy", page_icon=":mag:", layout="wide")

# ------ HEADER SECTION ------
left_column, right_column = st.columns(2)

with st.container():
    
    st.markdown("***INVENTORY APP***")
    st.title("Expected_Stock Vs Counted_Stock")
    st.subheader("Presentation by: Daniela Chambilla :yellow_heart:")
    image=Image.open("store3.png")
    st.image(image, use_column_width=True)

    st.write("How can you to verify the real amount of missing and suplus equipment in your wharehouse?")
    st.write("The goal is to take action to reduce the quantity of missing equipment, and also to improve the control of the warehouse")

def main():
    type_process=["SOH", "IW", "DISCREPANCY_RESULT"]
    option=st.sidebar.selectbox("Options:", type_process)

    if option=='SOH':
        st.subheader("STOCK ON HAND")
        data_counted=st.file_uploader("Upload Dataset:", type=["csv", "txt", "xlsx"])
        st.success("Dataset Successfully Loaded")
        if data_counted is not None:
            df_counted=pd.read_csv(data_counted, encoding="ISO-8859-1")
            st.dataframe(df_counted.head(90))

            if st.checkbox("Display quantity of elements in SOH "):
                st.write(df_counted.shape)
            
            if st.checkbox("Display quantity of products SOH without duplicated data, according to Retail_Product_SKU"):
                st.write(df_counted["Retail_Product_SKU"].nunique())

            if st.checkbox("Display quantity of products SOH without duplicated data, according to RFID code"):
                st.write(df_counted["RFID"].nunique())

            if st.checkbox("Display quantity of NULL values according to columns"):
                st.write(df_counted.isnull().sum())  

            if st.checkbox("Display all SOH columns"):
                st.write(df_counted.columns)

            if st.checkbox("Display some selected SOH columns"):
                selected_columns=st.multiselect("Select important SOH columns:", df_counted.columns)
                df_counted1=df_counted[selected_columns]
                st.dataframe(df_counted1)
            
            if st.checkbox("Display dataset without duplicated and null data according to RFID"):
                df_counted = df_counted.drop_duplicates("RFID")
                st.dataframe(df_counted.head(12)) 
                st.write(df_counted.shape) 
        
    if option=='IW':
        st.subheader("INVENTORY_WAREHOUSE")
        data_expected=st.file_uploader("Upload Dataset:", type=["csv", "txt", "xlsx"])
        st.success("Dataset Successfully Loaded")
        if data_expected is not None:
            df_expected=pd.read_csv(data_expected, encoding="ISO-8859-1")
            st.dataframe(df_expected.head(90))

            if st.checkbox("Display quantity of elements in IW "):
                st.write(df_expected.shape)
            
            if st.checkbox("Display quantity of products IW without duplicated data, according to Retail_Product_SKU"):
                st.write(df_expected["Retail_Product_SKU"].nunique())

            #if st.checkbox("Display quantity of products IW without duplicated data, according to RFID code"):
            #    st.write(df_expected["RFID"].nunique())

            if st.checkbox("Display quantity of NULL values according to columns"):
                st.write(df_expected.isnull().sum())  

            if st.checkbox("Display all IW columns"):
                st.write(df_expected.columns)

            if st.checkbox("Display some selected IW columns"):
                selected_columns=st.multiselect("Select important IW columns:", df_expected.columns)
                df_expected1=df_expected[selected_columns]
                st.dataframe(df_expected1)
            
            if st.checkbox("Display dataset without duplicated and null data according to Retail_Product_SKU"):
                df_expected = df_expected.drop_duplicates("Retail_Product_SKU")
                st.dataframe(df_expected.head(12)) 
                st.write(df_expected.shape) 
if __name__ == '__main__':
    main()
