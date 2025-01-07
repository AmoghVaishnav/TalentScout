import json

def save_candidate_info(candidate_info, filename="data/candidates.json"):
    """
    Save candidate information to a JSON file.

    Parameters:
    - candidate_info (dict): The dictionary containing candidate's details.
    - filename (str): The file to save candidate info.
    """
    with open(filename, "a") as file:
        json.dump(candidate_info, file, indent=4)
        file.write("\n")  

def save_generated_questions(questions_dict, filename="data/questions.json"):
    """
    Save the generated questions for each technology to a JSON file.

    Parameters:
    - questions_dict (dict): The dictionary containing tech stack and associated questions.
    - filename (str): The file to save generated questions.
    """
    with open(filename, "w") as file:
        json.dump(questions_dict, file, indent=4)
