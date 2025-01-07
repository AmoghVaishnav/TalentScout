from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model(model_name="facebook/vicuna-13b"):
    """
    Load a pretrained Vicuna model and tokenizer for prompt-based question generation.

    Parameters:
    - model_name (str): The name of the pretrained model from Hugging Face.

    Returns:
    - tokenizer: The tokenizer for the model.
    - model: The loaded model.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

def generate_questions_local(
    tech_stack, 
    num_questions=3, 
    model_name="facebook/vicuna-13b"
):
    """
    Generate technical questions based on the tech stack using a pretrained Vicuna model.

    Parameters:
    - tech_stack (list): A list of technologies provided by the candidate.
    - num_questions (int): The number of questions to generate per technology.
    - model_name (str): The name of the Hugging Face model to use.

    Returns:
    - dict: A dictionary with technologies as keys and lists of questions as values.
    """
    tokenizer, model = load_model(model_name)
    
    questions_dict = {}
    
    for tech in tech_stack:
        prompt = (
            f"Generate {num_questions} technical interview questions for the following technology: {tech}. "
            f"Ensure questions assess both practical and theoretical knowledge."
        )
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = model.generate(**inputs, max_length=256, num_beams=5, temperature=0.7)
        
        # Decode and format the questions
        questions = tokenizer.decode(outputs[0], skip_special_tokens=True)
        questions_dict[tech] = [q.strip() for q in questions.split("\n") if q.strip()]
    
    return questions_dict
