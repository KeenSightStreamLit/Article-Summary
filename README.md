# KeenSight-Article Summarizer

This is a Streamlit app that utilizes OpenAI's GPT-3.5-turbo model and the `newspaper` library to summarize financial articles and perform sentiment analysis. The app allows users to input a URL of a financial article and provides them with a summarized version of the article's main content and an analysis of its sentiment.

## Installation

To run this app locally, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required libraries using `pip3 install -r requirements.txt`.

## Usage

1. Obtain your OpenAI API key and paste it into the designated input field in the app.
2. Enter the URL of the financial article you want to summarize in the provided input field.
3. Click the "Summarize" button to generate the topic summary and perform sentiment analysis.

## Features

- **Topic Summary:** The app uses the GPT-3.5-turbo model to generate a concise summary of the main content of the financial article.
- **Sentiment Analysis:** It also utilizes the same model to analyze the sentiment of the article and provides a one-line reason explaining why a particular sentiment is given.

## Functionality

- The `get_main_content` function fetches the main content from the provided URL using the `newspaper` library.
- The `generate_topic_summary` function uses the OpenAI API to generate a topic summary based on the extracted text.
- The `analyze_sentiment` function performs sentiment analysis on the extracted text using the OpenAI API.
- The Streamlit app integrates these functions to provide a user-friendly interface for summarizing financial articles and analyzing their sentiment.

## Notes

- Ensure you have a stable internet connection to fetch article content and utilize the OpenAI API.
- Properly handle your OpenAI API key to maintain security and compliance.

**Disclaimer:** This app is for demonstration purposes only and may require proper configuration and usage guidelines in a production environment. Use it responsibly and comply with OpenAI's terms of service and usage policies.