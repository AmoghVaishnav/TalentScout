def gather_candidate_info():
    """
    Prompt to gather candidate's basic information.

    Returns:
    - dict: Candidate information including name, email, years of experience, tech stack, etc.
    """
    candidate_info = {}

    candidate_info["full_name"] = input("Please enter your full name: ")
    candidate_info["email"] = input("Please enter your email address: ")
    candidate_info["phone"] = input("Please enter your phone number: ")
    candidate_info["years_of_experience"] = input("How many years of experience do you have? ")
    candidate_info["desired_position"] = input("What position are you applying for? ")
    candidate_info["current_location"] = input("Where are you currently located? ")
    candidate_info["tech_stack"] = input("Please specify your tech stack (comma separated): ").split(',')

    return candidate_info
