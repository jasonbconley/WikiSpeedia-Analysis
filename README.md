# WikiSpeedia-Analysis
Using SNAP wikipedia data to perform some graph analysis

## Pre-processing
Once the data is downloaded, run Game/Create_Graph.py to generate the .graphml file for further processing.

Then, run Game/Community_Gen.py to create the two dataframes, the first of which stores the node names and the community they belong to, and the second stores the community numbers and their diameters. These are *community_list.csv* and *community_diameters.csv* respectively.
