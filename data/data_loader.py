import streamlit as st
import json
from pathlib import Path

DATA_PATH = Path("data/candidates.json")
DATA_PATH.parent.mkdir(exist_ok=True, parents=True)

def load_data():
    """Load existing candidate data from the JSON file."""
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_data(candidate_data):
    """Save candidate data to the JSON file."""
    existing_data = load_data()
    existing_data.append(candidate_data)
    with open(DATA_PATH, "w") as f:
        json.dump(existing_data, f, indent=4)

# Streamlit UI
st.title("TalentScout Hiring Assistant")
st.subheader("Candidate Information Form")

# Input fields
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
years_of_experience = st.number_input("Years of Experience", min_value=0, step=1)
desired_position = st.text_input("Desired Position(s)")
current_location = st.text_input("Current Location")
tech_stack = st.text_area(
    "Tech Stack (e.g., Python, Django, React)",
    help="Enter a comma-separated list of technologies you are proficient in."
)

# Save button
if st.button("Submit"):
    if all([full_name, email, phone, desired_position, current_location, tech_stack]):
        candidate_data = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "years_of_experience": years_of_experience,
            "desired_position": desired_position,
            "current_location": current_location,
            "tech_stack": [tech.strip() for tech in tech_stack.split(",")]
        }
        save_data(candidate_data)
        st.success("Candidate information saved successfully!")
    else:
        st.error("Please fill out all fields.")

# Display saved data (for testing purposes)
if st.checkbox("Show Saved Data"):
    data = load_data()
    st.write(data)
