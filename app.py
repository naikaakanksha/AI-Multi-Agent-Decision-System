import streamlit as st
from orchestrator.decision_maker import get_decision

st.set_page_config(page_title="AI Decision System", layout="centered")

# 🔷 Header
st.markdown("""
<h1 style='text-align: center;'>🤖 AI Multi-Agent Decision System</h1>
<p style='text-align: center; color: grey; font-size:16px;'>
Get intelligent decisions using multiple AI perspectives
</p>
""", unsafe_allow_html=True)

# 🔷 Info box (VERY IMPORTANT)
st.info("🤖 This system uses 5 AI agents: Career, Market, ROI, Devil’s Advocate, and Personal Fit to analyze your decision.")

st.divider()

# 🔷 Input Section
st.markdown("### 💬 Ask your question")

user_input = st.text_area(
    "",
    placeholder="e.g., Should I learn Data Science or Web Development?"
)

# 🔷 Suggestions
st.markdown("💡 **Try asking:**")
st.write("- Should I learn Data Science or Web Development?")
st.write("- Is MBA better than a tech career?")
st.write("- Should I focus on AI or Software Development?")

# 🔷 Button
if st.button("🚀 Analyze Decision", use_container_width=True):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("🧠 5 AI agents are analyzing your decision..."):
            final, career, market, devil, roi, fit = get_decision(user_input)

        st.divider()

        # 🔷 Final Decision
        st.markdown("## 🏆 Final Decision")
        st.success(final)

        st.divider()

        # 🔷 Agent Insights with TABS (Premium Look)
        st.markdown("## 🤖 Agent Insights")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "👨‍💼 Career",
            "📊 Market",
            "⚖️ Devil",
            "💰 ROI",
            "🧍‍♀️ Fit"
        ])

        with tab1:
            st.write(career)

        with tab2:
            st.write(market)

        with tab3:
            st.write(devil)

        with tab4:
            st.write(roi)

        with tab5:
            st.write(fit)