# Python CLI completion and history
export PYTHONSTARTUP=/opt/morse-blender-2.65-py-3.3/.pyrc
# Blender
export MORSE_BLENDER=/opt/morse-blender-2.65-py-3.3/opt/blender/blender
alias blender=/opt/morse-blender-2.65-py-3.3/opt/blender/blender
# Python
export PATH=$PATH:/opt/morse-blender-2.65-py-3.3/bin
export PYTHONPATH=$PYTHONPATH:/opt/morse-blender-2.65-py-3.3/lib/python3.3/dist-packages
export PKG_CONFIG_PATH=/opt/morse-blender-2.65-py-3.3/lib/pkgconfig:$PKG_CONFIG_PATH
# Colorize MORSE :-)
alias morse="env LD_LIBRARY_PATH=/opt/morse-blender-2.65-py-3.3/lib morse -c"
