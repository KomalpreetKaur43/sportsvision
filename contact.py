import streamlit as st

def show():
    # Custom styling using Streamlit
    st.markdown("""
    <style>
        .contact {
            padding: 2em 0;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            color: white;
            text-align: center;
        }
        .contact h2 {
            font-size: 50px;
        }
        .contact p {
            font-size: 40px;
            margin: 1em 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Contact Us Page
    st.markdown("""
    <div class="contact">
        <p>Contact us: <a href="mailto:sportsvision80@gmail.com" style="color: #1E90FF;">sportsvision80@gmail.com</a></p>
    </div>
    """, unsafe_allow_html=True)

# Make sure to call the show function
if __name__ == "__main__":
    show()
