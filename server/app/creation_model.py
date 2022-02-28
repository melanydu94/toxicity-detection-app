from detoxify import Detoxify    
import pandas as pd



def response_dict(toxic_score, sev_toxic_score, obscene_score, threat_score, insult_score, id_hate_score):
    my_dict = {
        "toxic": toxic_score,
        "severe_toxic": sev_toxic_score,
        "obscene": obscene_score,
        "threat": threat_score,
        "insult": insult_score,
        "identity_hate": id_hate_score
    }
    return my_dict

def sentiment_scores(sentence):
    results = Detoxify('original').predict(sentence)
    # print(pd.DataFrame(results, index=sentence).round(5).to_json(orient="index"))
    return pd.DataFrame(results, index=sentence).round(5).to_dict('index')
    
print(sentiment_scores(["I HATE YOU!!!!!!!", "I LOVE YOU !!!!"]))
