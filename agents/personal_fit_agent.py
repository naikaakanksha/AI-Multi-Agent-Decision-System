from utils.llm import call_llm

def personal_fit_agent(user_input):
    prompt = f"""
    You are a personal career mentor.

    Suggest what suits the user best based on:
    - Interests
    - Strengths
    - Learning style

    User question:
    {user_input}
    """
    return call_llm(prompt)