from utils.llm import call_llm

def roi_agent(user_input):
    prompt = f"""
    You are an ROI analyst.

    Evaluate:
    - Time investment
    - Effort required
    - Salary potential

    User question:
    {user_input}
    """
    return call_llm(prompt)