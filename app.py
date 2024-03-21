import streamlit as st
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium
import re
import os

  # Information about Temperature Analysis
navigation = st.sidebar.radio("Select a Page", [
                                "Introduction",  "Coding Profile", "Project", "Research", "Course", "AboutMe", "Contact-Enquiry"])


 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
        width: 200%;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Set the page width to 800 pixels


st.markdown(
    """
    <style>
    h1 {
        color: #2e7d32;
    }
    p {
        font-size: 16px;
    }
    .widget-label {
        color: #1976D2;
    }
    </style>
    """,
    unsafe_allow_html=True
)
 
# If access is granted, display the navigation options
if True:    
 
    def Introduction():
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            # Hi I am Lokesh 

            I am a programmer, developer and an ML  enthusiast currently pursuing Master's from IIIT Hyderabad.

            """)

            st.subheader("***Lokesh Sharma***")
            st.write("[M.Tech - CSE] 2022-24")
            st.write(" ***IIIT-Hyderabad***.")

            # Link to Your LinkedIn Profile
            your_linkedin = "[Your LinkedIn Profile](https://www.linkedin.com/in/lokesh-sharma-iiith/)"
            st.markdown(your_linkedin, unsafe_allow_html=True)
            githubcode = "[All Code github links](https://github.com/Lokeshiiith/)"
            st.markdown(githubcode, unsafe_allow_html=True)
            # adding resume
            with open("./images/resume.pdf", "rb") as file:
                resume_bytes = file.read()
            st.download_button(label="Download Resume", data=resume_bytes, file_name="./images/resume.pdf", mime="application/pdf")

        
        with col2:
            st.image("images/lokesh.jpg", use_column_width=True)
            

    if navigation == "Introduction":
        st.title("Introduction Page")
        Introduction()
        # Add text content
        
        # Add buttons
        # if st.button('Download CV'):
            # st.write('CV downloading is initiated...')
        # if st.button('Contact'):
            # st.write('Redirecting to contact page...')
    
    if navigation == "AboutMe":
        about_me_content = """
        # About Me
        Hello, I'm Lokesh Sharma, a passionate and dedicated professional in the field of Computer Science and Engineering.

        My expertise lies in languages like C, C++, Python, and Racket, coupled with hands-on experience in HTML, CSS, JavaScript, and React. Throughout my career, I've worked on a variety of projects ranging from distributed IoT platforms to peer-to-peer file transfer systems, demonstrating my adaptability and problem-solving skills.

        I am currently pursuing a Master's degree in Computer Science from IIIT Hyderabad, where I delved deep into advanced topics like Data Structures and Algorithms, Operating Systems, and Software Systems Development. My academic journey has been complemented by practical experiences, collaborative projects, which have equipped me with a robust skill set and a passion for continuous learning.

        In addition to my technical skills, I am adept at version control systems like Git and GitHub, and I have a strong foundation in system design principles and software development methodologies. I thrive in collaborative environments, where I can leverage my critical thinking abilities and creative problem-solving skills to drive innovation and achieve results.
        """

        # Define the content for the Personal Info section
        personal_info_content = """
        ## Personal Info
        - **Lokesh Sharma**
        - **Phone:** (+91) 8126449754
        - **Email:** lokesh.sharma@students.iiit.ac.in
        - **Personal Email:** lokeshsharma123456@gmail.com
        - **LinkedIn:** [lokesh-sharma-iiith/](https://www.linkedin.com/in/lokesh-sharma-iiith/)
        - **GitHub:** [Github](https://github.com/Lokeshiiith)
        """

        # Define the content for the Technical Skills section
        technical_skills_content = """
        ## Technical Skills
        - Programming Languages: C, C++, Python, Racket
        - Web Dev: HTML-CSS, JS, React
        - Operating Systems: Linux, Windows
        """

        # Define the content for the Relevant Course Work section
        coursework_content = """
        ## Relevant Course Work
        - Data Structures and Algorithms
        - Internals of Application Server
        """

        # Define the content for the Education section
        education_content = """
        ## Education
        - MTech CSE (CGPA: 7.6) - IIIT - HYDE (2022-24)
        - BTech CSE (CGPA: 7.3) - BTKIT Government Engineering College, Dwarahat (2015-19 | Uttarakhand)
        """

        # Define the content for the Hobbies section
        hobbies_content = """
        ## Hobbies
        - Cycling
        - Trekking
        - Yoga
        """
        # Display the content
        st.markdown(about_me_content)
        st.markdown(personal_info_content)
        st.markdown(technical_skills_content)
        st.markdown(coursework_content)
        st.markdown(education_content)
        st.markdown(hobbies_content)
        # Page title
        st.title('Location Tracker')

        # Specify the latitude and longitude coordinates
        latitude = 17.445847275442905
        longitude = 78.34930407132094

        # # Create a Folium map centered at the specified coordinates
        # m = folium.Map(location=[latitude, longitude], zoom_start=15)

        # # Add a marker at the specified location
        # folium.Marker(location=[latitude, longitude], popup='Your Location').add_to(m)

        # # Display the Folium map in the Streamlit app
        # folium_static(m)

    if navigation == "Project":
        st.title("Project")
        githubcode = "[Precipitaion Github code](https://github.com/Lokeshiiith/Climate_change_monitoring_tool/blob/main/PrecipitaionAnalysis.ipynb)"
# First Project
        st.write("## Feb 2023 - Distributed IoT Based App Development Platform")
        st.write("""
            Collaborated on a platform project for deploying, scaling, and monitoring IoT-based
            applications, utilizing oneM2M for efficient and seamless data collection in IoT environments.
            Implemented robust monitoring services and fault-tolerance mechanisms for uninterrupted operation.
            Developed a live tracker of subsystems using React, fetching real-time data from MongoDB.
            
            **Technologies:** Python, Kafka, MongoDB, Azure App Services
            
            **Video Link:** [Watch Video](https://youtu.be/IkRzGv-Mwc4)
            
            **GitHub:** [Project Repository]()
        """)
        st.write("---")  # Line separator

        # Second Project
        st.write("## Oct 2022 - Peer-to-Peer Multiclient File Transfer System")
        st.write("""
            Developed a robust file-sharing system where users can share and download files within
            the groups they belong to. Built tracker and client modules with fault tolerance incorporated
            within the tracker. In addition to reliability, provided an efficient solution, namely, in terms
            of file download rate.
            
            **Techniques harnessed:** Socket Programming, Multithreading, Modular Programming, Extensive use of System Calls
            
            **Video Link:** [Watch Video]()
            
            **GitHub:** [Project Repository]()
        """)
        st.write("---")  # Line separator       

    if navigation == "Research":
        st.write("## Sep 2023 - Climate Change analysis tool for Himalayan belt")
        st.write("""
            Conducted data analysis, clipping, and interpolation on temperature and precipitation data spanning
            60-70 years for new geospatial timberline points using the Aphrodite dataset and Indian Meteorological
            Department dataset. Developed and deployed a user-friendly Streamlit app for visualizing and analyzing
            climate data in the Himalayan region of India. Achieved recognition in the Cloudera and AMD hackathon
            on HackerEarth, securing a place in the top 32 peers out of 2000.
            
            **Technologies:** Python libraries, Interpolation, MATLAB, Streamlit, Azure webservices (CI CD integration with GitHub actions), GIS.
            
            **Video Link:** [Watch Video](https://www.youtube.com/playlist?list=PLyP0ATtJhq9Q9LYWe0Vgsx8DjCwqR550A)
            
            **GitHub:** [Project Repository](https://github.com/Lokeshiiith/Cloudera_project)
            
            **Website Link:** [Link](https://iiithydclimatechangetrend.azurewebsites.net/)
        """)
        st.write("---")  # Line separator
   
    if navigation == "Contact-Enquiry":
        # Define the content for the contact form
        st.markdown("""
            # Contact me for work/general Enquiries
            """)
        def is_valid_email(email):
            # Regular expression for validating email format
            regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return re.match(regex, email)
        def is_valid_mobile_number(phone_number):
    # Regular expression for validating mobile number format (10 digits)
            regex = r'^[0-9]{10}$'
            return re.match(regex, phone_number)
        # Create the contact form using Streamlit components
        with st.form(key='contact_form'):
            col1, col2 = st.columns(2)
            
            with col1:
                client_name = st.text_input('Name')
                client_email = st.text_input('Email address')
                client_phone = st.text_input('Phone Number')
            
            with col2:
                client_inquiry = st.text_area('Inquiry')
                is_client = st.checkbox('I want you to work on project with me')
            
            submit_button = st.form_submit_button(label='Submit')

        # Process the form submission
        if submit_button:
            # You can add your custom logic here
                if not is_valid_email(client_email):
                    st.error('Please enter a valid email address.')
                # Validate mobile number format
                elif not is_valid_mobile_number(client_phone):
                    st.error('Please enter a valid 10-digit mobile number.')
                else:
                    submission_data = f"Name: {client_name}\nEmail: {client_email}\nPhone Number: {client_phone}\nInquiry: {client_inquiry}\nWants to work with you: {is_client}\n\n"
                    log_file_path = 'log.txt'
                    # Check the size of the log file
                    file_size = os.path.getsize(log_file_path)
                    # Convert file size to MB
                    file_size_mb = file_size / (1024 * 1024)  # Convert bytes to MB
                    # Check if file size exceeds 1MB
                    if file_size_mb > 1:
                        st.error('Too many queries already there. Please come back later.')
                    else:
                        with open(log_file_path, 'a') as file:
                            file.write(submission_data)
                        st.success('Your inquiry has been submitted successfully!')

    if navigation == "Course":
        st.title("Courses At IIIT Hyderabad")
        st.write("## Course")
        st.write("This is a course page")


        # Define the relevant coursework
        relevant_courses = [
            "Data Structures and Algorithms",
            "Internals of Application Server",
            "Operating Systems",
            "Database Management System",
            "Advanced Computer Networks",
            "Statistical Methods in AI",
            "Software Systems and Development",
            "Advanced Compiler Design (Racket Programming)",
            "Computer Architecture"
        ]

        # Display details for each course using expandable sections
        for course in relevant_courses:
            # Create an expander for each course
            with st.expander(course, expanded=False):
                # Add content specific to each course
                st.subheader(f"Details for {course}")
                if course == "Data Structures and Algorithms":
                    st.markdown("Data Structures and Algorithms is a fundamental course...")
                elif course == "Internals of Application Server":
                    st.markdown("Internals of Application Server covers...")
                elif course == "Operating Systems":
                    st.markdown("Operating Systems course focuses on...")

    if navigation == "Coding Profile":
        # Main part of the Streamlit app
        st.title("Profile Statistics Coding Platforms")
        def fetch_leetcode_data(profile_api_url, username):
            url = f"{profile_api_url}/{username}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None
        def Leetcode_bar(leetcode_data):
            total_solved = leetcode_data['totalSolved']
            easy_solved = leetcode_data['easySolved']
            medium_solved = leetcode_data['mediumSolved']
            hard_solved = leetcode_data['hardSolved']

            categories = ['Easy', 'Medium', 'Hard']
            solved = [easy_solved, medium_solved, hard_solved]
            colors = ['green', 'orange', 'red']

            # Create horizontal bar chart
            fig, ax = plt.subplots()
            bars = ax.barh(categories, solved, color=colors)

            # Add data labels inside the bars
            for bar, value in zip(bars, solved):
                ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, str(value), va='center')

            # Add LeetCode profile link to the chart title
            leetcode_profile_url = 'https://leetcode.com/lokesh8126'
            ax.set_title(f'LeetCode Profile)', fontsize=16)

            # Set axis labels and title
            ax.set_xlabel(f'Number of Problems Solved : {total_solved}')
            ax.set_ylabel('Difficulty')

            # Show plot
            st.pyplot(fig)
        leetcode_profile_api_url = "https://leetcode-stats-api.herokuapp.com"
        data = fetch_leetcode_data(leetcode_profile_api_url, "lokesh8126")
        if not data:
            st.error("Failed to retrieve Leetcode data. Please try again later.")
        else:
            # provide link to leetcode profile
            st.write(f"LeetCode Profile: [lokesh8126](https://leetcode.com/lokesh8126)")
            st.image("images/leetcode.jpg", width = 200)
            Leetcode_bar(data)    
        st.write("---")  # Line separator
        #Now for gfg profile

        def fetch_gfg_data(username):
            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
                }
            url = f'https://auth.geeksforgeeks.org/user/{username}/practice'
            r = requests.get(url=url, headers=headers)
            return r
        def GFG_bar(data):
            soup = BeautifulSoup(data.content, 'html.parser')
            problemsSolved = int(soup.find_all('span', attrs={'class': 'score_card_value'})[1].text)
            # Find the ul element with class "tabs tabs-fixed-width linksTypeProblem"
            # Find the div element with class "solved_problem_section"
            solved_problem_section = soup.find('div', class_='solved_problem_section')
            # Check if the solved_problem_section exists
            if solved_problem_section:
                # Find all list items (li) within the ul element
                list_items = solved_problem_section.find_all('li', class_='tab')
                # Loop through the list items to extract data
                for li in list_items:
                    # Extract text from the anchor tag within the list item
                    anchor_text = li.a.text.strip()
                    # Split the text to separate the problem category and the number of problems
                    problem_category, num_problems = anchor_text.split(' (')
                    num_problems = int(num_problems.replace(')', ''))  # Remove the closing parenthesis and convert to int
                    # Store the data into respective dictionaries based on problem category
                    if "EASY" in problem_category:
                        easy = num_problems
                    elif "MEDIUM" in problem_category:
                        medium = num_problems
                    elif "HARD" in problem_category:
                        hard = num_problems
            # Create a horizontal bar chart
            fig, ax = plt.subplots()
            categories = ['Easy-Med', 'Medium2Hard', 'Hard']
            solved = [easy, medium, hard]
            colors = ['green', 'orange', 'red']
            bars = ax.barh(categories, solved, color=colors)
            # Add data labels inside the bars
            for bar, value in zip(bars, solved):
                ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, str(value), va='center')
            # Set the title and axis labels
            ax.set_title(f'GeeksforGeeks Profile')
            ax.set_xlabel(f'Number of Problems Solved : {problemsSolved}')
            ax.set_ylabel('Difficulty')
            # Show the plot
            st.pyplot(fig)

        data = fetch_gfg_data("lokeshsharma123456")
        if not data:
            st.error("Failed to retrieve GFG data. Please try again later.")
        else:
            st.write(f"GeeksforGeeks Profile: [lokeshsharma123456](https://auth.geeksforgeeks.org/user/lokeshsharma123456/practice)")
            st.image("images/gfg.jpg", width = 200)
            GFG_bar(data)    
        st.write("---")  # Line separator
        # Coding ninja profile
        st.image("images/cn.jpg", width = 200)
        st.write("Coding Ninja Profile: [Lokesh_8126](https://www.codingninjas.com/studio/profile/Lokesh_8126)")
        st.write('''---''')
        # Interviewbit Profile
        # st.image("./images/ib.jpg", width = 200)
        st.write("Interviewbit Profile: [lokeshsharma123456](https://www.interviewbit.com/profile/lokeshsharma123456)")
        st.image("images/interviewbit.png", width = 200)
        
