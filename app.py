# Import necessary libraries
import streamlit as st
from openai import OpenAI
from newspaper import Article

# Setting page layout
st.set_page_config(
    page_title="KeenSight-Article Summarizer",
    page_icon="✅"
)

# Function to fetch the main content from a given URL
def get_main_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Error fetching content: {e}"

# Function to generate topic summary using GPT-3.5-turbo
def generate_topic_summary(text, api_key):
    openai = OpenAI(api_key=api_key)
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a summarization assistant."},
            {"role": "user", "content": f"Summarize the following text in 10 sentences max:\n{text}"}
        ]
    )
    first_choice = completion.choices[0]
    return first_choice.message.content

# Function to perform sentiment analysis using GPT-3.5-turbo
def analyze_sentiment(text, api_key):
    openai = OpenAI(api_key=api_key)
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": f"Analyze the sentiment of the following text:\n{text} and give one line reason for that sentiment explaining why a particular sentiment is given. The response should start with 'The sentiment of this article is' "}
        ]
    )
    first_choice = completion.choices[0]
    return first_choice.message.content

# Streamlit App
def main():
    st.image('logo.png', width=200)
    st.title("Financial Article Summarizer")

    # Input field for user to provide their OpenAI API key
    user_api_key = st.text_input("Enter your OpenAI API key:", type="password")

    # Check if the user has provided an API key
    if not user_api_key:
        st.warning("Please enter your OpenAI API key.")
        st.stop()

    # Input field for user to provide URL
    url = st.text_input("Enter the URL of the financial article:")

    article_text = None  # Initialize article_text outside the try block

    if st.button("Summarize"):
        # Fetch main content from the provided URL
        try:
            article_text = get_main_content(url)

            # Generate overall topic summary
            topic_summary = generate_topic_summary(article_text, user_api_key)
            st.subheader("Topic Summary:")
            st.write(topic_summary)

            # Perform sentiment analysis
            sentiment = analyze_sentiment(article_text, user_api_key)
            st.subheader("Sentiment Analysis:")
            st.write(sentiment)

        except Exception as e:
            st.error(f"Error fetching or summarizing content: {e}")

if __name__ == "__main__":
    main()
