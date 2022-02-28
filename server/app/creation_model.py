from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def response_dict(sentiment, pos_score, neu_score, neg_score):
    my_dict = {
        "Sentiment": sentiment,
        "Rating_Positive": pos_score,
        "Rating_Neutral": neu_score,
        "Rating_Negative": neg_score,
    }
    return my_dict

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        sent = "Positive"
    elif sentiment_dict['compound'] <= - 0.05:
        sent = "Negative"
    else:
        sent = "Neutral"
    return response_dict(sent, round(sentiment_dict['pos'], 2), round(sentiment_dict['neu'], 2), round(sentiment_dict['neg'], 2))
    


