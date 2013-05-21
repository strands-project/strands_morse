#!/bin/bash

# To allow rosrun to launch the morse simulator..
environment_name="strands_sim"
simulation=$1
if [ "$simulation" == ""]; then
  simulation="default.py"
fi 

path=`rospack find $environment_name`
strands_sim=`rospack find strands_sim`
#cd $pth
#cd ..
added=`$strands_sim/morse_config.py $environment_name $path`
echo "Running morse on $path"
morse run $environment_name $simulation
