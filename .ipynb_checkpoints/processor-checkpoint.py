import os
import pandas as pd
import json

paths = { 
	'cataglories' : 'cataglories.json',
	'videos' : 'USvideos.csv'
}

def load_dataset () :

	# Video Data
	raw_videoData = pd.read_csv( paths['videos'] )

	# Cataglory data
	with open( paths['cataglories']) as f: 
		raw_jsonData = json.load(f)
	raw_jsonData = pd.DataFrame([ 
		{'label': item['snippet']['title'], 'id' : item['id']}  
		for (i,item) in enumerate(list(raw_jsonData['items'])) 
	])
	raw_jsonData['id'] = raw_jsonData['id'].astype(int)
	
	# Combined
	combined_data = raw_videoData.merge(raw_jsonData, left_on='category_id', right_on='id')
	combined_data = combined_data.reindex(columns=['trending_date', 'title', 'channel_title', 'publish_time','tags','views','likes','dislikes','comment_count','description','label'])

	# Process times
	trending_time = pd.to_datetime('20' + combined_data['trending_date'], format="%Y.%d.%m").dt.tz_localize('UTC')
	publish_time = pd.to_datetime(combined_data['publish_time'])

	combined_data['trending_date'] = trending_time
	combined_data['publish_time'] = publish_time
	combined_data['days_to_trend'] = ( combined_data['trending_date'] - combined_data['publish_time'] ) / pd.to_timedelta(1, unit='D')

	return combined_data

def process_by_chanel ( combined_data ) :
	
	trending_by_channel = pd.DataFrame( combined_data['channel_title'].value_counts() )
	trending_by_channel = pd.DataFrame({ 'channel' : trending_by_channel.index, 'count' : trending_by_channel['channel_title']}).reset_index(drop=True)

	channel_total_metrics = combined_data.groupby('channel_title').sum()
	trending_by_channel = trending_by_channel.merge(channel_total_metrics, left_on='channel', right_on='channel_title')
	trending_by_channel['days_to_trend'] = trending_by_channel['days_to_trend'] / trending_by_channel['count']

	cataglories = pd.DataFrame(combined_data.groupby('channel_title')['label'].first())
	trending_by_channel = trending_by_channel.merge(cataglories, left_on='channel', right_on='channel_title')

	return trending_by_channel
