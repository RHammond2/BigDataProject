
# coding: utf-8

# In[1]:

#import all necessary packages
import pandas as pd
import numpy as np
import seaborn as sns
import datashader as ds
import dask.dataframe as dd
import math
import matplotlib


from datetime import datetime, timedelta
from bokeh.plotting import figure, output_notebook, show, output_file
from IPython.core.display import HTML, display
from bokeh.tile_providers import STAMEN_TERRAIN
from datashader.callbacks import InteractiveImage
from datashader import transfer_functions as tf
from datashader.colors import Greys9,Hot,inferno,viridis

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
#x_range = ( -8280656,-8175066)
#y_range = (4940514,4998954)
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


# In[2]:

df = dd.read_csv('picks_webmerc',names=['p_d_status','time','long','lat','web_long','web_lat','temp','PCP01','passenger_count',                                 'trip_distance','tip_amount','tolls_amount','total_amount'])

df.head()


# In[3]:

#draw data by passenger count

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'web_long', 'web_lat',  ds.count('passenger_count'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)
#output_file("Pickups_passengers.png")


# In[ ]:

#draw data by passenger count

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'web_long', 'web_lat',  ds.count('trip_distance'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[ ]:

#draw data by passenger count

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'web_long', 'web_lat',  ds.count('tolls_amount'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(1200*1.5))
InteractiveImage(p, create_image)


# In[ ]:

#draw data by passenger count

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'web_long', 'web_lat',  ds.count('total_amount'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(1200*1.5))
InteractiveImage(p, create_image)


# In[ ]:

#draw data by precipitation

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'web_long', 'web_lat',  ds.count('PCP01'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)


# In[ ]:

#draw data by temperature

def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'web_long', 'web_lat',  ds.count('temp'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)

