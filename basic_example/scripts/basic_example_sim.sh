#!/bin/bash
environment_name="basic_example"
strands_morse=`rospack find strands_morse`
example=`rospack find basic_example`
path="$example"
common="$strands_morse/strands_sim"

PYTHONPATH="$path/src:$common/src:$PYTHONPATH"
MORSE_RESOURCE_PATH="$strands_morse:$common/data:$common/robots:$path:$MORSE_RESOURCE_PATH"
export MORSE_RESOURCE_PATH PYTHONPATH
added=`$strands_morse/morse_config.py $environment_name $path`
echo "Running morse on $path with PYTHONPATH=$PYTHONPATH and MORSE_RESOURCE_PATH=$MORSE_RESOURCE_PATH"
PATH=/opt/strands-morse-simulator/bin:$PATH

morse run thermo `rospack find strands_morse`/basic_example/example_sim.py
