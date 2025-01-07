# TalentScout

TalentScout is an intelligent hiring assistant chatbot developed to streamline the recruitment process. The chatbot assists in the initial screening of candidates by gathering essential information and posing relevant technical questions based on the candidate’s declared tech stack. It’s designed for a recruitment agency specializing in technology placements, providing a seamless experience for both candidates and recruiters.

The project utilizes state-of-the-art NLP models, such as Vicuna, to generate context-aware technical questions for candidates. The backend logic is powered by Streamlit (for UI) and Transformers (for leveraging large language models).

# Project Flow
# Data Collection:

The chatbot starts by greeting the user and requesting basic candidate information like name, email, phone, tech stack, and years of experience.
The information is gathered through text_input components in the Streamlit UI.
Technical Question Generation:

After gathering candidate details, the chatbot prompts the user to specify their tech stack (e.g., programming languages, frameworks, tools).
Based on the provided tech stack, the chatbot uses the Vicuna model to generate tailored technical questions for each listed technology (e.g., Python, Django).
The chatbot generates 3-5 technical questions per tech stack item using prompts created specifically for that purpose.
Conversation Flow:

The chatbot is designed to handle the conversation context, ensuring that it remembers previous inputs and generates relevant follow-up questions.
If the chatbot doesn't understand the input, a fallback mechanism provides a meaningful response to guide the user back to the conversation.
End of Conversation:

Once all the technical questions are generated and displayed, the chatbot thanks the candidate and concludes the session.

# How to Run the Project
To run the TalentScout - Hiring Assistant Chatbot locally, follow these steps:

#1. Clone the Repository
git clone https://github.com/your-username/talentscout-chatbot.git
cd talentscout-chatbot

# 2. Install the Dependencies
Make sure you have Python installed. Then, install the necessary Python libraries by running:
pip install -r requirements.txt

# 3. Run the Streamlit App
To launch the chatbot in your browser, run the following command:
streamlit run app.py
This will open a new tab in your browser where you can interact with the chatbot.

# 4. Interacting with the Chatbot
# Step 1: The chatbot will ask for basic candidate details like full name, email, phone number, and tech stack.
# Step 2: Once the details are provided, the chatbot will generate and display relevant technical questions based on the candidate's tech stack.
# Step 3: The chatbot maintains a smooth conversation flow and will gracefully end the interaction after completing the technical question generation.

# File Structure
hiring_assistant/
│
├── app.py                     # Main Streamlit app that runs the chatbot UI
├── data/
│   ├── questions.json         # Store pre-defined technical questions
│   ├── candidates.json        # Store collected candidate details
├── prompts/
│   ├── gather_info.py         # Prompts for gathering candidate info
│   ├── generate_questions.py  # Prompts for generating technical questions
│   ├── fallback.py            # Fallback prompts
├── models/
│   ├── save_model.py          # Code to save/load prompt-based interactions
│   ├── train.py               # Training logic for feedback-based learning
└── utils/
    ├── context_handler.py     # Handles conversation flow and context
    ├── privacy.py             # Data privacy and security compliance

