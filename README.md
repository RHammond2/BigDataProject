# BigDataProject
DS-GA 1004 Big Data Spring 2016 Taxi and Weather Analysis

There are 3 MapReduce processes in the code.

The first MapReduce to be run is the map_join.py and reduce.join.py in the DataCleanse folder, which filters out all weather data that does not have the minute reading equal to 51, and then converts the datetime in the taxi data to match that of the weather data, e.g., all minute readings equal to 51.

The second MapReduce to be run is the map_cleanse.py and reduce_cleanse.py in the DataClenase folder. In this step all bad readings from the taxi data are filtered out. This includes (0,0) lat/long readings, zero passengers, zero trip distance, and any monetary value less than zero or passenger count and trip distances less than zero.

The third step in the MapReduce aggregates all trip data to the hour to sum and count the appropriate fields. From here we are able to work on the actual analysis of the data.
