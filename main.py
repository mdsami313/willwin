import streamlit as st
from PIL import Image

def main():
    # Sidebar Navigation
    # st.sidebar.title("Nav")
    menu = ["Home", "Products", "About"]
    choice = st.sidebar.radio("",menu)

    if choice == "Home":
        home_page()
    elif choice == "Products":
        products_page()
    elif choice == "About":
        about_page()

def home_page():
    # st.set_page_config(page_title="", page_icon="🌟", layout="wide")
    st.title("WILLWIN ENTERPRISES")
    st.subheader("QUALITY, PERFECTION & RELIABILITY DELIVERED")


    st.write("""
    In an industry that demands highly competitive and precision based products willwin enterprises committed to excellent service, up to date technological upgradation, state of the art infrastructure and highly qualified human resources. we supplied machined parts ready to assemble components for valves & pumps industry, tractor industry, food industry & material handling industry, crane's, hoist’s, elevator part’s, all types of compressor spares, agriculture implements, cement & sugar industry, flour & rice mill machinery spares in graded cast iron, s.g. iron, alloy steel castings, ferrous & non ferrous machined components, specialised in “v” groove motor pulley’s & flywheels.
             

    """,)

    st.write("""
    #### VISION:
    TO SUPPLY QUALITY PRODUCTS BY INCORPORATING THE NEEDS AND REQUIREMENTS OF CUSTOMER

    #### MISSION:
    TO ACHIEVE HIGHEST CUSTOMER SATISFACTION BY CONTINUAL IMPROVEMENT OF THE PROCESSES AND INCREASING EFFECTIVENESS OF QUALITY MANAGEMENT SYSTEM BY EMPLOYEE INVOLVEMENT

    #### CULTURE:
    CUSTOMER SATISFACTION QUALITY EXCELLENCE
             

    """)

    st.write("""
    #### QUALITY POLICY:
    WE AT WILLWIN ENTERPRISES COMMITTED FOR, SUPPLIER OF PRECISION MACHINED COMPONENTS AND SUB ASSEMBLIES WITH HIGH QUALITY TO MEET CUSTOMERS DESIRED REQUIREMENTS UPTO THEIR FULLEST SATISFACTION AT ALL TIMES. CONTINUALLY IMPROVING ON THE QUALITY MANAGEMENT SYSTEM WITH FOCUS ON THE GROWTH IN BUSINESS. DEVELOPING THE SKILLS OF ALL MEMBERS AND WORKERS OF WILLWIN ENTERPRISES LEADING TO THEIR INDIVIDUAL GROWTH & WELLBEINGS.
             

    """)



    st.write("""
    #### PRODUCT RANGE:
    - MATERIAL HANDLING EQUIPMENT'S
    - CRANES SPARES
    - HOISTS SPARES
    - ELEVATOR PART'S
    - AUTOMOBILE PART'S
    - ACTUATOR GEAR BOXES
    - ALL TYPES OF VALVES
    - PUMPS COMPONENTS
    - ALL TYPES OF COMPRESSORS SPARES
    - AGRICULTURAL IMPLEMENTS
    - FOOD INDUSTRY SPARES
    - TRACTOR PARTS
    - CEMENT PLANTS PARTS
    - SUGAR PLANTS PARTS
    - FLOUR & RICE MILL MACHINERY SPARES ETC.
    """)

def products_page():
    st.title("Products Gallery")

    # Updated grid for product images
    image_paths = ["image1.png", "image2.png", "image3.png", "image4.png", "image5.png", "image6.png", "image7.png", "image8.png", "image9.png", "image10.png", "image11.png"]

    for i in range(0, len(image_paths), 2):
        cols = st.columns(2)
        for col, img_path in zip(cols, image_paths[i:i+2]):
            with col:
                image = Image.open(f"images\\{img_path}")
                resized_image = image.resize((250, 250))
                st.image(resized_image, use_column_width=True)

def about_page():
    st.title("About Us")

    st.write("""
    WILLWIN ENTERPRISES IS A PROPRIETORSHIP ESTABLISHED IN 2018, MANAGED BY MR. ABDULHAMID SHAIKH AND HAS A GOOD REPUTATION IN THE FIELD OF FOUNDRY AS WELL AS MACHINING OF PRECISION MACHINED PARTS READY TO ASSEMBLY COMPONENTS FOR VALVES & PUMPS INDUSTRY, TRACTOR INDUSTRY, FOOD INDUSTRY & MATERIAL HANDLING INDUSTRY, CRANE'S, HOIST’S, ELEVATOR PART’S, ALL TYPES OF COMPRESSOR SPARES, AGRICULTURE IMPLEMENTS, CEMENT & SUGAR INDUSTRY, FLOUR & RICE MILL MACHINERY SPARES IN GRADED CAST IRON, S.G. IRON, ALLOY STEEL CASTINGS, FERROUS & NON FERROUS MACHINED COMPONENTS, SPECIALISED IN “V” GROOVE MOTOR PULLEY’S & FLYWHEELS.

    LOCATION: SMART CITY BELGAUM, KARNATAKA STATE, INDIA. BELGAUM IS ONE OF THE MOST PROMISING INDUSTRIAL CENTERS OF KARNATAKA, 150 KMS. (90 MILES) FROM GOA AND ABOUT 500 KMS. (300 MILES) FROM MUMBAI PORT. IT IS WELL CONNECTED BY AIR, RAIL & ROAD.

    TEAM: THE COMPANY HAS WELL-QUALIFIED AND MOTIVATED TEAM OF ENGINEERS AND SKILLED PROFESSIONALS EXPERIENCED IN THE FIELD OF ENGINEERING WITH THE LATEST FACILITIES REQUIRED TO ACHIEVE AND SET GOALS. THE COMPANY TEAM FORCE OF 10-15 PEOPLE.
    """)

    st.write("""
    ### OUR COMMERCIAL DETAILS
    - **GSTIN NO.**: 29DUOPS2994Q1Z3
    - **UAM NO.**: KR04A0026587

    ### BANK DETAILS
    - **BANK NAME**: YES BANK LTD
    - **CURRENT ACCOUNT NUMBER**: 054761900000587
    - **IFS CODE**: YESB0000547
    - **BRANCH**: YES BANK LTD, PART GROUND FLOOR, THAKKAR PLAZA, CLUB ROAD, BELGAUM. 590001
    """)

if __name__ == "__main__":
    main()
