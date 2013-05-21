#!/bin/bash

# To allow rosrun to launch the morse simulator..
environment_name="bham_cs_sim"

path=`rospack find $environment_name`
strands_sim=`rospack find strands_sim`
#cd $pth
#cd ..
added=`$strands_sim/morse_config.py $environment_name $path`
echo "Running morse on $path"
morse run $environment_name
