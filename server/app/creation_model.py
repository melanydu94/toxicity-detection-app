from detoxify import Detoxify    
import pandas as pd
from torch import set_rng_state


def sentiment_scores(sentence):
    results = Detoxify(checkpoint="../model/toxic_original-c1212f89.ckpt", device="CUDA").predict(sentence)
    # print(pd.DataFrame(results, index=sentence).round(5).to_json(orient="index"))
    df = pd.DataFrame(results, index=sentence).round(5)
    my_dict = df.rename_axis('sentence').reset_index().to_dict('index')
    response_dict = list(my_dict.values())[0]
    return response_dict 
# print(sentiment_scores(["I HATE YOU!!!!!!!", "I LOVE YOU !!!!"]))
