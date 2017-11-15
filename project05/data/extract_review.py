# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:58:26 2017

@author: LeRookie
"""

import json    
import pandas as pd

from collections import defaultdict

business_df = pd.read_json('./yelp_dataset/dataset/business_filtered.json', lines=True)
business_list = business_df.business_id.tolist()

with open('./yelp_dataset/dataset/review.json', 'r', encoding="utf8") as input_file:
#    count = 0
    business_review_count = defaultdict(int)
    for jsonline in input_file:
#        if count >= 500:
#            break
        obj = json.loads(jsonline)
        business_id = obj['business_id']
        if business_id in business_list and business_review_count[business_id] < 5:
            
            with open('./yelp_dataset/dataset/review_filtered.json', 'a') as output_file:
                output_file.write(json.dumps(obj))
                output_file.write('\n')
#            print(obj)
            business_review_count[business_id] += 1
#        count += 1
