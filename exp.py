import streamlit as st

def show():
    st.markdown(
        """
        <style>
        .experience-container {
            background-color: black;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .experience-title {
            color: white;
            font-size: 40px;
            margin-bottom: 20px;
        }
        .experience-link {
            color: #1E90FF;
            font-size: 20px;
            text-decoration: none;
        }
        .experience-link:hover {
            text-decoration: underline;
        }
        .experience-image-caption {
            color: white;
            font-size: 24px;  /* Adjust the font size here */
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page Title
    st.markdown('<div class="experience-container">', unsafe_allow_html=True)
    st.markdown('<div class="experience-title"><h2>EXPERIENCE THE MAGIC!!!!</h2></div>', unsafe_allow_html=True)
    
    # Link to the website
    st.markdown(
        '<a href="https://universe.roboflow.com/sports-video-analysis/sports-video-analysis-t7jiq/model/1" class="experience-link" target="_blank">Click here to try out our model</a>',
        unsafe_allow_html=True
    )

    # Display the image with a specified width and caption
    st.image("roboflowqr.jpeg", caption="<div class='experience-image-caption'>Experience Our Model</div>", width=200, use_column_width='auto')

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()
