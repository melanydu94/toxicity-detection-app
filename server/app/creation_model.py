from detoxify import Detoxify    
import pandas as pd


def sentiment_scores(sentence):
    results = Detoxify(checkpoint="server/app/toxic_original-c1212f89.ckpt", device="cpu").predict(sentence)
    df = pd.DataFrame(results, index=sentence).round(5)
    my_dict = df.rename_axis('sentence').reset_index().to_dict('index')
    response_dict = list(my_dict.values())[0]
    return response_dict 
