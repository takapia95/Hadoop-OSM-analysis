# Project 2: Large-Scale Data Analysis using Hadoop MapReduce

## Overview
This project demonstrates large-scale data processing using Hadoop MapReduce. We analyze OpenStreetMap (OSM) data to extract insights about transportation infrastructure and public amenities in the US South region.

---

## Dataset
- **Source:** OpenStreetMap (Geofabrik)
- **File:** `us-south-260408.osm.pbf`
- **Size:** ~3.7 GB
- **Description:** Contains geographic and infrastructure data including roads, amenities, and other features.

---

## Objective
The goal of this project is to:
- Process large-scale geospatial data using Hadoop MapReduce
- Perform frequency analysis on infrastructure features
- Identify dominant patterns in highway and amenity distributions

---

## Data Preprocessing
The raw `.osm.pbf` file is not directly suitable for Hadoop Streaming, so preprocessing was performed:

1. Filtered relevant tags (`amenity`, `highway`) using `osmium`
2. Exported filtered data to JSON format
3. Converted JSON into line-based text format for Hadoop

Example processed record:
