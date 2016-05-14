
# coding: utf-8

# In[13]:

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


# In[4]:

#load data to plot geographically
get_ipython().magic(u"time sep_trips = pd.read_csv('yellow_tripdata_2015-09.csv',usecols=     ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude','dropoff_latitude', 'passenger_count'])")

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

sep_trips['dropoff_x'] = map(longToWebMerc,sep_trips['dropoff_longitude'])
sep_trips['dropoff_y'] = map(latToWebMerc,sep_trips['dropoff_latitude'])
sep_trips['pickup_x'] = map(longToWebMerc,sep_trips['pickup_longitude'])
sep_trips['pickup_y'] = map(latToWebMerc,sep_trips['pickup_latitude'])


# In[5]:

#initialize the bokeh notebooks
output_notebook()


# In[24]:

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


# In[23]:

samples = sep_trips.sample(n=10000)
p = base_plot()
p.add_tile(STAMEN_TERRAIN)
p.circle(x=samples['dropoff_x'], y=samples['dropoff_y'], **options)
show(p)


# In[25]:

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(sep_trips, 'dropoff_x', 'dropoff_y',  ds.count('passenger_count'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[27]:

#this plots all where pickups is greater than dropoffs in red and where the number of dropoffs greater than pickups in blue

def merged_images(x_range, y_range, w, h, how='log'):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    picks = cvs.points(sep_trips, 'pickup_x',  'pickup_y',  ds.count('passenger_count'))
    drops = cvs.points(sep_trips, 'dropoff_x', 'dropoff_y', ds.count('passenger_count'))
    more_drops = tf.interpolate(drops.where(drops > picks), cmap=["lightblue", 'blue'], how=how)
    more_picks = tf.interpolate(picks.where(picks > drops), cmap=["lightpink", 'red'],  how=how)
    img = tf.stack(more_picks,more_drops)
    return tf.dynspread(img, threshold=0.1, max_px=4)

p = base_plot()
InteractiveImage(p, merged_images)


# In[ ]:




# In[ ]:




# In[ ]:



