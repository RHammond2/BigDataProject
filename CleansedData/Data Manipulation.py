
# coding: utf-8

# In[20]:

#import all necessary packages
import pandas as pd
import numpy as np
import seaborn as sns
import datashader as ds
import math
import matplotlib

from datetime import datetime, timedelta
from bokeh.plotting import figure, output_notebook, show, output_file
from IPython.core.display import HTML, display
from bokeh.tile_providers import STAMEN_TERRAIN
from datashader.callbacks import InteractiveImage
from datashader.colors import Hot, inferno
from datashader import transfer_functions as tf
from datashader.colors import Greys9

get_ipython().magic(u'matplotlib inline')

#change coordinates to a web mercator projection
#Functions are altered from: http://www.neercartography.com/latitudelongitude-tofrom-web-mercator/
def longToWebMerc(x):
    if abs(x) > 180:
        return 0
    semimajorAxis = 6378137.0  # WGS84 spheriod semimajor axis
    east = x * 0.017453292519943295
    easting = semimajorAxis * east
    return easting

def latToWebMerc(y):
    if abs(y) > 90:
        return 0
    north = y * 0.017453292519943295
    northing = 3189068.5 * math.log((1.0 + math.sin(north)) / (1.0 - math.sin(north)))
    return northing

#initialize the bokeh notebooks
output_notebook()

x_range=(-8250000,-8210000)
y_range=(4965000,4990000)
options = dict(line_color=None, fill_color='darkslateblue', size=1)

def base_plot(tools='pan,wheel_zoom,save,reset',plot_width=900, plot_height=600, **plot_args):
    p = figure(tools=tools, plot_width=plot_width, plot_height=plot_height,
        x_range=x_range, y_range=y_range, outline_line_color=None,
        min_border=0, min_border_left=0, min_border_right=0,
        min_border_top=0, min_border_bottom=0, **plot_args)
    
    p.axis.visible = False
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    return p

from IPython.core.display import HTML, display
display(HTML("<style>.container { width:90% !important; }</style>"))


# In[51]:

df1 = pd.read_csv('part-00000',sep=',')#,usecols=['p_d_status','pickup_longitude','pickup_latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount'])
#df1 = df1['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']
'''
df2 = pd.read_csv('part-00001',sep=',',names = cols)
df2 = df2[['pickup_longitude','pickup_latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df3 = pd.read_csv('part-00002',sep=',',names = cols)
df3 = df3[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df4 = pd.read_csv('part-00003',sep=',',names = cols)
df4 = df4[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df5 = pd.read_csv('part-00004',sep=',',names = cols)
df5 = df5[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df6 = pd.read_csv('part-00005',sep=',',names = cols)
df6 = df6[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df7 = pd.read_csv('part-00006',sep=',',names = cols)
df7 = df7[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df8 = pd.read_csv('part-00007',sep=',',names = cols)
df8 = df8[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df9 = pd.read_csv('part-00008',sep=',',names = cols)
df9 = df9[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df10 = pd.read_csv('part-00009',sep=',',names = cols)
df10 = df10[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df11 = pd.read_csv('part-00010',sep=',',names = cols)
df11 = df11[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df12 = pd.read_csv('part-00011',sep=',',names = cols)
df12 = df12[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df13 = pd.read_csv('part-00012',sep=',',names = cols)
df13 = df13[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df14 = pd.read_csv('part-00013',sep=',',names = cols)
df14 = df14[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df15 = pd.read_csv('part-00014',sep=',',names = cols)
df15 = df15[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df16 = pd.read_csv('part-00015',sep=',',names = cols)
df16 = df16[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df17 = pd.read_csv('part-00016',sep=',',names = cols)
df17 = df17[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df18 = pd.read_csv('part-00017',sep=',',names = cols)
df18 = df18[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df19 = pd.read_csv('part-00018',sep=',',names = cols)
df19 = df19[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df20 = pd.read_csv('part-00019',sep=',',names = cols)
df20 = df20[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df21 = pd.read_csv('part-00020',sep=',',names = cols)
df21 = df21[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df22 = pd.read_csv('part-00021',sep=',',names = cols)
df22 = df22[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df23 = pd.read_csv('part-00022',sep=',',names = cols)
df23 = df23[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
df24 = pd.read_csv('part-00023',sep=',',names = cols)
df24 = df24[['longitude','latitude','passenger_count','PCP01','trip_distance','temp','tolls_amount']]
'''


# In[49]:

#concatenate dataframes and map the lat,longs to web mercator
#frames = [df1,df2,df3,df4,df5,df6,df7,df8,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24]
#frames = [df1,df2]
#all_points = pd.concat(frames)
#create two separate dataframes one for each of pickups and dropoffs

#p_d_status,month,time,direction,speed,gust,cloud_ceiling,sky_cover,low_cloud,middle_cloud,high_cloud,visibility,temp,dewpoint,sea_level_pressure,altimeter,station_pressure,max_temp,min_temp,PCP01,PCP06,PCP24,PCPXX,snow_depth,pickup_longitude,pickup_latitude,passenger_count,trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount	
'''
df = df1.rename(columns={'$direction':'$speed','$speed':'gust','$gust':'cloud_ceiling','$cloud_ceiling':'sky_cover',\
                        '$sky_cover':'low_cloud','$low_cloud':'middle_cloud','$middle_cloud':'high_cloud',\
                        '$high_cloud':'visibility','$visibility':'temp','$temp':'dewpoint','$dewpoint':'sea_level_pressure',\
                        '$sea_level_pressure':'altimeter','$altimeter':'station_pressure','$station_pressure':'max_temp',\
                        '$max_temp':'min_temp','$min_temp':'PCP01','$PCP01':'PCP06','$PCP06':'PCP24','$PCP24':'PCPXX',\
                        '$PCPXX':'snow_depth','$snow_depth':'pickup_longitude','$pickup_longitude':'pickup_latitude',\
                        '$pickup_latitude':'passenger_count','$passenger_count':'trip_distance',\
                        '$trip_distance':'fare_amount','$fare_amount':'extra','$extra':'mta_tax','$mta_tax':'tip_amount',\
                        '$tip_amount':'tolls_amount','$tolls_amount':'improvement_surcharge','$improvement_surcharge':'total_amount'},inplace=True)
'''


# In[57]:

df = df1[['p_d_status','snow_depth','pickup_longitude','pickup_latitude','passenger_count','min_temp','trip_distance','visibility','tip_amount','mta_tax']]
df.head()


# In[58]:

picks = df.loc[df['p_d_status'] == 'p']
drops = df.loc[df['p_d_status'] == 'd']
picks.head(5)


# In[60]:

picks['x'] = map(longToWebMerc,picks['snow_depth'])
picks['y'] = map(latToWebMerc,picks['pickup_longitude'])
picks.head()


# In[61]:

#draw all 12 months of data by passenger count

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(picks, 'x', 'y',  ds.count('pickup_latitude'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[62]:

#draw all twelve months of data by trip distance
def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(picks, 'x', 'y',  ds.count('passenger_count'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[63]:

#draw all twelve months of data by tolls amount
def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(picks, 'x', 'y',  ds.count('tip_amount'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[64]:

#draw all twelve months of data by precipitation
def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(picks, 'x', 'y',  ds.count('min_temp'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[65]:

#draw all twelve months of data by temp
def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(picks, 'x', 'y',  ds.count('visibility'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



