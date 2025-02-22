import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")

st.title("Growth Mindset Challange")

st.header("🚀 Welcome to your growth journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app help you build a growth mindset with reflection, challenges, and achievements! ☀️")

st.header("💡 Today's Growth Mindset Quote")
st.write('"Success is not final, failure is not fatal: it is the courage to continue that counts."- Winston Churchill')

st.header("🔧 What's your challenge today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 you are facing: {user_input}. Keep pushing forward towards to your goal! 🚀")
else:
    st.warning("Tell us your challenge to get started!")

st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here: ")
if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past exprience help you grow! Share your difficulties ")

st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🌠 Amazing! You Achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 😍")

st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**⛔ Created By M.Mudasir Chandio**")
