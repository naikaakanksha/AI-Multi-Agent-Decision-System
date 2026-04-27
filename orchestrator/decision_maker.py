from agents.career_agent import career_agent
from agents.market_agent import market_agent
from agents.devil_agent import devil_agent
from agents.roi_agent import roi_agent
from agents.personal_fit_agent import personal_fit_agent
from utils.llm import call_llm

def get_decision(user_input):
    career = career_agent(user_input)
    market = market_agent(user_input)
    devil = devil_agent(user_input)
    roi = roi_agent(user_input)
    fit = personal_fit_agent(user_input)

    final_prompt = f"""
    You are an expert decision-maker.

    Career Advice:
    {career}

    Market Trends:
    {market}

    Devil's Advocate:
    {devil}

    ROI Analysis:
    {roi}

    Personal Fit:
    {fit}

    Give:
    1. Final Decision
    2. Key Reasons
    3. When this may not be ideal
    """

    final = call_llm(final_prompt)

    return final, career, market, devil, roi, fit