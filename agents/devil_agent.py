from utils.llm import call_llm

def devil_agent(user_input):
    prompt = f"""
    You are a critical thinker.

    Argue AGAINST the most popular choice.
    Highlight risks and downsides.

    User question:
    {user_input}
    """
    return call_llm(prompt)