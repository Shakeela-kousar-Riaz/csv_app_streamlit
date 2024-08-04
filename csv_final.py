import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set title and name
st.title("Data Analysis and Visualization App")
st.sidebar.markdown("<h3 style='color:red;'>Shakeela Riaz</h3>", unsafe_allow_html=True)

# Upload file
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check file type
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("**Data Preview:**")
    st.write(df.head())

    # Display basic data information
    st.write("**Data Summary:**")
    st.write(df.describe())

    # Column search and details
    st.write("**Column Information:**")
    search_column = st.text_input("Search column name")

    if search_column:
        if search_column in df.columns:
            st.write(f"Column length: {len(df[search_column])}")
            st.write(f"Missing values: {df[search_column].isnull().sum()}")
        else:
            st.write("Column not found.")
    
    # Display DataFrame shape
    st.write("**DataFrame Shape:**")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # Visualization
    st.write("**Data Visualization:**")
    st.sidebar.title("Plot Settings")

    # Select column for x-axis
    x_column = st.sidebar.selectbox("Select X-axis column", df.columns)
    
    # Select column for y-axis
    y_column = st.sidebar.selectbox("Select Y-axis column", df.columns)

    plot_type = st.sidebar.selectbox("Select Plot Type", ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Box Plot", "Relational Plot"])

    if plot_type == "Scatter Plot":
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=x_column, y=y_column)
        st.pyplot(plt)

    elif plot_type == "Line Plot":
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x=x_column, y=y_column)
        st.pyplot(plt)

    elif plot_type == "Bar Plot":
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x=x_column, y=y_column)
        st.pyplot(plt)

    elif plot_type == "Histogram":
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df[x_column], kde=True)
        st.pyplot(plt)

    elif plot_type == "Box Plot":
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=x_column, y=y_column)
        st.pyplot(plt)

    elif plot_type == "Relational Plot":
        plt.figure(figsize=(10, 6))
        sns.relplot(data=df, x=x_column, y=y_column, height=6, aspect=1.5)
        st.pyplot(plt)
