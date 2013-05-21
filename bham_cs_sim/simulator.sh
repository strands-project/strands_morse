#!/bin/bash

# To allow rosrun to launch the morse simulator..

pth=`rospack find bham_cs_sim`
cd $pth
cd ..
echo "Running morse on $pth"
morse run bham_cs_sim
