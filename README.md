# Project 2: Large-Scale Data Analysis using Hadoop MapReduce

## Dataset
us-south-260408.osm.pbf

## Goal
Analyze OpenStreetMap highway and amenity frequencies using Hadoop MapReduce.

## Preprocessing
1. Filtered the OSM PBF file with osmium
2. Exported to JSON
3. Converted to Hadoop-readable text

## Files
- mapper_highway.py
- mapper_amenity.py
- reducer_count.py
- convert_osm_stream_v2.py

## How to Run
1. Start Hadoop daemons
2. Upload sample file to HDFS
3. Run Hadoop Streaming job

## Sample Command
hadoop jar ...

## Results
Top highway values included crossing, motorway_junction, and bus_stop.
## Additional Analyses

### Amenity Frequency Analysis
We performed a MapReduce job to compute frequency of amenity types.

### Top 10 Comparison
We extracted the top 10 most frequent highway and amenity types and visualized them using bar charts.

### Visualization
Bar charts were generated using Python (matplotlib) to illustrate the distribution of features.
