#!/bin/bash

# To allow rosrun to launch the morse simulator..
default_environment_name="tum_kitchen"
default_simulation="default.py"




environment_name="$1"
if [ "$environment_name" == "" ]; then
	environment_name="$default_environment_name"
fi


simulation="$2"
if [ "$simulation" == "" ]; then
  simulation="$default_simulation"
fi 

strands_morse=`rospack find strands_morse`
path="$strands_morse/$environment_name"
common="$strands_morse/strands_sim"


PYTHONPATH="$path/src:$common/src:$PYTHONPATH"
MORSE_RESOURCE_PATH="$strands_morse:$common/data:$common/robots:$path/data:$MORSE_RESOURCE_PATH"
export MORSE_RESOURCE_PATH PYTHONPATH
#cd $pth
#cd ..
added=`$strands_morse/morse_config.py $environment_name $path`
echo "Running morse on $path with PYTHONPATH=$PYTHONPATH and MORSE_RESOURCE_PATH=$MORSE_RESOURCE_PATH"
PATH=/opt/strands-morse-simulator/bin:$PATH
morse run $environment_name $simulation
