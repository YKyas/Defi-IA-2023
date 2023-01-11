import pandas as pd
import numpy as np 

def target_embedding(df_original):
    cities = ['amsterdam', 'copenhagen', 'madrid', 'paris', 'rome', 'sofia', 'valletta', 'vienna', 'vilnius']
    languages = ['austrian', 'belgian', 'bulgarian', 'croatian', 'cypriot', 'czech', 'danish', 'dutch',
                'estonian', 'finnish', 'french', 'german', 'greek', 'hungarian', 'irish', 'italian',
                'latvian', 'lithuanian', 'luxembourgish', 'maltese', 'polish', 'portuguese', 'romanian',
                'slovakian', 'slovene', 'spanish', 'swedish']
    groups = ['Morriott International','Chillton Worldwide','Independant','Accar Hotels','Yin Yang','Boss Western']
    brands = ['Chill Garden Inn','Morriot','Royal Lotus','Corlton','Independant','Ibas','Navatel','Ardisson',
    'Marcure','Safitel','Boss Western','J.Halliday Inn','8 Premium','Tripletree','CourtYord','Quadrupletree']

    city_mean=pd.read_csv("../processed_data/city_mean.csv", index_col=0).to_dict('records')[0]
    language_mean=pd.read_csv("../processed_data/language_mean.csv", index_col=0).to_dict('records')[0]
    group_mean=pd.read_csv("../processed_data/group_mean.csv", index_col=0).to_dict('records')[0]
    brand_mean=pd.read_csv("../processed_data/brand_mean.csv", index_col=0).to_dict('records')[0]
   
    new_df = df_original.copy()
    
    #city
    dfs = []
    for city in cities:
        rslt_df = new_df[new_df['city'] == city]
        rslt_df['city'] = city_mean[city]
        dfs.append(rslt_df)
    new_df = pd.concat(dfs)

    
    #language
    dfs = []
    for language in languages:
        rslt_df = new_df[new_df['language'] == language]
        rslt_df['language'] = language_mean[language]
        dfs.append(rslt_df)
    new_df = pd.concat(dfs)

    
    #group
    dfs = []
    for group in groups:
        rslt_df = new_df[new_df['group'] == group]
        rslt_df['group'] = group_mean[group]
        dfs.append(rslt_df)
    new_df = pd.concat(dfs)
    
    
    #brand
    dfs = []
    for brand in brands:
        rslt_df = new_df[new_df['brand'] == brand]
        rslt_df['brand'] = brand_mean[brand]
        dfs.append(rslt_df)
    new_df = pd.concat(dfs)
    new_df = new_df.sort_index(ascending=True)
    
    return new_df

