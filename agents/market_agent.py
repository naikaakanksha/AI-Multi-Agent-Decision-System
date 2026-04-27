from utils.llm import call_llm

def market_agent(user_input):
    prompt = f"""
    You are a job market analyst.

    Provide:
    - Industry demand
    - Future trends
    - Hiring outlook

    User question:
    {user_input}
    """
    return call_llm(prompt)