from utils.llm import call_llm

def career_agent(user_input):
    prompt = f"""
    You are an expert career advisor.

    Provide:
    - Career opportunities
    - Growth potential
    - Long-term benefits

    User question:
    {user_input}
    """
    return call_llm(prompt)