
## Load in the data
- Actual loading script in `processor.py`
- Didnt include hear because it makes the notebook more messy


```python
import matplotlib.pyplot as plot
import numpy as np
```


```python
# Python script to do a lot of the data processessing and make this notebook look cleaner
import processor
dataset = processor.load_dataset()
channels = processor.process_by_chanel( dataset )
```


```python
# Pull out the important info about the trending videos into one table
# Label is the assigned cataglory
# Days to trend is publication date - trending date
dataset.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>trending_date</th>
      <th>title</th>
      <th>channel_title</th>
      <th>publish_time</th>
      <th>tags</th>
      <th>views</th>
      <th>likes</th>
      <th>dislikes</th>
      <th>comment_count</th>
      <th>description</th>
      <th>label</th>
      <th>days_to_trend</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-11-14 00:00:00+00:00</td>
      <td>WE WANT TO TALK ABOUT OUR MARRIAGE</td>
      <td>CaseyNeistat</td>
      <td>2017-11-13 17:13:01+00:00</td>
      <td>SHANtell martin</td>
      <td>748374</td>
      <td>57527</td>
      <td>2966</td>
      <td>15954</td>
      <td>SHANTELL'S CHANNEL - https://www.youtube.com/s...</td>
      <td>People &amp; Blogs</td>
      <td>0.282627</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-11-14 00:00:00+00:00</td>
      <td>Me-O Cats Commercial</td>
      <td>Nobrand</td>
      <td>2017-04-21 06:47:32+00:00</td>
      <td>cute|"cats"|"thai"|"eggs"</td>
      <td>98966</td>
      <td>2486</td>
      <td>184</td>
      <td>532</td>
      <td>Kittens come out of the eggs in a Thai commerc...</td>
      <td>People &amp; Blogs</td>
      <td>206.716991</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-11-14 00:00:00+00:00</td>
      <td>AFFAIRS, EX BOYFRIENDS, $18MILLION NET WORTH -...</td>
      <td>Shawn Johnson East</td>
      <td>2017-11-11 15:00:03+00:00</td>
      <td>shawn johnson|"andrew east"|"shawn east"|"shaw...</td>
      <td>321053</td>
      <td>4451</td>
      <td>1772</td>
      <td>895</td>
      <td>Subscribe for weekly videos ▶ http://bit.ly/sj...</td>
      <td>People &amp; Blogs</td>
      <td>2.374965</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-11-14 00:00:00+00:00</td>
      <td>BLIND(folded) CAKE DECORATING CONTEST (with Mo...</td>
      <td>Grace Helbig</td>
      <td>2017-11-11 18:08:04+00:00</td>
      <td>itsgrace|"funny"|"comedy"|"vlog"|"grace"|"helb...</td>
      <td>197062</td>
      <td>7250</td>
      <td>217</td>
      <td>456</td>
      <td>Molly is an god damn amazing human and she cha...</td>
      <td>People &amp; Blogs</td>
      <td>2.244398</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-11-14 00:00:00+00:00</td>
      <td>Wearing Online Dollar Store Makeup For A Week</td>
      <td>Safiya Nygaard</td>
      <td>2017-11-11 01:19:33+00:00</td>
      <td>wearing online dollar store makeup for a week|...</td>
      <td>2744430</td>
      <td>115426</td>
      <td>1110</td>
      <td>6541</td>
      <td>I found this online dollar store called ShopMi...</td>
      <td>People &amp; Blogs</td>
      <td>2.944757</td>
    </tr>
  </tbody>
</table>
</div>




```python
# All the channels that were on trending
# Count is number of times trended
# Stats reflect total views, likes, dislikes and comments for each video
# Days to trend is average across all trending videos
channels.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>channel</th>
      <th>count</th>
      <th>views</th>
      <th>likes</th>
      <th>dislikes</th>
      <th>comment_count</th>
      <th>days_to_trend</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ESPN</td>
      <td>203</td>
      <td>105654218</td>
      <td>937723</td>
      <td>108043</td>
      <td>387753</td>
      <td>2.132705</td>
      <td>Sports</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Tonight Show Starring Jimmy Fallon</td>
      <td>197</td>
      <td>271426383</td>
      <td>5981334</td>
      <td>187407</td>
      <td>403655</td>
      <td>3.567450</td>
      <td>Comedy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TheEllenShow</td>
      <td>193</td>
      <td>253841999</td>
      <td>6035132</td>
      <td>193602</td>
      <td>344469</td>
      <td>2.611557</td>
      <td>Entertainment</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Netflix</td>
      <td>193</td>
      <td>185818315</td>
      <td>4211072</td>
      <td>196212</td>
      <td>391350</td>
      <td>3.216193</td>
      <td>Entertainment</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Vox</td>
      <td>193</td>
      <td>122633963</td>
      <td>3272518</td>
      <td>615977</td>
      <td>558845</td>
      <td>4.479800</td>
      <td>News &amp; Politics</td>
    </tr>
  </tbody>
</table>
</div>



## Look at trending date statistics by videos


```python
# Huge disperity between median and mean
# Lets see that with data
days_to_trend_mean = dataset['days_to_trend'].mean()
days_to_trend_median = dataset['days_to_trend'].median()
print('It takes ' + str(days_to_trend_mean)[:5] + ' days to trend on average')
print('Median of only ' + str(days_to_trend_median)[:5] + ' days to trend')
```

    It takes 16.22 days to trend on average
    Median of only 4.791 days to trend
    


```python
# Looking at it below, wow, some videos take forever to trend? Lets look at that.
fig, a = plot.subplots(1,2,figsize=(10,5))
bins = np.arange( 0,4000, 100)
a[0].hist( dataset['days_to_trend'].tolist(), log=True, bins=bins )
a[0].set_title('Time till trending, log scale')
a[0].set_ylabel('Videos')
a[0].set_xlabel('Days till trending')
a[1].hist( dataset['days_to_trend'].tolist(), log=False, bins=bins )
a[1].set_title('Time till trending, linear scale')
print('Chart showing how many days some videos took to trend in a logarithmic fassion')
```

    Chart showing how many days some videos took to trend in a logarithmic fassion
    


![png](output_7_1.png)



```python
# Lets pull one of these videos to make sure
# This video was published in 2006, trended in 2018? Has only a quarter of a million views?
# So you are almost guerenteed to trend immediately or not at all, its very hard for an older video to trend
dataset[dataset['days_to_trend'] > 3000 ][:1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>trending_date</th>
      <th>title</th>
      <th>channel_title</th>
      <th>publish_time</th>
      <th>tags</th>
      <th>views</th>
      <th>likes</th>
      <th>dislikes</th>
      <th>comment_count</th>
      <th>description</th>
      <th>label</th>
      <th>days_to_trend</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7054</th>
      <td>2018-02-05 00:00:00+00:00</td>
      <td>Budweiser - Original Whazzup? ad</td>
      <td>dannotv</td>
      <td>2006-07-23 08:24:11+00:00</td>
      <td>Budweiser|"Bud"|"Whazzup"|"ad"</td>
      <td>258506</td>
      <td>459</td>
      <td>152</td>
      <td>82</td>
      <td>Original Whazzup ad - however, there is a litt...</td>
      <td>Entertainment</td>
      <td>4214.649873</td>
    </tr>
  </tbody>
</table>
</div>



## By metric breakdown


```python
# Lets get some statistics
total_trends = channels['count'].sum()
mean_trending_views = channels['views'].sum() / total_trends
mean_trending_likes = channels['likes'].sum() / total_trends
mean_trending_dislikes = channels['dislikes'].sum() / total_trends
mean_trending_comments = channels['comment_count'].sum() / total_trends
print('A trending video will have on average:')
print(str(mean_trending_views)[:10],'views')
print(str(mean_trending_likes)[:8],'likes')
print(str(mean_trending_dislikes)[:7],'dislikes')
print(str(mean_trending_comments)[:7],'comments')
```

    A trending video will have on average:
    2360784.63 views
    74266.70 likes
    3711.40 dislikes
    8446.80 comments
    


```python
# Lets plot out some statistics as to the breakdown by channel
fig, a = plot.subplots(2,2,figsize=(15,15))
def add_to_plot(dataX, dataY, i, label):
    a[i//2, i%2].scatter(dataX, dataY, label=label)
    a[i//2, i%2].set_ylabel(label)
    a[i//2, i%2].set_yscale('log')
    a[i//2, i%2].set_ylim((1,dataY.max()*2))
add_to_plot( channels['count'], channels['views'],0,'views' )
add_to_plot( channels['count'], channels['views'],1,'likes' )
add_to_plot( channels['count'], channels['dislikes'],2,'dislikes' )
add_to_plot( channels['count'], channels['comment_count'],3,'comments' )
print('Chart showing How different metrics effect trending rate')
print('X axis is number of times trended, Y axis is value of highlighted metric')
```

    Chart showing How different metrics effect trending rate
    X axis is number of times trended, Y axis is value of highlighted metric
    


![png](output_11_1.png)



```python
# All the charts above look quite similer and seem fairly strongly coorilated
# Notice that there seems to be a hard cutoff on views though, you have to have a certain amount of views to trend.
# Lets look at that in more detail
```

## By Channel breakdown


```python
# Lets see if all channels are treated equally here
# Take top 50 channels by views
high_views = channels[:50]
fig, a = plot.subplots(figsize=(7,7))
a.scatter(channels['count'], channels['views'])
a.scatter(high_views['count'], high_views['views'])
a.set_ylabel('views of high trending channels')
a.set_yscale('log')
a.set_ylim((1,channels['views'].max()*2))
print('High trending channels seem to have nothign to do with views')
print('They have to have a certain cuttof it seems, but after a point it doesnt matter')
print('Interesting to note that these top trending channels dont get more views, infact they get less per video?')
```

    High trending channels seem to have nothign to do with views
    They have to have a certain cuttof it seems, but after a point it doesnt matter
    Interesting to note that these top trending channels dont get more views, infact they get less per video?
    


![png](output_14_1.png)



```python
# So what does it mean that you can trend over and over but not get many more views than someone who doenst?
```

## By Category breakdown


```python
fig, a = plot.subplots(figsize=(7,7))
def chart_views ( label ):
    data = channels[ channels['label'] == label ]
    a.scatter(data['count'], data['views'], label = label)
    a.set_ylim((1,channels['views'].max()*2))
    a.set_yscale('log')
all_cats = channels['label'].unique()
for cat in all_cats:chart_views(cat)
plot.legend()
print('messy chart that shows categlory breakdowns by views')
```

    messy chart that shows categlory breakdowns by views
    


![png](output_17_1.png)



```python
# Lets see this breakdown in more detail
fig, a = plot.subplots(4,4,figsize=(20,20))
def chart_views ( label, i ):
    chart = a[i//4,i%4]
    data = channels[ channels['label'] == label ]
    chart.scatter(channels['count'], channels['views'], c='grey')
    chart.scatter(data['count'], data['views'], label = label,c='red')
    chart.set_ylim((1,channels['views'].max()*2))
    chart.set_yscale('log')
    chart.set_title(label)
all_cats = channels['label'].unique()
for (i,cat) in enumerate(all_cats): chart_views(cat,i)
print('Red indicates where each cataeglory falls in the overall rankings, clearly some get trend more than others')
```

    Red indicates where each cataeglory falls in the overall rankings, clearly some get trend more than others
    


![png](output_18_1.png)



```python
# Cutting off all data after 10^6 views, lets see where the average video channel falls on the trending amount
fig, a = plot.subplots(4,4,figsize=(20,20))
points = []
def chart_views ( label, i ):
    chart = a[i//4,i%4]
    data = channels[ channels['label'] == label][channels['views'] > 10000000 ]
    chart.scatter(channels['count'], channels['views'], c='grey')
    chart.scatter(data['count'], data['views'], label = label,c='black')
    _x = data['count'].mean()
    _y = data['views'].mean()
    chart.scatter([_x],[_y], label = label,c='purple')
    chart.set_ylim((1,channels['views'].max()*2))
    chart.set_yscale('log')
    chart.set_title(label)
    points.append((label,_x,_y))
all_cats = channels['label'].unique()
for (i,cat) in enumerate(all_cats): chart_views(cat,i)
print('Purlple indicates average channel with more than 10M views trended')
```

    C:\ProgramData\Anaconda3\lib\site-packages\ipykernel_launcher.py:6: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
      
    

    Purlple indicates average channel with more than 10M views trended
    


![png](output_19_2.png)



```python
# Lets see how these breakdown
fig, a = plot.subplots(figsize=(10,10))
for (i,x,y) in points:
    a.scatter(x,y)
    if ( i == 'Science & Technology'):
        a.annotate(i,(x + 1,y - 10000000))
    else:
        a.annotate(i,(x + 1,y + 10000))
a.set_ylim((10000000,1000000000))
a.set_yscale('log')
a.set_ylabel('Number of views trended on average')
a.set_xlabel('Number of times trended on anverage per chanel')
plot.legend()
```

    No handles with labels found to put in legend.
    




    <matplotlib.legend.Legend at 0x2203c25bf60>




![png](output_20_2.png)


## By Tag Topic breakdown


```python
import re
import collections
import pandas as pd
```


```python
# First of all, how many tags should you have?
tag_dataset = pd.DataFrame()
tag_dataset['tag_num'] = dataset['tags'].str.split('|').str.len()
tag_dataset['views'] = dataset['views']
tag_dataset[:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tag_num</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>748374</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>98966</td>
    </tr>
    <tr>
      <th>2</th>
      <td>44</td>
      <td>321053</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>197062</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25</td>
      <td>2744430</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Lets see how video views relate to tag numbers
fig, a = plot.subplots(figsize=(7,7))
group = tag_dataset.groupby('tag_num').mean().reset_index().rolling(4).mean()
a.scatter(tag_dataset['tag_num'],tag_dataset['views'])
a.scatter(group['tag_num'],group['views'])
a.set_ylabel('Number of views for video')
a.set_xlabel('Number of tags used ')
a.set_yscale('log')
print('Blue are videos, yellow is rollind average')
```

    Blue are videos, yellow is rollind average
    


![png](output_24_1.png)



```python
# What are top videos actually about by tag
pattern = re.compile('[^\|a-zA-Z0-9_]+')
all_tags = '|'.join(dataset['tags']).lower
all_tags = pattern.sub('', all_tags)
all_tags = all_tags.split('|')
print('found ' + str(len(all_tags)) + ' tags')
```

    found 808183 tags
    


```python
# Lets look at top used tags
counter=collections.Counter(all_tags)
print('Videos trended by tag')
counter.most_common(10)
```

    Videos trended by tag
    




    [('', 8410),
     ('funny', 4142),
     ('comedy', 3647),
     ('howto', 2026),
     ('music', 1667),
     ('pop', 1634),
     ('none', 1537),
     ('makeup', 1504),
     ('trailer', 1413),
     ('2018', 1282)]




```python
# Didnt know how to do this with pandas, so its slow in a double for look ;/
tags_by_video = dataset['tags'].str.split('|').tolist()
views_by_video = dataset['views']
combined = dict () 
for i in range(len(tags_by_video)):
    for tag in tags_by_video[i]:
        t = pattern.sub('', tag).lower()
        if combined.get(t):
            combined[t][0] += views_by_video[i]
            combined[t][1] += 1
        else:
            combined[t] = [views_by_video[i],1]
    if i % 10000 == 0: print(str(i/len(tags_by_video))[:5] + '%')
print('processing. . .')
```

    0.0%
    0.244%
    0.488%
    0.732%
    0.976%
    processing. . .
    


```python
# Create a dataframe to show the tags
rows = [ {'tag':a,'views':b,'trends':c} for a,(b,c) in combined.items() ]
tagsData = pd.DataFrame( rows)
```


```python
tagsData = tagsData.drop([tagsData.index[116]])
```


```python
# Clearly music tags trend in most views, but not most number of times
tagsData.sort_values(by='views',ascending=False)[:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tag</th>
      <th>trends</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2692</th>
      <td>pop</td>
      <td>1634</td>
      <td>11327075747</td>
    </tr>
    <tr>
      <th>3595</th>
      <td>rap</td>
      <td>382</td>
      <td>6609541543</td>
    </tr>
    <tr>
      <th>23</th>
      <td>funny</td>
      <td>4142</td>
      <td>6459300503</td>
    </tr>
    <tr>
      <th>48</th>
      <td>comedy</td>
      <td>3647</td>
      <td>5759029286</td>
    </tr>
    <tr>
      <th>715</th>
      <td>musicvideo</td>
      <td>753</td>
      <td>4919357940</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Comedy is dramaticly more likely to trend again when compaired to musical tags
tagsData.sort_values(by='trends',ascending=False)[:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tag</th>
      <th>trends</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23</th>
      <td>funny</td>
      <td>4142</td>
      <td>6459300503</td>
    </tr>
    <tr>
      <th>48</th>
      <td>comedy</td>
      <td>3647</td>
      <td>5759029286</td>
    </tr>
    <tr>
      <th>111</th>
      <td>howto</td>
      <td>2026</td>
      <td>3527731838</td>
    </tr>
    <tr>
      <th>708</th>
      <td>music</td>
      <td>1667</td>
      <td>2821610384</td>
    </tr>
    <tr>
      <th>2692</th>
      <td>pop</td>
      <td>1634</td>
      <td>11327075747</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Try charting this data
fig, a = plot.subplots(figsize=(7,7))
a.scatter(tagsData['trends'], tagsData['views'])
a.set_ylabel('Number of views for tag')
a.set_xlabel('Number of trends for tag')
print('Not sure if this plot is usefull')
```

    Not sure if this plot is usefull
    


![png](output_32_1.png)


## Finaly, I want to see if telling people like a video actually gets more likes?
Just curious about that


```python
like_dataset=pd.DataFrame()
like_dataset['ask_to_like'] = dataset['description'].str.contains("like")
like_dataset['likes'] = dataset['likes']
like_dataset.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ask_to_like</th>
      <th>likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>57527</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>2486</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>4451</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>7250</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>115426</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Wow! thats actually fairly decisive
asked_likes = like_dataset[ like_dataset['ask_to_like'] == True]['likes'].mean()
didnt_ask_likes = like_dataset[ like_dataset['ask_to_like'] == False ]['likes'].mean()
print('If asked, mean of ' + str(asked_likes)[:8] )
print('If didnt asked, mean of ' + str(didnt_ask_likes)[:8] )
print('You saw it here, asking people to leave a video a like actually gets you less likes! ')
```

    If asked, mean of 60704.67
    If didnt asked, mean of 77105.84
    You saw it here, asking people to leave a video a like actually gets you less likes! 
    

## Conclusions

What requirements are their to get your video trending?
- You seem to need a certain amount of views and engagement 
- It helps to be have your video in a few key cataglories 
- When looking at Frequently Trending Channels:
    - Education, comedy & News channels trend more and with fewer views than anyone else others
    - Music channels will often trend, but only with a high view count, and you shouldnt expect to trend often
    - Gaming chanels are even less likely to trend frequently and need a similarly high number of views
    - News, Comody, and Entertainment channels are amung the most over-represented chanels on the trending list
        - Trending hundreds of times with less views than many music video chanels
- Trending before is a high likelyhood of trending again

How long till you trend?
- Trending will happen withing a few days and sharply falls off after that
- Some select older videos will pop on after a while, but reletively rare
- Trend in the first 3 days or dont trend at all if true in vast majority of cases

What metrics dont matter?
- Dislikes dont seem to effect trending at all
- Views, after about 5 Million, do not have any impact it seems

What helps the video do well?
- Aparently asking for likes is not helpful in getting likes
- Tags by themselves dont seem to indicate much
    - However, you get optimal views with 5ish tags, the more tags the lower the views
    - More than 60 tags and views start to fall fast
    - However, that is relative to other good videos, so += 10 Milion views isnt much in that ranking


```python

```
