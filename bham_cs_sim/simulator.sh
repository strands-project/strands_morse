#!/bin/bash

# To allow rosrun to launch the morse simulator..
environment_name="bham_cs_sim"

path=`rospack find strands_sim`
#cd $pth
#cd ..
added=`$path/morse_config.py $environment_name $path`
echo "Running morse on $path"
morse run $environment_name
