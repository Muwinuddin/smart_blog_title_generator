import streamlit as st
import random

def generate_titles(topic):
    templates = [
        f"What Everyone Gets Wrong About {topic}",
        f"{topic} Explained Like You're Five",
        f"Is {topic} Dead? Here's the Truth",
        f"The Surprising Science Behind {topic}",
        f"X Things You Didn’t Know About {topic}",
        f"Why {topic} Could Change Everything",
        f"The Dark Side of {topic}",
        f"If You Care About {topic}, Read This Now",
        f"How {topic} is Disrupting the Industry",
        f"Lessons from Experts on {topic}",
        f"The Most Controversial Opinion About {topic}",
        f"How I Failed at {topic} — and What I Learned",
        f"Could {topic} Save the World?",
        f"The Beginner’s Guide to {topic} You’ll Wish You Had Sooner",
        f"{topic}: Trends, Challenges, and Predictions for the Future"
    ]

    return random.sample(templates, 5)  # Return 5 random, unique titles

st.set_page_config(page_title="Smart Blog Title Generator")

st.title("📝 Smart Blog Title Generator")
st.write("Generate catchy blog titles powered by LLaMA-3 (Groq API)")

topic = st.text_input("Enter your blog topic")

if st.button("Generate Titles"):
    if topic:
        with st.spinner("Generating..."):
            try:
                titles = generate_titles(topic)
                st.success("Here are your blog titles:")
                st.markdown(titles)
            except Exception as e:
                st.error(str(e))
    else:
        st.warning("Please enter a topic.")
