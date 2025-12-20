import streamlit as st
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Bhavya Goyal - Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Function to convert image to base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Custom CSS for dark theme with colorful accents
st.markdown(
    """
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0a0e14 0%, #131920 100%);
        font-family: 'Inter', sans-serif;
    }

    /* Profile photo circle */
    .profile-photo {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin: 0 auto 1.5rem auto;
        display: block;
    }

    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1a2332 0%, #0f1419 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        border: 1px solid #2d3748;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    }

    .header-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6rem;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 4rem;
    }

    .header-text {
    text-align: left;
    flex: 1;
    }



    .main-header h1 {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 50%, #fb923c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
    }

    .main-header h2 {
        font-size: 1.5rem;
        color: #9ca3af;
        font-weight: 400;
        margin-bottom: 1rem;
    }

    .contact-info {
        display: flex;
        justify-content: flex-start;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
    }

    .contact-item {
        color: #22d3ee;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        padding: 0.5rem 1rem;
        background: rgba(167, 139, 250, 0.1);
        border-radius: 8px;
        border: 1px solid rgba(167, 139, 250, 0.3);
    }

    /* Section headers */
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: #e6e8eb;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid;
        border-image: linear-gradient(90deg, #a78bfa 0%, #ec4899 50%, #fb923c 100%) 1;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Project cards */
    .project-card {
        background: linear-gradient(135deg, #1a2332 0%, #0f1419 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #2d3748;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }

    .project-card:hover {
        border-image: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%) 1;
        box-shadow: 0 8px 30px rgba(167, 139, 250, 0.3);
        transform: translateY(-2px);
    }

    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        background: linear-gradient(135deg, #22d3ee 0%, #34d399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
    }

    .project-date {
        color: #9ca3af;
        font-size: 0.85rem;
        margin-bottom: 1rem;
        font-style: italic;
    }

    .project-description {
        color: #c5cbd3;
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.2) 0%, rgba(236, 72, 153, 0.2) 100%);
        color: #ec4899;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.75rem;
        border: 1px solid rgba(236, 72, 153, 0.4);
        font-family: 'JetBrains Mono', monospace;
    }

    /* Experience cards */
    .experience-card {
        background: linear-gradient(135deg, #1a2332 0%, #0f1419 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid #a78bfa;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    }

    .company-name {
        font-size: 1.2rem;
        font-weight: 600;
        color: #fb923c;
        font-family: 'JetBrains Mono', monospace;
    }

    .role-title {
        font-size: 1.1rem;
        color: #e6e8eb;
        margin-bottom: 0.3rem;
    }

    /* Skills grid */
    .skills-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-top: 1rem;
    }

    .skill-category {
        background: linear-gradient(135deg, #1a2332 0%, #0f1419 100%);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #2d3748;
    }

    .skill-category h3 {
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Links */
    .project-link {
        color: #22d3ee;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }

    .project-link:hover {
        color: #34d399;
        text-decoration: underline;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1419 0%, #1a2332 100%);
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        color: #e6e8eb;
    }

    [data-testid="stSidebar"] h3 {
        font-size: 1.3rem;
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 1rem;
    }

    [data-testid="stSidebar"] .stRadio > label {
        font-size: 1.1rem;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        font-size: 1.1rem;
        padding: 0.8rem 0;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #22d3ee;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        font-family: 'JetBrains Mono', monospace;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        box-shadow: 0 5px 20px rgba(167, 139, 250, 0.4);
        transform: translateY(-2px);
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Dashboard images */
    .dashboard-image {
        border-radius: 10px;
        border: 2px solid rgba(167, 139, 250, 0.3);
        margin: 0.5rem 0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        max-height: 400px;
        object-fit: contain;
    }

    </style>
""",
    unsafe_allow_html=True,
)

# Header with profile photo
try:
    profile_img_base64 = get_image_base64(
        "/home/jovyan/git/Projects/Portfolio/profile_photo.png"
    )
    header_html = f"""
    <div class="main-header">
        <div class="header-row">
            <div class="header-text">
                <h1>BHAVYA GOYAL</h1>
                <h2>Data Scientist & Analytics Engineer</h2>
                <div class="contact-info">
                    <div class="contact-item">bgoyal@ucsd.edu</div>
                    <div class="contact-item">(619) 953-7409</div>
                    <div class="contact-item">San Diego, California</div>
                </div>
            </div>
            <img src="data:image/png;base64,{profile_img_base64}" class="profile-photo" alt="Bhavya Goyal">
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)
except Exception as e:
    # Fallback if image not found
    st.markdown(
        """
        <div class="main-header">
            <div class="header-row">
                <div class="header-text">
                    <h1>BHAVYA GOYAL</h1>
                    <h2>Data Scientist & Analytics Engineer</h2>
                    <div class="contact-info">
                        <div class="contact-item">bgoyal@ucsd.edu</div>
                        <div class="contact-item">(619) 953-7409</div>
                        <div class="contact-item">San Diego, California</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Sidebar navigation
with st.sidebar:
    st.markdown("### Navigation")
    page = st.radio(
        "", ["About", "Projects", "Skills", "Education"], label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Projects", "12+")
    with col2:
        st.metric("Skills", "25+")

    st.markdown("---")
    st.markdown("### Connect")
    st.markdown("""
        - [GitHub](https://github.com/rsm-bgoyal)
        - [LinkedIn](https://www.linkedin.com/in/bhavya-goyal-429568308/)
    """)

# Main content based on page selection
if page == "About":
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
        <div style="background: linear-gradient(135deg, #1a2332 0%, #0f1419 100%);
                    padding: 2rem; border-radius: 12px; border: 1px solid #2d3748;">
            <p style="color: #c5cbd3; font-size: 1.1rem; line-height: 1.8;">
                I'm a <span style="color: #22d3ee; font-weight: 600;">Data Scientist and Analytics Engineer</span>
                pursuing my Master's in Business Analytics at UC San Diego's Rady School of Management.
                With a strong foundation in AI, machine learning, and data engineering, I specialize in building
                end-to-end analytics solutions that drive business insights.
            </p>
            <p style="color: #c5cbd3; font-size: 1.1rem; line-height: 1.8; margin-top: 1rem;">
                My expertise spans from <span style="color: #a78bfa; font-weight: 600;">deep learning and NLP</span>
                to <span style="color: #a78bfa; font-weight: 600;">data warehousing and interactive dashboard development</span>.
                I'm passionate about transforming complex data into actionable insights and building AI-powered solutions
                that solve real-world problems.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div style="background: linear-gradient(135deg, #1a2332 0%, #0f1419 100%);
                    padding: 1.5rem; border-radius: 12px; border: 1px solid #2d3748;">
            <h3 style="background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
                       -webkit-background-clip: text;
                       -webkit-text-fill-color: transparent;
                       margin-bottom: 1rem; font-family: 'JetBrains Mono', monospace;">
                Core Expertise
            </h3>
            <ul style="color: #c5cbd3; list-style: none; padding: 0;">
                <li style="margin-bottom: 0.5rem;">• Machine Learning & Deep Learning</li>
                <li style="margin-bottom: 0.5rem;">• NLP & Sentiment Analysis</li>
                <li style="margin-bottom: 0.5rem;">• Data Warehousing (Snowflake)</li>
                <li style="margin-bottom: 0.5rem;">• Interactive Dashboards</li>
                <li style="margin-bottom: 0.5rem;">• ETL Pipeline Development</li>
                <li style="margin-bottom: 0.5rem;">• Computer Vision & CNNs</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="section-header">Professional Experience</div>',
        unsafe_allow_html=True,
    )

    # Experience 1
    st.markdown(
        """
    <div class="experience-card">
        <div class="company-name">Virtuous Vision Pvt Ltd, India</div>
        <div class="role-title">Data Science and AI Intern</div>
        <div class="project-date">January 2024 - January 2025</div>
        <div class="project-description">
            <ul style="color: #c5cbd3; line-height: 1.8;">
                <li>Designed and deployed an AI chatbot using Python and TensorFlow to streamline bookings,
                    provide real-time vendor and venue recommendations, and enhance 24/7 customer support.</li>
                <li>Increased customer support availability by 30% through faster response times and reduced
                    manual queries.</li>
                <li>Presented solutions effectively to both technical and non-technical stakeholders.</li>
            </ul>
        </div>
        <div>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">TensorFlow</span>
            <span class="skill-tag">AI Chatbot</span>
            <span class="skill-tag">NLP</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Experience 2
    st.markdown(
        """
    <div class="experience-card">
        <div class="company-name">Ohceans Pte Ltd, Singapore</div>
        <div class="role-title">Data Science Intern</div>
        <div class="project-date">July 2023 - December 2023</div>
        <div class="project-description">
            <ul style="color: #c5cbd3; line-height: 1.8;">
                <li>Spearheaded development of a React.js dashboard, integrated with Plotly.js for interactive
                    charts and Leaflet.js for geospatial maps.</li>
                <li>Improved real-time vessel tracking and incident reporting by 25% in operational speed.</li>
                <li>Collaborated with domain experts to define KPIs and delivered weekly progress updates to
                    management, aligning technical deliverables with business goals.</li>
            </ul>
        </div>
        <div>
            <span class="skill-tag">React.js</span>
            <span class="skill-tag">Plotly.js</span>
            <span class="skill-tag">Leaflet.js</span>
            <span class="skill-tag">Data Visualization</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

elif page == "Projects":
    st.markdown(
        '<div class="section-header">Featured Projects</div>', unsafe_allow_html=True
    )

    # Filter options
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("Search projects", placeholder="Enter keywords...")
    with col2:
        filter_skill = st.selectbox(
            "Filter by skill",
            ["All", "Python", "Deep Learning", "NLP", "Tableau", "Streamlit", "SQL"],
        )

    projects = [
        {
            "title": "Twitter Sentiment & Equity Market Intelligence",
            "date": "Sep 2025 - Dec 2025",
            "org": "UC San Diego",
            "description": "Built an end-to-end analytics pipeline integrating Twitter data with equity market data for 25 U.S. stocks. Implemented NLP sentiment analysis in Python using RoBERTa and VADER, engineered financial indicators (Volume Z-Score, Strength Rank, Rolling Volatility), and delivered three interactive Tableau dashboards. Findings show sentiment–return correlation strengthens on high-volume trading days, positioning sentiment as a confirmation signal in market analysis.",
            "skills": [
                "Python",
                "NLP",
                "RoBERTa",
                "VADER",
                "Tableau",
                "Sentiment Analysis",
                "Time Series Analysis",
            ],
            "links": [],
            "images": [
                "1765513575211.jpeg",
                "1765513575173.jpeg",
                "1765513575339.jpeg",
            ],
        },
        {
            "title": "Yelp Analytics Dashboard",
            "date": "Nov 2025 - Dec 2025",
            "org": "UC San Diego",
            "description": "Developed an interactive Streamlit dashboard for analyzing Yelp business and review data, enabling data-driven insights for restaurant performance and customer sentiment analysis. Implemented Python-based data processing pipelines to clean and transform Yelp datasets, created dynamic visualizations for rating trends, review patterns, and geographic distribution of businesses.",
            "skills": [
                "Streamlit",
                "Python",
                "Data Visualization",
                "Interactive Dashboards",
                "Data Engineering",
            ],
            "links": [
                {
                    "text": "GitHub Repo",
                    "url": "https://github.com/rsm-bgoyal/Yelp-Analytics-Dashboard",
                },
                {
                    "text": "Live Dashboard",
                    "url": "https://yelp-analytics-dashboard-e877zsqi6mcjvdqcrrtvxa.streamlit.app/",
                },
            ],
            "images": [],
        },
        {
            "title": "Interactive Leadership Development Game (The Strategy Shuffle)",
            "date": "Oct 2025 - Nov 2025",
            "org": "UC San Diego",
            "description": "Built a Streamlit-based interactive card game to gamify leadership and influence concepts from Managerial Decision-Making coursework. Developed personalized player profiles based on influence strengths and integrated Smart, Hard, and Soft Power strategies into gameplay scenarios. Created customizable game configurations supporting multiple players and rounds.",
            "skills": ["Streamlit", "Python", "Game Development", "UI/UX Design"],
            "links": [
                {
                    "text": "GitHub Repo",
                    "url": "https://github.com/rsm-bgoyal/The-Strategy-Shuffle",
                },
                {
                    "text": "Play Game",
                    "url": "https://the-strategy-shuffle-feufg8kckcqusbftvf6mmn.streamlit.app/",
                },
            ],
            "images": [],
        },
        {
            "title": "Snowflake Data Warehouse and ETL Integration",
            "date": "Aug 2025",
            "org": "UC San Diego",
            "description": "Developed a Snowflake data warehouse integrating purchase, supplier, invoice, and weather datasets through automated Python and SQL ETL pipelines. Built materialized views and optimized queries, improving data processing efficiency and enabling analysis of purchase order discrepancies and external factors.",
            "skills": [
                "Snowflake",
                "Python",
                "SQL",
                "ETL",
                "Data Warehousing",
                "Query Optimization",
            ],
            "links": [],
            "images": [],
        },
        {
            "title": "Image Classification for Genetic Relatedness",
            "date": "Jan 2023 - May 2023",
            "org": "Nanyang Technological University",
            "description": "Applied image classification models to determine genetic similarity between image pairs. Compared multiple deep learning architectures to identify optimal accuracy in recognizing genetic relationships using Siamese networks and CNNs.",
            "skills": [
                "Deep Learning",
                "Python",
                "CNN",
                "Image Classification",
                "Siamese Networks",
            ],
            "links": [
                {
                    "text": "GitHub Repo",
                    "url": "https://github.com/rsm-bgoyal/Image-Classification-for-genetic-relatedness",
                }
            ],
            "images": [],
        },
        {
            "title": "Utilization of Deep Reinforcement Learning in the Metaverse",
            "date": "Jan 2023 - May 2023",
            "org": "Nanyang Technological University",
            "description": "Developed a Quality of Service (QoS) optimization model for augmented-reality (AR) socialization in the Metaverse using deep reinforcement learning (DRL). The model dynamically allocates channels between AR users and virtual service providers in a multichannel wireless network to minimize delay and transmission power while maximizing user satisfaction and display stability. After comparing with various pre-existing reinforcement learning algorithms, the QoS model performs better in all aspects, accounting for factors such as delay, transmit power, channel allocation, user satisfaction, and maximum tolerable display to provide users with a smooth AR experience.",
            "skills": [
                "Deep Learning",
                "Reinforcement Learning",
                "Python",
                "QoS Optimization",
                "Wireless Networks",
            ],
            "links": [],
            "images": ["metaverse_poster.png"],
        },
        {
            "title": "Gender and Age Image Classification using Neural Networks",
            "date": "Sep 2022 - Dec 2022",
            "org": "Nanyang Technological University",
            "description": "Designed and implemented a Convolutional Neural Network (CNN) for gender and age classification from facial images. Conducted comparative analysis of the proposed CNN model against multiple baseline architectures to assess accuracy and computational efficiency.",
            "skills": [
                "TensorFlow",
                "Keras",
                "Deep Learning",
                "Python",
                "CNN",
                "Image Classification",
            ],
            "links": [
                {
                    "text": "GitHub Repo",
                    "url": "https://github.com/rsm-bgoyal/Gender-Age-Classification",
                }
            ],
            "images": [],
        },
        {
            "title": "Database Management System for Advanced Contact Tracing",
            "date": "Jan 2022 - May 2022",
            "org": "Nanyang Technological University",
            "description": "Created a SQL-based database system for COVID-19 contact tracing. Developed optimized SQL queries to efficiently identify individuals potentially exposed to infection, improving response time for health authorities.",
            "skills": [
                "SQL",
                "Microsoft SQL Server",
                "Database Design",
                "Query Optimization",
                "DBMS",
            ],
            "links": [],
            "images": [],
        },
        {
            "title": "Depression Detection in Twitter Tweets",
            "date": "Sep 2021 - Dec 2021",
            "org": "Nanyang Technological University",
            "description": "Performed sentiment analysis on 50,000+ COVID-19 and lockdown-related tweets using Python to detect changes in public mood. Identified a 20% rise in negative sentiment, revealing actionable insights for mental health and public wellbeing initiatives.",
            "skills": [
                "Python",
                "NLP",
                "NLTK",
                "Sentiment Analysis",
                "Text Mining",
                "Data Cleaning",
            ],
            "links": [
                {
                    "text": "YouTube Presentation",
                    "url": "https://youtu.be/VNwZwU3IW0Q?si=UBQE_UxPh4E4sh-5",
                }
            ],
            "images": [],
        },
        {
            "title": "PropNow Housing Information App",
            "date": "Jan 2021 - Apr 2021",
            "org": "Nanyang Technological University",
            "description": "Developed a mobile app using Android Studio to assist users in house buying/selling and mortgage calculations. Implemented features for transaction tracking and real-time price estimation with an intuitive interface.",
            "skills": [
                "Java",
                "Android Studio",
                "Mobile Development",
                "UI Design",
                "XML",
            ],
            "links": [
                {
                    "text": "GitHub Repo",
                    "url": "https://github.com/rsm-bgoyal/PropNowAndroidApp",
                }
            ],
            "images": [],
        },
        {
            "title": "Data Analysis on High School Student Alcohol Consumption",
            "date": "Aug 2020 - Dec 2020",
            "org": "Nanyang Technological University",
            "description": "Conducted statistical analysis on a public dataset examining correlations between academic performance, alcohol consumption, and parental education levels. Delivered insights into behavioral and demographic factors influencing outcomes.",
            "skills": [
                "R",
                "Statistical Analysis",
                "Data Visualization",
                "Correlation Analysis",
            ],
            "links": [
                {
                    "text": "GitHub Repo",
                    "url": "https://github.com/rsm-bgoyal/High-School-Student-Alcohol-Consumption",
                }
            ],
            "images": [],
        },
        {
            "title": "Women's E-Commerce Data Analysis",
            "date": "Jan 2020 - Apr 2020",
            "org": "Nanyang Technological University",
            "description": "Performed exploratory data analysis on a women's e-commerce dataset to identify shopping patterns and predict product preferences. Built a recommendation engine using features derived from customer reviews, ratings, and comments.",
            "skills": [
                "Python",
                "Machine Learning",
                "Text Mining",
                "Data Cleaning",
                "EDA",
            ],
            "links": [
                {
                    "text": "GitHub Repo",
                    "url": "https://github.com/rsm-bgoyal/Women-s-E-Commerce-Analysis",
                }
            ],
            "images": [],
        },
    ]

    # Filter projects
    filtered_projects = projects
    if search:
        filtered_projects = [
            p
            for p in filtered_projects
            if search.lower() in p["title"].lower()
            or search.lower() in p["description"].lower()
        ]
    if filter_skill != "All":
        filtered_projects = [
            p for p in filtered_projects if filter_skill in p["skills"]
        ]

    # Display projects
    for project in filtered_projects:
        st.markdown(
            f"""
        <div class="project-card">
            <div class="project-title">{project["title"]}</div>
            <div class="project-date">{project["date"]} • {project["org"]}</div>
            <div class="project-description">{project["description"]}</div>
            <div style="margin-top: 1rem;">
                {"".join([f'<span class="skill-tag">{skill}</span>' for skill in project["skills"]])}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Display project images if available
        if project.get("images"):
            if len(project["images"]) == 1:
                # Single image - display centered with max height
                try:
                    st.image(project["images"][0], use_container_width=False, width=600)
                except:
                    pass
            else:
                # Multiple images - display in columns
                cols = st.columns(len(project["images"]))
                for idx, img_path in enumerate(project["images"]):
                    with cols[idx]:
                        try:
                            st.image(img_path, use_container_width=True)
                        except:
                            pass

        # Display links
        if project["links"]:
            cols = st.columns(len(project["links"]))
            for idx, link in enumerate(project["links"]):
                with cols[idx]:
                    st.markdown(f"[{link['text']} →]({link['url']})")

        st.markdown("<br>", unsafe_allow_html=True)

elif page == "Skills":
    st.markdown(
        '<div class="section-header">Technical Skills</div>', unsafe_allow_html=True
    )

    skills_data = {
        "Programming Languages": [
            "Python",
            "C",
            "C++",
            "Java",
            "JavaScript",
            "R",
            "MATLAB",
            "SQL",
        ],
        "Machine Learning & AI": [
            "TensorFlow",
            "Keras",
            "scikit-learn",
            "CNNs",
            "Reinforcement Learning",
            "NLP",
            "A/B Testing",
            "Deep Learning",
        ],
        "Data Engineering & Tools": [
            "Snowflake",
            "ETL Pipelines",
            "Git",
            "Plotly",
            "Leaflet",
            "React",
            "Android Studio",
            "Tkinter",
        ],
        "Visualization & Dashboards": [
            "Tableau",
            "Streamlit",
            "Plotly.js",
            "Interactive Dashboards",
            "Data Visualization",
        ],
        "Databases": [
            "SQL",
            "Microsoft SQL Server",
            "Database Design",
            "Query Optimization",
        ],
        "NLP & Text Analysis": [
            "NLTK",
            "RoBERTa",
            "VADER",
            "Sentiment Analysis",
            "Text Mining",
        ],
        "Spoken Languages": [
            "English (Proficient)",
            "Hindi (Proficient)",
            "Spanish (Conversant)",
        ],
    }

    st.markdown('<div class="skills-container">', unsafe_allow_html=True)

    cols = st.columns(2)
    idx = 0
    for category, skills in skills_data.items():
        with cols[idx % 2]:
            st.markdown(
                f"""
            <div class="skill-category">
                <h3>{category}</h3>
                <div>
                    {"".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])}
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        idx += 1

    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Education":
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <div class="experience-card">
        <div class="company-name">University of California, San Diego</div>
        <div class="role-title">Master of Science in Business Analytics</div>
        <div class="project-date">Rady School of Management • Expected December 2026</div>
        <div class="project-description">
            <p style="color: #c5cbd3;">
                Advanced coursework in data science, machine learning, business intelligence, and analytics.
                Focus on applying cutting-edge analytical techniques to solve complex business problems.
            </p>
        </div>
        <div>
            <span class="skill-tag">Business Analytics</span>
            <span class="skill-tag">Machine Learning</span>
            <span class="skill-tag">Data Science</span>
            <span class="skill-tag">Business Intelligence</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="experience-card">
        <div class="company-name">Nanyang Technological University, Singapore</div>
        <div class="role-title">Bachelor of Science in Data Science and Artificial Intelligence (Honours)</div>
        <div class="project-date">Graduated December 2023</div>
        <div class="project-description">
            <p style="color: #c5cbd3;">
                Comprehensive education in data science, artificial intelligence, machine learning, and software engineering.
                Completed multiple research projects in deep learning, NLP, and computer vision.
            </p>
        </div>
        <div>
            <span class="skill-tag">Data Science</span>
            <span class="skill-tag">Artificial Intelligence</span>
            <span class="skill-tag">Deep Learning</span>
            <span class="skill-tag">Computer Vision</span>
            <span class="skill-tag">NLP</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-header">Leadership & Affiliations</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class="skill-category">
            <h3>Welfare Officer</h3>
            <p style="color: #c5cbd3;">Nanyang Arts Ensemble</p>
            <p style="color: #9ca3af; font-size: 0.9rem; margin-top: 0.5rem;">
                Organized and facilitated mental wellbeing workshops
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="skill-category">
            <h3>Member</h3>
            <p style="color: #c5cbd3;">NTU Indian Dance</p>
            <p style="color: #9ca3af; font-size: 0.9rem; margin-top: 0.5rem;">
                Collaborated with peers to coordinate cultural performances and events
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #9ca3af; padding: 2rem;
                border-top: 1px solid #2d3748; margin-top: 3rem;">
        <p style="font-family: 'JetBrains Mono', monospace;">
            Built with Streamlit • © 2025 Bhavya Goyal
        </p>
        <p style="margin-top: 0.5rem;">
            <a href="https://www.linkedin.com/in/bhavya-goyal-429568308/" target="_blank"
               style="color: #22d3ee; text-decoration: none; margin: 0 1rem;">LinkedIn</a>
            <a href="https://github.com/rsm-bgoyal" target="_blank"
               style="color: #22d3ee; text-decoration: none; margin: 0 1rem;">GitHub</a>
            <a href="mailto:bgoyal@ucsd.edu"
               style="color: #22d3ee; text-decoration: none; margin: 0 1rem;">Email</a>
        </p>
    </div>
""",
    unsafe_allow_html=True,
)
