# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

def main():
	df = pd.read_json('business.json', lines=True)

	# Filter to only include Food and Restaurants businesses
	df = df[df.categories.map(lambda x: 'Food' in x) | \
	        df.categories.map(lambda x: 'Restaurants' in x)]

	# Filter out businesses with low review counts
	df = df[df.review_count >= 5]

	# Select only relevant columns
	df = df[['business_id', 'categories', 'name']]

	df.to_json('business_filtered.json', orient='records', lines=True)

if __name__== "__main__":
	main()
