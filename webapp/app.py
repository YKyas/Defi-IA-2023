import gradio as gr
import joblib
import pandas as pd 
from prepare import *

def tester(city, language, stock ,date_min, date_max, mobile, group, brand,parking, pool, children_policy):
    regressor_xgb=joblib.load("../models/regressor_xgb.joblib")
    date = date_max-date_min
    data = [[stock, city, date, language, mobile, group, brand, parking, pool, children_policy]]
    sample = pd.DataFrame(data, columns=['stock', 'city', 'date', 'language', 'mobile', 'group', 'brand', 'parking', 'pool', 'children_policy'])
    df_embed = target_embedding(sample)
    y_hat = regressor_xgb.predict(df_embed)
    print(y_hat)
    return y_hat
title = "1001 Nights Project : Prédire le prix d'une réservation d'hôtel"

head = (
  "<center>"
  "<img src=\"https://drive.google.com/uc?id=1y3Bjc0tt3W49vnR2DqnkBFzMZy53NTyd\" height=\"500\">"
  "</center>"
)
demo = gr.Interface(
            fn=tester,
            inputs=[gr.Dropdown(['amsterdam', 'copenhagen', 'madrid', 'paris', 'rome', 'sofia', 'valletta', 'vienna', 'vilnius'],value="Amsterdam",label="Choose the city where you want to stay"),
            gr.Dropdown(['austrian', 'belgian', 'bulgarian', 'croatian', 'cypriot', 'czech', 'danish', 'dutch',
             'estonian', 'finnish', 'french', 'german', 'greek', 'hungarian', 'irish', 'italian',
             'latvian', 'lithuanian', 'luxembourgish', 'maltese', 'polish', 'portuguese', 'romanian',
             'slovakian', 'slovene', 'spanish', 'swedish'],value="finnish",label="Choose the langage of your search"),
            gr.Slider(0, 284, step=1,label="Choose the availability of your hotel"),
            gr.Slider(0, 44, step=1,label= "Choose the date of your arrival"),
            gr.Slider(0, 44, step=1,label="Choose the end date of your stay"),
            "checkbox",
            gr.Dropdown(['Independant', 'Accar Hotels', 'Yin Yang', 'Boss Western', 'Morriott International'],value="finnish",label="Choose the brand of your hotel"),
            gr.Dropdown(['Independant', 'Boss Western', 'J.Halliday Inn', 'Safitel', 'Royal Lotus'],value="finnish",label="Choose the group of your hotel"),
            "checkbox",
            "checkbox",
            "checkbox"],
            outputs=["number"],
            title=title,description=head)

demo.launch(server_name="0.0.0.0",share=True)
