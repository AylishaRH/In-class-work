import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Aylisha Roper-Haskins | Portfolio',
  page_icon='🎯',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font_size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio(
    'Go to',
    ['🏡 Home', '💕 About', '👜 Projects', '🛠 Skills' ,'📝 Resume', '💌 Contact' ]
)

# Home Page
if page == '🏡 Home':
  st.markdown('<p class="main-header">Aylisha Haskins</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Business Addministration student | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
     st.metric('GPA', '2.6', '📚')
  with col2:
     st.metric('Project', '2', '💻')
  with col3:
     st.metric('Skills', '5', '🧠')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am a Business Administration student at Medgar Evers College with a passionate 
                interest in Computer Information System and technonlogy. I am building my skills
                in Python, Streamlit, and data to create real-world, useful tools. Some day I 
                will need it in my line of profession. 
            
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                🎶 **Fun Fact:** I like to make beats
             ''')
    with col2:
      # Placeholder for image
      st.image('https://raw.githubusercontent.com/avinashjairam/cis211_project1/refs/heads/main/grumpy_cat.jfif', use_column_width=True)

  # About Page
elif page == '💕About':
    st.title('About Me')

    # Timeline of my Professional Journey
    st.subheader('My Journey 🌅')

    with st.expander('2023 - Present: Medgar Evers College'):
      st.write('''
                  - Major: Business Administration 
                  - Relevant Coursework: Principles of Accounting, Introudction to Statistics, Internet & Emergin Technogloy, Human Resource Managment, International Business
                  - Activities: Dance and photography
              ''')

    with st.expander('2019 - 2023: Young Women Leadership'):
      st.write('''
                  - Advanced regents diaploma
                  - Graduated with honors
                  - Cheerleading
              ''')

    st.subheader('Interests & Hobbies 👩🏾‍💼')
    interests = ['Business & Entrepreneurship', 'Fashion & styling ', 'Content Creating', 'Photography', 'Travel', 'Dance']

    # Display the interests in columns
    cols = st.columns(3)
    for i, interest in enumerate(interests):
      with cols[i % 3]:
        st.info(f'🔷 {interest}')
      
elif page == '👜 Projects':
    st.title('My Projects')
    st.write('Here are some projects I have worked on or I am planning:')

    # Project 1
    with st.container():
      col1, col2 = st.columns([1, 2])
  
      with col1:
          st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg', use_column_width = True)
      
      with col2:
          st.subheader('🗂️ Interactive Portfolio (CIS 211)')
          st.write('''
            This Streamlit wed app (the site you are on now) showcases my coursework,
            skills, and interests. It's part of my CIS 211 project and also a real portfolio
            I can share with anybody.
        ''')
          st.caption('**Technologies:** Python, GitHub, Streamlit')


    # Project 2 
    with st.container():
      col1, col2 = st.columns([1,2])
      with col1:
        st.image('https://static.vecteezy.com/system/resources/previews/014/680/687/non_2x/online-shopping-or-payment-via-mobile-phone-concept-flat-illustration-in-cartoon-style-vector.jpg', 
                 use_column_width = True
                )
      
      with col2:
        st.subheader('🛍️ Depop/ Online Reselling Plan')
        st.write('''
            A small business plan for selling clothes and items online, including
            pricing, photos, shipping, and communication. 
        ''')
        st.caption('**Skills:** Customer Service, Pricing, Social Media')
  
elif page == '🛠 Skills':
    st.title('Technical & Professional Skills')

    # Skills with progress bars
    st.subheader('Programming & Technical Skills')
  
    skills_data = {
      'Python' : 70,
      'HTML/CSS' : 60,
      'JavaScript' : 40,
      'Excel/ Google Sheets' : 85,
      'Technical Writing' : 65
    }

    for skill, level in skills_data.items():
      col1, col2 = st.columns([1,3])
      with col1:
        st.write(skill)
      with col2:
        st.progress(level/100)
  
    st.subheader('Tools & Technologies')

    col1, col2, col3 = st.columns(3)
    with col1:
      st.success('Excel')
      st.info('Word')
      st.warning('Powerpoint')
  
    with col2:
      st.success('Canva')
      st.info('Google Docs')
      st.warning('ChatGPT/AI Tools')
      
    with col3:
      st.success('Writing')
      st.info('Social Media')
      st.warning('Presentation Skills')
  
elif page == '📝 Resume':
    st.title('Resume')
  
    st.write('You can download my resume using the button below .')

    # Read PDF from my GitHub repository
    with open('my_resume.pdf', 'rb') as pdf_file:
      PDFbyte = pdf_file.read()
    
    st.download_button(
      label ='🔻 Download Full Resume (PDF)',
      data = PDFbyte,
      file_name = 'Resume (2).pdf',
      mime ='application/pdf'
    )
  
elif page == '📩 Contact':
    st.title("Let's Connect!")
  
    col1, = st.columns(1)
  
    with col1:
      st.subheader('Send me a message.')
  
      st.write('''
          📧 **Email:** aylishahaskins13@gmail.com
  
          👩‍💻 **Github:** [https://github.com/AylishaRH](https://github.com)
  
      ''')
  
      # Fun interative element
      st.subheader('Current Status')
  
      status = st.selectbox(
          "I'm currently:",
          [
              '📕 Studying',
              '🧘🏾‍♀️ Relaxing',
              '📸 Photography'
              '📺 Watching TV'
          ]
      )
  
  
      st.info(f'Status: {status}')
  
      # Footer
      st.write('---')
      st.markdown(
          f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Aylisha Roper-Haskins </center>',
          unsafe_allow_html = True
      )
    



      









