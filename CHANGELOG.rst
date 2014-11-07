^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package strands_morse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.7 (2014-11-07)
------------------
* Merge pull request `#83 <https://github.com/strands-project/strands_morse/issues/83>`_ from strands-project/install_pose_simulator
  added install target for human_pose_simulator
* added install target for human_pose_simulator
* Merge pull request `#82 <https://github.com/strands-project/strands_morse/issues/82>`_ from hawesie/hydro-devel
  Added topological map file.
* Added topological map file.
* Merge pull request `#81 <https://github.com/strands-project/strands_morse/issues/81>`_ from nilsbore/hydro-devel
  Added openni_wrapper as a run dependency
* Added openni_wrapper as a run dependency since generate_camera_topics.launch uses it
* Contributors: Marc Hanheide, Nick Hawes, Nils Bore

0.0.6 (2014-11-04)
------------------
* Merge pull request `#80 <https://github.com/strands-project/strands_morse/issues/80>`_ from cdondrup/human
  Using the standard morse human model
* Updated README with install and set-up instructions using the morse-blender-bundle
* Switched to standard human model
* Merge pull request `#78 <https://github.com/strands-project/strands_morse/issues/78>`_ from cdondrup/hydro-devel
  Fixing the "stuck in the ground" bug.
* Fixing the stuck in the ground bug.
  fixing `#77 <https://github.com/strands-project/strands_morse/issues/77>`_
  I the UoL environments the robot started at z = 0.0 which sometimes let it start in the ground and prevented movement.
* Contributors: Christian Dondrup, Marc Hanheide

0.0.5 (2014-10-30)
------------------
* There is no definition for the morse-blender-bundle for fedora yet.
  Bloom complains:
  Could not resolve rosdep key 'morse-blender-bundle' for distro 'heisenbug':
  No definition of [morse-blender-bundle] for OS [fedora]
  rosdep key : morse-blender-bundle
  OS name    : fedora
  OS version : heisenbug
  Data: ubuntu:
  precise:
  - morse-blender-2.65-py-3.3
  removing run_dependency for now.
* Contributors: Christian Dondrup

0.0.4 (2014-10-30)
------------------
* Merge pull request #76 from cdondrup/install
  Adding install targets and dependencies
* Added morse-blender-bundle to run dependencies.
* Added topic_republisher as run_dependency
* Added install targets
* Merge pull request #72 from nilsbore/hydro-devel
  [kth] Created a KTH simulator environment
* Added a map generated with gmapping
* Fixed cameras in a good position
* First version of KTH simulator environment
* Contributors: Christian Dondrup, Lars Kunze, Nils Bore

0.0.3 (2014-08-21)
------------------
* fixed rosdeps
* Contributors: Marc Hanheide

0.0.2 (2014-08-21)
------------------
* Added simple setup based on tutorial indoors-1 environment where I know the robot drives ok.
* Merge pull request `#71 <https://github.com/strands-project/strands_morse/issues/71>`_ from nilsbore/patch-1
  Just added some descriptions to the readme. No harm done.
* Update README.md
  Added instructions for getting OpenNI topics.
* Merge pull request `#70 <https://github.com/strands-project/strands_morse/issues/70>`_ from kunzel/hydro-devel
  Adapted elevator and sliding door code to the most recent version of morse
* Merge pull request `#68 <https://github.com/strands-project/strands_morse/issues/68>`_ from nilsbore/hydro-devel
  Add option to ScitosA5 to generate openni stack topics
  Nice work @nilsbore! Thanks a lot!
* adapted elevator  and sliding door code to latest morse verion
* updated starting pose of bob
* added lamp to morse environment
* Changed the topics of the simulated rgb camera to the same as the original topic
* Added option to enable/disable openni topics
* Made some changes to the robot setup file, changed focal lengths of cameras to be more like the ones on our sensors and made the video camera update slower because my computer is not near handling that framerate
* Managed to get the openni wrapper stack working with MORSE after much fiddling around, this is only the code that doesn't touch the simulator setup
* Changed the sync policy to give nicer clouds while moving
* Added a node for converting pointcloud + color image to a colored point cloud and a depth image aligned to the rgb image
* Merge pull request `#67 <https://github.com/strands-project/strands_morse/issues/67>`_ from kunzel/hydro-devel
  Removed discontinuity in the floor (Thanks to Greg!)
* Removed discontinuity in the floor (Thanks to Greg!)
* Merge pull request `#64 <https://github.com/strands-project/strands_morse/issues/64>`_ from nilsbore/hydro-devel
  Changed the PTU step so it works with the flir_pantilt_d46 action server
* Merge pull request `#65 <https://github.com/strands-project/strands_morse/issues/65>`_ from kunzel/hydro-devel
  builder file for scene generation; added json file of 2000 generated scenes
* added 3d maps for cs_lg_bham
* Merge branch 'hydro-devel' of https://github.com/strands-project/strands_morse into hydro-devel
* added json file of 2000 generated scenes
* added builder script for scene generation
* builder file for scene generation
* Changed the PTU step so it works with the flir_pantilt_d46 action server
* Merge pull request `#63 <https://github.com/strands-project/strands_morse/issues/63>`_ from kunzel/hydro-devel
  Hydro devel: added object search scenario
* Merge branch 'hydro-devel' of https://github.com/strands-project/strands_morse into hydro-devel
* object search scenario
* Merge pull request `#62 <https://github.com/strands-project/strands_morse/issues/62>`_ from marc-hanheide/hydro-devel
  Human Pose Semantic Camera "Hack"
* renamed to better match semantics
* added posetransformer
* Merge branch 'hydro-devel' of github.com:strands-project/strands_morse
* added semantic human camera and pose publisher to simulate human detection
* Merge pull request `#60 <https://github.com/strands-project/strands_morse/issues/60>`_ from BFALacerda/hydro-devel
  getting fake scitos service to work
* getting fake scitos service to work
* Merge pull request `#59 <https://github.com/strands-project/strands_morse/issues/59>`_ from cburbridge/master
  Lift in Morse
* Adding the LG tables and charging station to the builder script for the whole cs building
* A simple control GUI for the lift and BHAM simulation
* Fix lift controller for python 3.3 install
* Merge pull request `#58 <https://github.com/strands-project/strands_morse/issues/58>`_ from kunzel/master
  moved docking station in BHAM env; updated robot starting pose; updated BHAM env map with origin on docking station
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* updated map with origin on docking station; updated rviz visualization
* added the parameter for discharging rate; can be overwritten in a builder script
* removed a table in the middle of the area (no 7); and shifted the wall by 10 centimeters to provide more space for the docking station
* moved docking station to a place outside the robot lab
* Merge pull request `#57 <https://github.com/strands-project/strands_morse/issues/57>`_ from Jailander/master
  Changes UOL MHT simulations
* + Added charging station and label to uol mht blender
  + Included new maps and waypoint files for mht simulation of autonomous patrolling
* Merge pull request `#56 <https://github.com/strands-project/strands_morse/issues/56>`_ from kunzel/master
  Added a scene converter for the new file format
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* added scene converter for new file layout
* Merge pull request `#54 <https://github.com/strands-project/strands_morse/issues/54>`_ from kunzel/master
  Added a scene generator for desktops. I'll merge it in as it should not influence the simulation in general.
* added table-top objects
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* generate a single scene on a table, wait for enter, and remove it
* adaptated help msg to new command
* merged from master and resolved conflicts
* tweaked parameters of semantic camera
* aaai paper version
* initial version
* added ptu republisher to launch file
* Merge pull request `#51 <https://github.com/strands-project/strands_morse/issues/51>`_ from kunzel/master
  Added tables and chairs to bham env; chenged image resolution to 640x480
* added tables and chairs by default
* changed camera resolution to 640x480
* cups in tum kitchen
* object placement with labelling
* QSR-based scene generation
* placement based on config file
* QSR labelling for scenes
* generation of scenes with QSR labels
* write scene descriptionsto file
* generate destop scenes and log information for learning
* initial version of object placement utility
* Merge pull request `#50 <https://github.com/strands-project/strands_morse/issues/50>`_ from mudrole1/master
  Objects for lg and functions to add them
* objects for lg modified, added function to import them
* Added objects for lower-ground flour of Birmingham building.
* added missing runtime dependencies; changed build time dependencies also to runtime
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* Added a simple node (scitos_node) that publishes topics and provides services according to the real robot.
  This node runs in parallel to morse and thereby complements it by providing missing topics such as /motor_state.
  As this node should be launched whenever the scitos robot is used in MORSE, I added a launch file called scitos.launch, which now bundles the scitos robot state publisher and the scitos_node. I included this new launch file in all existing simulations (bham,tum,uol). That is, future changes wrt to the robot should be realized within scitos.launch instead of the individual environment launch files.
* Merge pull request `#45 <https://github.com/strands-project/strands_morse/issues/45>`_ from kunzel/master
  Added battery state sensor to robot (requires an up-to-date strands-project/morse!)
* set cam_near property for depth camarea
* added object property to docking station
* adjusted camera size and frequency
* disabled physics for dockingstation
* included strands logo in blend file
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* added NEW battery state sensor (requires strands-project/morse update!); adjusted topic names
* Use scitos robot with all sensors as default; spawn it in fornt of the docking station
* added docking station and label to environment
* added light source to lg environment
* changed origin of docking station model
* added robot station label for docking station
* cropped map for bham cs lg
* fixed package name in load_manifest instruction
* Merge pull request `#40 <https://github.com/strands-project/strands_morse/issues/40>`_ from kunzel/master
  added strands logo to scitos robot; changed floor color of cs_lg
* changed floor color
* added strands logo to scitos robot
* Merge pull request `#38 <https://github.com/strands-project/strands_morse/issues/38>`_ from kunzel/master
  fixed and tuned physics parameters of the robot model.
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* tunning physics parameters
* fixed physics parameters
* Merge pull request `#36 <https://github.com/strands-project/strands_morse/issues/36>`_ from kunzel/master
  set topic for ptu jointstate
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* set topic for ptu jointstate
* Merge pull request `#35 <https://github.com/strands-project/strands_morse/issues/35>`_ from kunzel/master
  fixed video camera; fixed frame ids
* fixed video camera; fixed frame ids
* Merge pull request `#33 <https://github.com/strands-project/strands_morse/issues/33>`_ from kunzel/master
  Using the new robot model made by Lenka
* using the fancy looking robot model made by Lenka
* updated physics of robot model
* Merge pull request `#31 <https://github.com/strands-project/strands_morse/issues/31>`_ from kunzel/master
  fixed problem with point cloud offset
* fixed problem with point cloud offset (workaround: https://github.com/morse-simulator/morse/issues/371)
* Merge pull request `#28 <https://github.com/strands-project/strands_morse/issues/28>`_ from kunzel/master
  usage of depth camera without TF frame; defined topic and frame names as constants in the robot model
* Merge pull request `#30 <https://github.com/strands-project/strands_morse/issues/30>`_ from mudrole1/master
  Added improve blender model for robot
* Added improve blender model for robot
* Merge pull request `#29 <https://github.com/strands-project/strands_morse/issues/29>`_ from cdondrup/master
  Added a simulation environment for a first user study
* Added a simulation environment for a first user study. Representing a simple restaurant setup with thrre tables and a kitchen (another table) in one of our gymnasiums.
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* added hint that we use strands-project/morse
* usage of depth camera without TF frame; defined topic and frame names as constants
* Merge pull request `#26 <https://github.com/strands-project/strands_morse/issues/26>`_ from BFALacerda/master
  moved the state publisher from 2d nav launch to morse launch
* Merge pull request `#25 <https://github.com/strands-project/strands_morse/issues/25>`_ from markrosoft/master
  Normalised faces: Looks much better to me ;-)
* moved the state publisher from 2d nav launch to morse launch
* Plugging the many holes in the walls.
* Added the robot station Image above the charger
* Merge pull request `#23 <https://github.com/strands-project/strands_morse/issues/23>`_ from marc-hanheide/human
  This adds another environment to the uol and tum class of environments including a human for HRI research
* Merge branch 'master' of github.com:strands-project/strands_morse into human
* Merge pull request `#24 <https://github.com/strands-project/strands_morse/issues/24>`_ from markrosoft/master
  Loop Closure Fix (initially the wrong old map was committed)
* Added Loop Closure
* fixed import
* renamed properly
* Merge branch 'master' of github.com:strands-project/strands_morse into human
* Merge pull request `#22 <https://github.com/strands-project/strands_morse/issues/22>`_ from markrosoft/master
  University of Lincoln MHT Third Floor Morse Model. Tested as fully working
* Merge branch 'master' of https://github.com/markrosoft/strands_morse into human
* initial version of the UOL MHT 3rd floor
* added our own new human
* added pose publisher for human
* added human
* Merge pull request `#18 <https://github.com/strands-project/strands_morse/issues/18>`_ from strands-project/add-sensors-to-robot-model
  Added camera sensors to robot model
  looks perfect. Great job! worked for me.
* added option for running the robot without depth cameras
* updated roslaunch command for tum kitchen
* added camera sensors (video, depth, semantic) to robot model
* Merge pull request `#17 <https://github.com/strands-project/strands_morse/issues/17>`_ from strands-project/morse-config-bug
  use /usr/bin/env to determine python3.3 location
* use /usr/bin/env to determine python3.3 location
* Merge pull request `#14 <https://github.com/strands-project/strands_morse/issues/14>`_ from strands-project/new-package-structure
  MAJOR refactoring of repository structure; cleaning up files;  new launch files ...
* added command for rviz
* updated readme
* fixed commands
* refactored repository structure to be more consistent; new launch files for simulation, navigation, and visualization (RVIZ)
* changed indentation to fix `#10 <https://github.com/strands-project/strands_morse/issues/10>`_
* Merge pull request `#11 <https://github.com/strands-project/strands_morse/issues/11>`_ from BFALacerda/master
  added map and launch files for 2dnav in bham cs building lower ground floor
* added launch file for 2dnav in bhac cs building, lower ground floor
* added map of the bham cs building lower ground floor
* Added command for 2D navigation
* Merge pull request `#9 <https://github.com/strands-project/strands_morse/issues/9>`_ from strands-project/navigation-2D
  added 2D navigation launch files/removed deprecated package
* added 2D navigation launch files for two MORSE environments: tum_kitchen/bham_cs_level_1; removed deprecated package: strands_morse_2dnav
* Merge pull request `#8 <https://github.com/strands-project/strands_morse/issues/8>`_ from marc-hanheide/master
  Refactoring and catkinising of simulation to support multiple environments more transparently
  WARNING: There are currently no launch files for the 2D navigation in simulation! That is, if you don't need the new repository structure by now, please wait until the launch files are in place.
* added missing resource path
* moved 2dnav out of sim repository
* added removal of file
* moved simulation urdf file into strands_sim/robots
* refactoring of repository:
  * added stuff to catkinise this repository (now strands_morse is the package, everythnig else is contained in it)
  * the policy is that different environments can go into different subdirs (simulator.sh takes care of setting everything up)
  * changed simulator.sh to set PYTHONPATH etc and removed this from the specific builder scripts
  * move all non-simulation code (strands_executive) into subfolder TO-BE-MOVED for now
  * created new environment tum_kitchen
  * put everything that is common into strands_sim (robots, scripts, etc), make sure other environments can find what is in strands_sim
* cropped tum kitchen map
* Merge pull request `#5 <https://github.com/strands-project/strands_morse/issues/5>`_ from strands-project/ptu
  mounted depthcam, semantic cam, and video cam on ptu
* mounted depthcam, semantic cam, and video cam on ptu
* Built the blender file for the docking station.
* Merge pull request `#4 <https://github.com/strands-project/strands_morse/issues/4>`_ from strands-project/video-cam
  added videocam to scitos robot
* added videocam to scitos robot
* ignore all .rosinstall directories in git
* Merge pull request `#3 <https://github.com/strands-project/strands_morse/issues/3>`_ from strands-project/marc_devel
  changed to non-holonomic robot (both in robot model and movebase)
* changed to non-holonomic robot (both in robot model and movebase)
* Merge branch 'master' of https://github.com/strands-project/strands_morse
* some maps
* changed position of the battery
* floor 1 map
* splitting robot state publisher from navigation stack
* Merge branch 'devel-chris'
* fix elevator bug / laser issues
* added failure transition to the CHARGE_BATTERY state in smach_nav.py and added possibility to start the MORSE simulation only on the lower ground floor of tge UB CS building
* Merge branch 'devel-chris'
  Conflicts:
  strands_morse_2dnav/nav.launch
* single floor models
* fix UG floor
* model updates
* Added script for generating random positions of objects and placing them on
  planar objects (eg tables)
* Merge remote-tracking branch 'origin/master'
* added scham implementation of patrolling behaviour for fixed points and simulated battery discharge and charge
* Merge branch 'lars-devel'
* added a battery sensor to the robot
* added comment for depth camera
* added pose sensor
* renamed camera
* Some objects in common room.
* structured the floors to aid visibility changes
* generate flexible plan for navigation
* added semantic camera
* added script for simple navigation in tum kitchen
* adjusted navigation parameters
* made robot holonomic, edited footprint, replaced /odom with /map
* added kinect sensor on PTU
* Merge branch 'master', remote-tracking branch 'origin'
* Adding CS building launch instruction
* combining CS building and ScitosA5
* fix path error.
* Adding morse site management to ros launch scripts.
* ~ files ignored
* Merge branch 'master' into devel-chris
* adding door to common room
* added alternative start method for simulation
* added possibility to run morse via rosrun
* commented out import from Test
* Merge remote-tracking branch 'origin/master' into first-ros-morse-simulation
* Moved sensors and actuators into robot specification
* ignore blender revisions
* removed obsolete robot model
* scitos robot v2
* second version of scitos A5
* removed blender bak
* ignore *pyc files
* updated robot model
* Updating readme.
* Updating readme.
* bham_cs_sim: simulation of the CS builing at UB
* added gitignore
* simplified urdf
* updated README
* initial version
* getting started instructions
* Initial commit
* Contributors: Akshaya Thippur, BFALacerda, Bruno Lacerda, Chris Burbridge, Christian Dondrup, Jaime Pulido Fentanes, Lars Kunze, Lenka, Lenka Mudrova, Marc Hanheide, Mark Collins, Nick Hawes, Nils Bore, cburbridge, cdondrup
