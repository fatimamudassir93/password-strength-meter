import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Upper & Lower Case": bool(re.search(r"[a-z]", password)) and bool(re.search(r"[A-Z]", password)),
        "Numbers": bool(re.search(r"\d", password)),
        "Special Characters": bool(re.search(r"[@$!%*?&]", password))
    }
    
    strength = sum(criteria.values())
    return strength, criteria

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")
    
    # Custom CSS for styling
    st.markdown("""
        <style>
            body { background-color: #000000; color: white; }
            .stApp { background-color: #000000; color: #ffffff; }
            .stTextInput>div>div>input { font-size: 18px; color: #ffffff; background-color: #333333; }
            .stProgress>div>div { border-radius: 10px; height: 20px; }
            h1, h3, p { color: #FFD700; }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)
    st.write("""A password strength meter helps users create strong and secure passwords. 
A strong password should be at least 8 characters long, contain uppercase and lowercase letters, 
numbers, and special characters. Avoid using common words or easily guessable patterns.

Use this tool to check the strength of your password!
""")
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        strength, criteria = check_password_strength(password)
        
        # Display progress bar based on strength level
        strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
        strength_colors = ["#FF4B4B", "#FF914D", "#FFD700", "#4CAF50", "#008000"]
        
        st.progress(strength / 4)
        st.markdown(f"<h3 style='color: {strength_colors[strength]}; text-align: center;'>{strength_levels[strength]}</h3>", unsafe_allow_html=True)
        
        st.markdown("### Password Criteria")
        for criterion, met in criteria.items():
            color = "#4CAF50" if met else "#FF4B4B"
            st.markdown(f"<p style='color: {color};'>✔ {criterion}</p>" if met else f"<p style='color: {color};'>✖ {criterion}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()



