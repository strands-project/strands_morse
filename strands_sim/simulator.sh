#!/bin/bash

# To allow rosrun to launch the morse simulator..

pth=`rospack find strands_sim`
cd $pth
cd ..
echo "Running morse on $pth"
morse run strands_sim
