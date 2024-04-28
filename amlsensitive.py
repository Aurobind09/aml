import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Example text data
text_data = [
    "I love this product, it's amazing!",
    "This movie was terrible, I hated it.",
    "The restaurant service was okay, but the food was great.",
    "I feel neutral about this book.",
    "I'm not sure how I feel about this.",
    "The weather is beautiful today."
]

# Analyze sentiment for each piece of text
for text in text_data:
    sentiment_scores = sia.polarity_scores(text)
    print(f"Text: {text}")
    print(f"Sentiment Scores: {sentiment_scores}")
    if sentiment_scores['compound'] >= 0.05:
        print("Overall Sentiment: Positive")
    elif sentiment_scores['compound'] <= -0.05:
        print("Overall Sentiment: Negative")
    else:
        print("Overall Sentiment: Neutral")
    print()
