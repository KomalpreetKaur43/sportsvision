import streamlit as st

def show():
    st.markdown("""
    <style>
    body {
        background-color: black; /* Set the background color of the entire page */
        color: white; /* Set default text color to white for better readability */
    }
    .content {
        font-size: 60px; /* Increase the font size here */
        font-weight: bold; /* Ensure text color is white */
        text-align: center;
        margin: 30px 0;
        padding: 20px; /* Add padding to make sure it is visible */
    }
    .action-heading {
        font-size: 40px; /* Increase the font size here */
        font-weight: bold; /* Ensure text color is white */
        text-align: center;
        margin: 20px 0;
    }
    .caption { /* Ensure caption text color is white */
        font-size: 14px; /* Optional: Adjust caption font size */
        text-align: center;
        display: block;
        margin-top: 5px;
    }
    .video-container {
        text-align: center;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Content
    st.markdown('<div class="content">Welcome to SportsVision</div>', unsafe_allow_html=True)
    st.write("Enhance your athletic performance with our cutting-edge video analysis tools. Upload your sports videos and get detailed insights and metrics to take your game to the next level.")

    # Centered Video
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    st.video('output.mp4')
    st.markdown('</div>', unsafe_allow_html=True)

    # Key Benefits
    st.write("## Key Benefits")
    st.write("""
    - Advanced Performance Metrics
    - Personalized Improvement Plans
    - Expert Analysis by Professional Coaches
    - Easy-to-Use Upload and Review System
    - Secure and Private
    """)

    # Action Heading
    st.markdown('<div class="action-heading">See how we bring the action to life below!</div>', unsafe_allow_html=True)

    # Images in a grid layout with unique captions
    cols = st.columns(3)
    image_paths = ['referee.png', 'hoop.png', 'player.png', 'basketball.png', 'scorecard.png']
    captions = [
        'Referee in action',
        'Basketball hoop',
        'Player making a shot',
        'Basketball close-up',
        'Scorecard from the game'
    ]

    for i in range(3):
        with cols[i]:
            st.image(image_paths[i], caption='', use_column_width=True)
            st.markdown(f'<p class="caption">{captions[i]}</p>', unsafe_allow_html=True)

    cols = st.columns(2)
    for i in range(3, 5):
        with cols[i-3]:
            st.image(image_paths[i], caption='', use_column_width=True)
            st.markdown(f'<p class="caption">{captions[i]}</p>', unsafe_allow_html=True)
