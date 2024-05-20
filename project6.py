#REQUIRED LIBRARIES
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pickle

#FUNCTION FOR ENCODING THE TOWN VARIABLES TO NUMBER
def encoding_t(town):
    if town=='ANG MO KIO':
        enc_t = int(0)
    elif town=='BEDOK':
        enc_t=int(1)
    elif town=='BISHAN':
        enc_t=int(2)
    elif town=='BUKIT BATOK':
        enc_t=int(3)
    elif town=='BUKIT MERAH':
        enc_t=int(4)
    elif town=='BUKIT PANJANG':
        enc_t=int(5)
    elif town=='BUKIT TIMAH':
        enc_t=int(6)
    elif town=='CENTRAL AREA':
        enc_t=int(7)
    elif town=='CHOA CHU KANG':
        enc_t=int(8)
    elif town=='CLEMENTI':
        enc_t=int(9)
    elif town=='GEYLANG':
        enc_t=int(10)
    elif town=='HOUGANG':
        enc_t=int(11)
    elif town=='JURONG EAST':
        enc_t=int(12)
    elif town=='JURONG WEST':
        enc_t=int(13)
    elif town=='KALLANG/WHAMPOA':
        enc_t=int(14)
    elif town=='LIM CHU KANG':
        enc_t=int(15)
    elif town=='MARINE PARADE':
        enc_t=int(16)
    elif town=='PASIR RIS':
        enc_t=int(17)
    elif town=='PUNGGOL':
        enc_t=int(18)
    elif town=='QUEENSTOWN':
        enc_t=int(19)
    elif town=='SEMBAWANG':
        enc_t=int(20)
    elif town=='SENGKANG':
        enc_t=int(21)
    elif town=='SERANGOON':
        enc_t=int(22)
    elif town=='TAMPINES':
        enc_t=int(23)
    elif town=='TOA PAYOH':
        enc_t=int(24)
    elif town=='WOODLANDS':
        enc_t=int(25)
    elif town=='YISHUN':
        enc_t=int(26)

    return enc_t

#FUNCTION FOR ENCODING THE FLAT TYPE VARIABLES TO NUMBER
def encoding_ft(flt_type):
    if flt_type=='1 ROOM':
        enc_ft = int(0)
    elif flt_type=='2 ROOM':
        enc_ft = int(1)
    elif flt_type=='3 ROOM':
        enc_ft = int(2)
    elif flt_type=='4 ROOM':
        enc_ft = int(3)
    elif flt_type=='5 ROOM':
        enc_ft = int(4)
    elif flt_type=='EXECUTIVE':
        enc_ft = int(5)
    elif flt_type=='MULTI GENERATION':
        enc_ft = int(6)

    return enc_ft

#FUNCTION FOR ENCODING THE FLAT MODEL VARIABLES TO NUMBER
def encoding_fm(flt_model):
    if flt_model=='2-room':
        enc_fm = int(0)
    elif flt_model=='3Gen':
        enc_fm = int(1)
    elif flt_model=='Adjoined flat':
        enc_fm = int(2)
    elif flt_model=='Apartment':
        enc_fm = int(3)
    elif flt_model=='DBSS':
        enc_fm = int(4)
    elif flt_model=='Improved':
        enc_fm = int(5)
    elif flt_model=='Improved-Maisonette':
        enc_fm = int(6)
    elif flt_model=='Maisonette':
        enc_fm = int(7)
    elif flt_model=='Model A':
        enc_fm = int(8)
    elif flt_model=='Model A-Maisonette':
        enc_fm = int(9)
    elif flt_model=='Model A2':
        enc_fm = int(10)
    elif flt_model=='Multi Generation':
        enc_fm = int(11)
    elif flt_model=='New Generation':
        enc_fm = int(12)
    elif flt_model=='Premium Apartment':
        enc_fm = int(13)
    elif flt_model=='Premium Apartment Loft':
        enc_fm = int(14)
    elif flt_model=='Premium Maisonette':
        enc_fm = int(15)
    elif flt_model=='Simplified':
        enc_fm = int(16)
    elif flt_model=='Standard':
        enc_fm = int(17)
    elif flt_model=='Terrace':
        enc_fm = int(18)
    elif flt_model=='Type S1':
        enc_fm = int(19)
    elif flt_model=='Type S2':
        enc_fm = int(20)

    return enc_fm

#FUNCTION FOR LOADING MODEL AND PREDICTING
def predict_selling_price(year, town, flat_type, floor_area_sqm, flat_model, storey_start, storey_end, remaining_lease_year, remaining_lease_month, lease_commence_date):
    year_ip = int(year)
    town_ip = encoding_t(town)
    ft_ip = encoding_ft(flat_type)
    fas_ip = int(floor_area_sqm)
    fm_ip = encoding_fm(flat_model)
    ss_ip = np.log(int(storey_start))
    se_ip = np.log(int(storey_end))
    rly_ip = int(remaining_lease_year)
    rlm_ip = int(remaining_lease_month)
    lcd_ip = int(lease_commence_date)

    with open(r"C:\Users\Jameel Ahamed\Desktop\PYTHON\Singapore_resale_flat_price_prediction.pkl", "rb") as f:
        Model = pickle.load(f)
    
    user_input = np.array([[year_ip, town_ip, ft_ip, fas_ip, fm_ip, ss_ip, se_ip, rly_ip, rlm_ip, lcd_ip]])
    y_pred = Model.predict(user_input)
    price = np.exp(y_pred[0])

    return round(price)

#STREAMLIT PART FOR FRONT END
st.set_page_config(page_title= "Singapore Resale Flat Prices Prediction| By Jameel",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This Application is created by *Jameel*!"""})
st.markdown("<h1 style='text-align: center; color: #FF10AB;'>🏨 SINGAPORE RESALE FLAT PRICES PREDICTION</h1>", unsafe_allow_html=True)

with st.sidebar:
    Option = option_menu('Menu', ["Home","Predictions"], 
                        icons=["house-door-fill","gear"],
                        default_index=0,
                        styles={"nav-link": {"font-size": "30px", "text-align": "centre", "margin": "0px", "--hover-color": "#B51894"},
                                "icon": {"font-size": "25px"},
                                "container" : {"max-width": "3000px"},
                                "nav-link-selected": {"background-color": "#FF10AB"}})
    
if Option=="Home":
    st.markdown("## <span style='color:#FF10AB'>**Technologies Used :**</span> Python, Streamlit, Pandas, Matplotlib.pyplot, EDA, Scikit-learn, Random forest regressor ,Evaluation metrics of regression, Model Deployment, Pickling", unsafe_allow_html=True)
    st.markdown("## <span style='color:#FF10AB'>**Description :**</span> This project aims to develop a machine learning model and deploy it as a user-friendly online application to offer prices forecasts regarding the resale values of apartments in Singapore. The predictive model will utilize historical transactions of resale flats price data, aiming to assist prospective buyers and sellers in assessing the value of a previously resold flat. Various factors influence resale prices, such as location, apartment type, floor area, and lease duration. Providing customers with an estimated resale price based on these factors is one way a predictive model can help address these challenges.", unsafe_allow_html=True)

elif Option=="Predictions":
    col1, col2 = st.columns([4, 5])
    with col1:
        ip_year = st.selectbox("Select the year:",['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])
        ip_town = st.selectbox("Select the Town:", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'LIM CHU KANG', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        ip_flat_type = st.selectbox("Select the Flat Type:", ['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI GENERATION'])
        ip_flat_model = st.selectbox("Select the Flat Model:", ['2-room', '3Gen', 'Adjoined flat', 'Apartment', 'DBSS', 'Improved', 'Improved-Maisonette', 'Maisonette', 'Model A', 'Model A-Maisonette', 'Model A2', 'Multi Generation', 'New Generation', 'Premium Apartment', 'Premium Apartment Loft', 'Premium Maisonette', 'Simplified', 'Standard', 'Terrace', 'Type S1', 'Type S2'])
        ip_lease_commence_date = st.selectbox("Select the Lease Commence Date:", [str(i) for i in range(1966, 2018)])

    with col2:
        ip_remaining_lease_year = st.number_input("Enter the value of Remaining Lease Year: (Min: 42 / Max: 97, if no Remaining Lease Enter 0)")
        ip_remaining_lease_month = st.number_input("Enter the value of Remaining Lease Month: (Min: 0  / Max: 11)")
        ip_floor_area_sqm = st.number_input("Enter the Value of Floor Area in Sqm: (Min:31 / Max: 280)")
        ip_storey_start = st.number_input("Enter the value of Storey Start:")
        ip_storey_end = st.number_input("Enter the value of Storey End:")
        

    submit_button = st.button(label="PREDICT RESALE PRICE")
    st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #FF10AB;
                        color: white;
                        width: 44%;
                    }
                    </style>
                """, unsafe_allow_html=True)

    if submit_button:
        predicted_price = predict_selling_price(ip_year, ip_town, ip_flat_type, ip_floor_area_sqm, ip_flat_model, ip_storey_start, ip_storey_end, ip_remaining_lease_year, ip_remaining_lease_month, ip_lease_commence_date)

        st.markdown(f"""<h2 style='color:#FF10AB;'>The Predicted Price is : $ {predicted_price}</h2>""", unsafe_allow_html=True)