# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:58:26 2017

@author: LeRookie
"""

import json    
import pandas as pd

from collections import defaultdict

def main():
	business_df = pd.read_json('business_filtered.json', lines=True)
	business_list = business_df.business_id.tolist()

	with open('review.json', 'r', encoding="utf8") as input_file:
	    business_review_count = defaultdict(int)
	    for jsonline in input_file:
	        obj = json.loads(jsonline)
	        business_id = obj['business_id']
	        if business_id in business_list and business_review_count[business_id] < 5:
	            
	            with open('review_filtered.json', 'a') as output_file:
	                output_file.write(json.dumps(obj))
	                output_file.write('\n')
	            business_review_count[business_id] += 1

if __name__== "__main__":
	main()
