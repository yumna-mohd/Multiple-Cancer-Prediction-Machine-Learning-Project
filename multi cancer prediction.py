# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:52:10 2024

@author: taiga
"""


#importing libraries

import os #used to create file paths
import pickle #used to load previously saved machine learning models 
import streamlit as st #used to create the web-based user interface for the cancer prediction system
from streamlit_option_menu import option_menu #used to create an option menu with icons in the Streamlit sidebar


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the lung cancer model using the full path
lung_cancer_model_path = os.path.join(script_dir, "Saved Models", "lung_cancer_model.sav")
lung_cancer_model = pickle.load(open(lung_cancer_model_path, "rb"))

# Loading the breast cancer model using the full path
breast_cancer_model_path = os.path.join(script_dir, "Saved Models", "breast_cancer_model.sav")
breast_cancer_model = pickle.load(open(breast_cancer_model_path, "rb"))

# Loading the prostate cancer model using the full path
prostate_cancer_model_path = os.path.join(script_dir, "Saved Models", "prostate_cancer_model.sav")
prostate_cancer_model = pickle.load(open(prostate_cancer_model_path, "rb"))

#----------------------------------------------------------------------------------------------------------------

# Sidebar for navigation
with st.sidebar:  
    selected = option_menu('Multiple Cancer Prediction System',
                           # Adding the menu options
                           ['Home', 'Lung Cancer', 'Breast Cancer', 'Prostate Cancer'],
                           
                           # Adding the icons to the submenu options
                           icons=['house-door', 'lungs', 'gender-female', 'gender-male'],
                           
                           # Setting the default index to 0
                           default_index=0)


    
#----------------------------------------------------------------------------------------------------------------
    
#Introduction page
if (selected == 'Home'):
    
    # Setting the desired width
    image_width = 500
     
    #setting the title
    new_title = '<p style="font-family:Georgia; color:#00FFFF; font-size: 34px;">Welcome to Multi Cancer Detection</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
    # Instructions
    st.markdown("""
    <div style='visibility: visible;display:flex'>
        <p style="font-size:0.8rem;">
            Guidance: This application empowers you to identify three prevalent types of cancer: lung cancer, breast cancer, and prostate cancer. Through this tool, users can perform diagnostic predictions for these specific cancer types. Simply select the cancer category of interest, input the relevant data, and click the corresponding button to obtain accurate results.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    
    #adding the image gif
    image_file_path = os.path.join(script_dir, "hospital.gif")
    image_file = open(image_file_path,'rb')

    image_bytes = image_file.read() 

    st.image(image_bytes,width=image_width)
    
    #adding the background image 
    def set_bg_from_url(url, opacity=1):
        
        #adding and styling the footer text
        footer = """
        
        <footer>
            <div style='visibility: visible;display:flex'>
                <p style="font-size:1.1rem;font-family:Georgia; color:#00FFFF">
                    Made by Yumna Muhammad Shahid Shah
                </p>
            </div>
        </footer>
    """
        st.markdown(footer, unsafe_allow_html=True)
        
        # Set background image using HTML and CSS
        st.markdown(
            f"""
            <style>
                body {{
                    background: url('{url}') no-repeat center center fixed;
                    background-size: cover;
                    opacity: {opacity};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

    # Set background image from URL
    set_bg_from_url("https://i.pinimg.com/originals/b8/23/e3/b823e38cc01fdb9278b6f7faa2feda6d.gif", opacity=0.875)
    

#----------------------------------------------------------------------------------------------------------------  
    
#Lung Cancer prediction page
if (selected == 'Lung Cancer'):
    
    #page title
    #st.title('Lung Cancer Detection')
    new_title = '<p style="font-family:Georgia; color:#00FFFF; font-size: 34px;">Lung Cancer Detection</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
    # Instructions
    st.markdown("""
    <div style='visibility: visible;display:flex'>
        <p style="font-size:0.8rem;">
            Instructions: Input values for all parameters except age, assigning either 1 (representing No) or 2 (representing Yes) in the respective fields. Afterward, click the button to obtain the results.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        AGE = st.text_input('Age')
    
    with col2:
        SMOKING = st.text_input('Smoking')
        
    with col3:
        YELLOW_FINGERS = st.text_input('Blood Pressure Level')
    
    with col4:
        
        ANXIETY = st.text_input('Skin Thickness level')
    
    with col1:
        PEER_PRESSURE = st.text_input('Insulin level')
        
    with col2:
        CHRONIC_DISEASE = st.text_input('BMI value')
        
    with col3:        
        FATIGUE  = st.text_input('Fatigue')
    
    with col4:        
        ALLERGY = st.text_input('Age of the person')
    
    with col1:        
        WHEEZING  = st.text_input('Wheezing')
        
    with col2:       
        ALCOHOL_CONSUMING = st.text_input('Alcohol Consuming')
        
    with col3:
        COUGHING = st.text_input('Coughing')
    
    with col4:
        SHORTNESS_OF_BREATH = st.text_input('Shortness of Breath')
        
    with col1:
        SWALLOWING_DIFFICULTY = st.text_input('Swallowing dificulty')
        
    with col2:        
        CHEST_PAIN  = st.text_input('Chest pain')
            
    
    #code for predicting lung cancer
    lung_cancer_diagnosis = ''
    
    #creating a button for lung cancer prediction    
    if st.button('Lung Cancer Test Result'):
        lung_cancer_prediction = lung_cancer_model.predict([[AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING,SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN ]])
        
        if (lung_cancer_prediction[0]=='NO'):
            lung_cancer_diagnosis = 'The person does not have lung cancer.'
        else:
            lung_cancer_diagnosis = 'The person has lung cancer.'
            
    st.success(lung_cancer_diagnosis)  
    
    
    #adding the background image 
    def set_bg_from_url(url, opacity=1):
        # Set background image using HTML and CSS
        st.markdown(
            f"""
            <style>
                body {{
                    background: url('{url}') no-repeat center center fixed;
                    background-size: cover;
                    opacity: {opacity};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )
           
    # Set background image from URL
    set_bg_from_url("https://t4.ftcdn.net/jpg/04/24/30/93/360_F_424309320_UkOxg2z3sq7yXwGnWCO6xBXkRI4byhnI.jpg", opacity=0.875)
    
    
#----------------------------------------------------------------------------------------------------------------
       
#Breast Cancer prediction page
if (selected == 'Breast Cancer'):
    
    #page title
    st.title('Breast Cancer Detection')
    
    # Instructions
    st.markdown("""
    <div style='visibility: visible;display:flex'>
        <p style="font-size:0.8rem;">
            Instructions: Input the correct values in the corresponding fields and click the button to obtain the results.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3, col4 = st.columns(4)
    
    
    with col1:
        radius_mean = st.text_input('Radius mean')
    
    with col2:
        texture_mean = st.text_input('Texture mean')
        
    with col3:
        perimeter_mean = st.text_input('Perimeter mean')
    
    with col4:
        
        area_mean = st.text_input('area mean')
    
    with col1:
        smoothness_mean = st.text_input('smoothness mean')
        
    with col2:
        compactness_mean = st.text_input('compactness mean')
        
    with col3:        
        concavity_mean = st.text_input('concavity mean')
    
    with col4:        
        concave_points_mean = st.text_input('concave points mean')
    
    with col1:        
        symmetry_mean  = st.text_input('symmetry mean')
        
    with col2:       
        fractal_dimension_mean = st.text_input('Fractal dimension mean')
        
   
    #code for predicting breast cancer
    Breast_cancer_diagnosis = ''
    
    #creating a button for breast cancer prediction
    
    if st.button('Breast Cancer Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean]])
        
        if (breast_cancer_prediction[0]=='M'):
            Breast_cancer_diagnosis = 'The Breast cancer is Malignant.'
        else:
            Breast_cancer_diagnosis = 'The Breast cancer is Benign.'
            
    st.success(Breast_cancer_diagnosis)   
    
    
    #adding the background image 
    def set_bg_from_url(url, opacity=1):
        # Set background image using HTML and CSS
        st.markdown(
            f"""
            <style>
                body {{
                    background: url('{url}') no-repeat center center fixed;
                    background-size: cover;
                    opacity: {opacity};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )
           
    # Set background image from URL
    set_bg_from_url("https://t4.ftcdn.net/jpg/04/24/30/93/360_F_424309320_UkOxg2z3sq7yXwGnWCO6xBXkRI4byhnI.jpg", opacity=0.875)
    
    
#----------------------------------------------------------------------------------------------------------------   

#Prostate Cancer prediction page
if (selected == 'Prostate Cancer'):
    
    #page title
    st.title('Prostate Cancer Detection')
    
    # Instructions
    st.markdown("""
    <div style='visibility: visible;display:flex'>
        <p style="font-size:0.8rem;">
            Instructions: Input the correct values in the corresponding fields and click the button to obtain the results.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
       
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3, col4 = st.columns(4)
      
    with col1:
        radius = st.text_input('Radius')
    
    with col2:
        texture = st.text_input('Texture')
        
    with col3:
        perimeter = st.text_input('Perimeter')
    
    with col4:
        
        area = st.text_input('Area')
    
    with col1:
        smoothness = st.text_input('Smoothness')
        
    with col2:
        compactness = st.text_input('Compactness')
        
    with col3:        
        symmetry = st.text_input('Symmetry')
    
    with col4:        
        fractal_dimension = st.text_input('Fractal Dimension')
    

    #code for prostate cancer prediction
    Prostate_cancer_diagnosis = ''
    
    #creating a button for prostate cancer prediction
    
    if st.button('Prostate Cancer Result'):
        prostate_cancer_prediction = prostate_cancer_model.predict([[radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension]])
        
        
        if (prostate_cancer_prediction[0]=='M'):
            Prostate_cancer_diagnosis = 'The Prostate cancer is Malignant.'
        else:
            Prostate_cancer_diagnosis = 'The Prostate cancer is Benign.'
            
    st.success(Prostate_cancer_diagnosis)   
    
    #adding the background image 
    def set_bg_from_url(url, opacity=1):
        # Set background image using HTML and CSS
        st.markdown(
            f"""
            <style>
                body {{
                    background: url('{url}') no-repeat center center fixed;
                    background-size: cover;
                    opacity: {opacity};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )
           
    # Set background image from URL
    set_bg_from_url("https://t4.ftcdn.net/jpg/04/24/30/93/360_F_424309320_UkOxg2z3sq7yXwGnWCO6xBXkRI4byhnI.jpg", opacity=0.875)
    









