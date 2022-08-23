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
    type_process=["SOH & IW","Graphics", "Analysis"]
    option=st.sidebar.selectbox("Options:", type_process)

    if option=="SOH & IW":

        st.subheader("STOCK ON HAND")
        data_counted=st.file_uploader("Upload Dataset Stock On Hand (Counted_Data):", type=["csv", "txt", "xlsx"])
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
        
    
        st.subheader("INVENTORY_WAREHOUSE")
        data_expected=st.file_uploader("Upload Dataset Inventory Wirehouse (Expected_Data):", type=["csv", "txt", "xlsx"], key = "uniquecalueofsomesort")
        st.success("Dataset Successfully Loaded")
        if data_expected is not None:
            df_expected=pd.read_csv(data_expected, encoding="ISO-8859-1")
            st.dataframe(df_expected.head(90))

            if st.checkbox("Display quantity of elements in IW"):
                st.write(df_expected.shape)
            
            if st.checkbox("Display quantity of products IW without duplicated data, according to Retail_Product_SKU"):
                st.write(df_expected["Retail_Product_SKU"].nunique())

            if st.checkbox("Display quantity of NULL values according to columns", key = "uniquevalueofsomesort"):
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
        
            if st.checkbox("Display integration between SOH and IW"):
                st.subheader("DISCREPANCY SOH & IW")
                my_columns_selected = ["Retail_Product_Color", "Retail_Product_Level1", "Retail_Product_Level1Name", "Retail_Product_Level2Name", "Retail_Product_Level3Name",
                "Retail_Product_Level4Name", "Retail_Product_Name", "Retail_Product_SKU", "Retail_Product_Size", "Retail_Product_Style", "Retail_SOHQTY"]
                df_A = df_expected[my_columns_selected]
                df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
                df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)
                df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].fillna(0)
                df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].astype(int)
                df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)
                df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]
                df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
                df_discrepancy.loc[df_discrepancy["Diff"]>0, "Overs"] = df_discrepancy["Diff"]
                df_discrepancy.loc[df_discrepancy["Diff"]==0, "Match"] = df_discrepancy["Diff"]
                df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)
                df_discrepancy["Overs"] = df_discrepancy["Overs"].fillna(0).astype(int)
                df_discrepancy["Match"] = df_discrepancy["Match"].fillna(0).astype(int)
                st.dataframe(df_discrepancy.head(60)) 
            

            if st.checkbox("Display products of retail level 1"):
                st.subheader("DISCREPANCY IN PRODUCT TYPE 1")
                my_columns_selected = ["Retail_Product_Color", "Retail_Product_Level1", "Retail_Product_Level1Name", "Retail_Product_Level2Name", "Retail_Product_Level3Name",
                "Retail_Product_Level4Name", "Retail_Product_Name", "Retail_Product_SKU", "Retail_Product_Size", "Retail_Product_Style", "Retail_SOHQTY"]
                df_A = df_expected[my_columns_selected]
                df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
                df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)
                df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].fillna(0)
                df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].astype(int)
                df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)
                df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]
                df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
                df_discrepancy.loc[df_discrepancy["Diff"]>0, "Overs"] = df_discrepancy["Diff"]
                df_discrepancy.loc[df_discrepancy["Diff"]==0, "Match"] = df_discrepancy["Diff"]
                df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)
                df_discrepancy["Overs"] = df_discrepancy["Overs"].fillna(0).astype(int)
                df_discrepancy["Match"] = df_discrepancy["Match"].fillna(0).astype(int)
                df_discrepancy_grouped = df_discrepancy.groupby("Retail_Product_Level1Name").sum()
                st.dataframe(df_discrepancy_grouped.head())       
            




    if option=="Graphics":
        st.subheader("Discrepancy in Graphics")


    if option=="Analysis":
        st.subheader("Conclusion about the currency discrepancy")


if __name__ == '__main__':
    main()
