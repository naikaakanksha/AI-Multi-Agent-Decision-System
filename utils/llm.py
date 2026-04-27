def call_llm(prompt):
    
    prompt = prompt.lower()

    # 🧠 Logic / General
    if "should i" in prompt or "better" in prompt:
        return (
            "From a logical perspective, both options should be evaluated based on effort, outcome, and long-term impact."
        )

    # 💰 ROI / MONEY
    elif "roi" in prompt or "worth" in prompt or "investment" in prompt or "salary" in prompt:
        return (
            "From a return on investment perspective, some options may take more time initially but provide higher long-term benefits."
        )

    # ⚖️ RISK / DEVIL
    elif "risk" in prompt or "downside" in prompt or "challenge" in prompt:
        return (
            "One important consideration is the potential risk involved, including uncertainty, competition, and required effort."
        )

    # 🧠 PERSONAL FIT
    elif "suit" in prompt or "interest" in prompt or "like" in prompt:
        return (
            "The best decision depends on your personal interests, strengths, and long-term goals."
        )

    # 🌍 TRENDS / MARKET
    elif "trend" in prompt or "demand" in prompt or "future" in prompt:
        return (
            "Current trends indicate growing demand in technology-driven fields, especially in AI, data, and software development."
        )

    # 🏆 FINAL
    else:
        return (
            "Considering all factors such as logic, trends, risks, ROI, and personal fit, the best choice depends on balancing practical outcomes with your personal goals."
        )