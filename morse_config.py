#! /usr/bin/env python3
"""
Script to check that simulation is on the morse sites list.
"""

import os
import configparser
import sys

def get_config_file():
    config_path = os.path.expanduser("~/.morse")
    if not os.path.exists(config_path):
        print( "WARNING: Morse had no config file, so one is being created in ", config_path )
        os.mkdir(config_path)

    return os.path.join(config_path, "config")


def set_site_path(name, path):
    config = configparser.SafeConfigParser()
    config.read(get_config_file())
    
    if not config.has_section("sites"):
        config.add_section("sites")
        
    config.set('sites', name, path)
        
    with open(get_config_file(), 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Error: rong number of args. Usage: morse_config.py sim_name sim_path")
        exit(1)
    else:
        set_site_path(sys.argv[1], sys.argv[2])
        exit(0)
