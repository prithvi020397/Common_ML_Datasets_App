import os
import streamlit as st 

# EDA Pkgs
import pandas as pd 

# Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 

def main():
    """ Common ML Dataset Explorer """
    st.title("Common ML Dataset Explorer")
    st.subheader("Datasets For ML Explorer with Streamlit")


    html_temp = """
    <div style ="background-color:tomato;"><p style="color:white;font-size:50px">Streamlit is awesome</p></div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)


    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select A file",filenames)
        return os.path.join(folder_path,selected_filename)

    filename = file_selector()
    st.info("You selected {}".format(filename))

        # Read Data
    df = pd.read_csv(filename)
        # Show Dataset
    if st.checkbox("Show datasets"):
     number=st.number_input("Number of rows to view",5,10)
     st.dataframe(df.head(number))


        # Show Columns
    if st.button("Columns names"):
        st.write(df.columns)
        # Show Shape
    if st.checkbox(" SHape datasets"):
        st.write(df.shape)
        data_dim =st.radio("Show Dimmenisons By",("Rows","Columns") )
        if data_dim =='Rows':
            st.text("Number of rows")
            st.write(df.shape[1])

        elif data_dim =='Columns':
            st.text("Number of columns")
            st.write(df.shape[1])

        else:
            st.write(df.shape)
        
        # Select Columns
        if st.checkbox("columnsto show"):
            all_coloums = df.columns.tolist()
            selected_coloums=st.multiselect("Select",all_coloums)
            new_df = df[selected_coloums]
            st.dataframe(new_df)
        # Show Values
        if  st.button("Values Count"): 
            st.text("Value counts by Target /Class")
            st.write(df.iloc[:,-1].value_counts())
        # Show Datatypes
        if  st.button("Data types"): 
            st.text("Data types")
            st.write(df.dtypes)
        # Show Summary
        if st.checkbox("Summary"):
            st.text("Summary")
            st.write(df.describe().T)


        ## Plot and Visualization
        st.subheader("Data Visualization")
        #Correlation
        #Seaborn
        if st.checkbox("Correlation Plot [Seaborn]"):
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()

        #Count Plots
        #Pie charts
        if st.checkbox("Pie Chart"):
            all_coloums_names =df.columns.tolist()
            if st.button("Generate Plot"):
                st.success("Generate a Pie Plot")
                st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
                st.pyplot()


        #Count Plot
        if  st.checkbox("Count PLOT"):
            st.text("value by Target")
            all_coloums_names =df.columns.tolist()
            primary_col = st.selectbox("primary columns to groupby",all_coloums_names)
            selected_coloums_names = st.multiselect("selected_coloums",all_coloums_names)
            if st.button("Plot"):
                st.text("Generate Plot")
                if selected_coloums_names:
                    vc_plot =df.groupby(primary_col)[selected_coloums_names].count()
                else:
                    vc_plot =df.iloc[:,-1].value_counts()
                st.write(vc_plot.plot(kind="bar"))
                st.pyplot()


        #Customizable
        st.subheader("Customizable Plot")
        all_columns_names = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

        if st.button("Generated Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))


            #PLots by Streamlist
            if type_of_plot == "area":
                cust_data =df[selected_coloums_names]
                st.area_chart(cust_data)

            elif type_of_plot == "bar":
                cust_data =df[selected_coloums_names]
                st.bar_chart(cust_data)


            elif type_of_plot == "line":
                cust_data =df[selected_coloums_names]
                st.line_chart(cust_data)

                #custom plots
            elif type_of_plot:
                cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
                st.write(cust_plot)
                st.pyplot() 


        if st.button("Thanks"):
             st.balloons()

    st.sidebar.header("About App")
    st.sidebar.info("A Simple EDA App for Exploring Common ML Dataset")

    st.sidebar.header("Get Datasets")
    st.sidebar.markdown("[Common ML Dataset Repo]("")")

    st.sidebar.header("About")
    st.sidebar.info("Prithvi Sai")
    st.sidebar.text("Built with Streamlit")
    st.sidebar.text("Maintained by Prithvi Sai")









if __name__ == "__main__":
  main()




       






    