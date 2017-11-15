# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:25:20 2017

@author: LeRookie
"""
import pandas as pd

review_df = pd.read_json('./yelp_dataset/dataset/review_filtered.json', lines=True)

# Select only the important columns
review_df = review_df[['business_id', 'text']]

# Concatenate the texts
review_df = review_df.groupby('business_id')['text'].apply(lambda x: "%s" % '\n\r'.join(x)).to_frame().reset_index()

business_df = pd.read_json('./yelp_dataset/dataset/business_filtered.json', lines=True)

combined_df = pd.merge(business_df, review_df, on='business_id')

combined_df.to_json('./yelp_dataset/dataset/combined_review.json', orient='records', lines=True)