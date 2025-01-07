import streamlit as st
from prompts.generate_questions import generate_questions_local
from prompts.gather_info import gather_candidate_info
from utils.context_handler import maintain_conversation_context
from utils.privacy import ensure_data_privacy

# Initialize the context handler to maintain conversation context
context_handler = maintain_conversation_context()

# Function to display the greeting and guide the candidate
def display_greeting():
    st.title("TalentScout - Hiring Assistant Chatbot")
    st.write("Welcome to the TalentScout Hiring Assistant!")
    st.write("I'm here to help you with the initial screening for your desired job position.")
    st.write("Let's start by gathering some information.")
    st.write("Please type your answers below.")

# Function to gather candidate information
def collect_candidate_info():
    candidate_info = gather_candidate_info()

    if candidate_info is not None:
        # Store the information into the context handler for the next steps
        context_handler.store_candidate_info(candidate_info)
        return candidate_info
    else:
        return None

# Function to collect and generate questions based on tech stack
def generate_technical_questions(tech_stack):
    num_questions = 3  # You can adjust this number as needed
    questions = generate_questions_local(tech_stack, num_questions)
    
    return questions

# Function to handle the conversation flow
def conversation_flow():
    # Display greeting and initial information
    display_greeting()

    # Step 1: Collect Candidate Info
    if 'candidate_info' not in st.session_state:
        st.session_state['candidate_info'] = {}

    if 'name' not in st.session_state['candidate_info']:
        name = st.text_input("What is your full name?")
        if name:
            st.session_state['candidate_info']['name'] = name
            st.write(f"Thanks {name}! Let's move on.")
    
    if 'email' not in st.session_state['candidate_info']:
        email = st.text_input("What is your email address?")
        if email:
            st.session_state['candidate_info']['email'] = email
            st.write(f"Great! We've got your email.")
    
    if 'phone' not in st.session_state['candidate_info']:
        phone = st.text_input("What is your phone number?")
        if phone:
            st.session_state['candidate_info']['phone'] = phone
            st.write(f"Got it! Now, let's continue.")
    
    if 'experience' not in st.session_state['candidate_info']:
        experience = st.text_input("How many years of experience do you have?")
        if experience:
            st.session_state['candidate_info']['experience'] = experience
            st.write(f"Thanks for the info!")

    if 'position' not in st.session_state['candidate_info']:
        position = st.text_input("What position are you looking for?")
        if position:
            st.session_state['candidate_info']['position'] = position
            st.write(f"Noted! We're almost done gathering information.")
    
    if 'location' not in st.session_state['candidate_info']:
        location = st.text_input("Where are you currently located?")
        if location:
            st.session_state['candidate_info']['location'] = location
            st.write(f"Got your location!")

    if 'tech_stack' not in st.session_state['candidate_info']:
        tech_stack_input = st.text_input("What is your tech stack (e.g., Python, Django, React)?")
        if tech_stack_input:
            tech_stack = tech_stack_input.split(",")  # Split by commas to handle multiple techs
            st.session_state['candidate_info']['tech_stack'] = tech_stack
            st.write(f"Thank you for sharing your tech stack: {', '.join(tech_stack)}")

            # Step 2: Generate Technical Questions
            st.write(f"Generating questions based on your tech stack: {', '.join(tech_stack)}")
            questions = generate_technical_questions(tech_stack)

            # Display the generated questions
            for tech, tech_questions in questions.items():
                st.write(f"### Questions for {tech}:")
                for q in tech_questions:
                    st.write(f"- {q}")

# Main execution
if __name__ == "__main__":
    conversation_flow()