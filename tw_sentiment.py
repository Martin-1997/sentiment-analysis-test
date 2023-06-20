from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np

# Preprocessing according to the models requirements
def preprocess_tweet(tweet):
    tweet_words = []
    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = 'http'
        elif word.startswith('\n'):
            word = " "
        tweet_words.append(word)
    tweet_processed = " ".join(tweet_words)
    return tweet_processed

# load model and tokenizer
def load_roberta_model_tokenizer():
    roberta = "cardiffnlp/twitter-roberta-base-sentiment"
    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)
    return tokenizer, model

# sentiment analysis
def analyze_tweet(tokenizer, model, tweet):
    encoded_tweet = tokenizer(tweet, return_tensors='pt')
    output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
    # print(output)
    scores = output[0][0].detach().numpy()
    scores_softmax = softmax(scores)
    # Define labels to express sentiment in numbers
    labels = [-1, 0, 1]
    # Multiply scores and labels element-wise and sum it up to get a optimism score
    # 1: Totally optimistic
    # 0: Neutral
    # -1: Totally pessimistic
    optimism_score = np.sum(np.multiply(scores_softmax, labels))
    # print(f"Tweet to analyze: {encoded_tweet}")
    # print(f"optimism_score: {optimism_score}")
    return optimism_score
