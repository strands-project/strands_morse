#! /usr/bin/env python3

import sys
from PySide import QtGui, QtCore

import roslib
import rospy
import pymorse
from std_msgs.msg import Bool

class ControlGUI(QtGui.QWidget):
    
    def __init__(self, morse):
        super(ControlGUI, self).__init__()
        self._floors=["B","G","1","2"]
        
        self._callers={}
        for i in self._floors:
            self._callers[i]=rospy.Publisher("/lift_sim/call{}".format(i), Bool)
            
        self._commanders={}
        for i in self._floors:
            self._commanders[i]=rospy.Publisher("/lift_sim/command{}".format(i), Bool)
            
        self.initUI()

        self._morse = morse

    def _cmd_floor(self,flr):
        self._commanders[flr].publish(True)

    def _call_floor(self,flr):
        self._callers[flr].publish(True)        
        
        
    def initUI(self):
        floor_buttons=[QtGui.QPushButton("Floor {}".format(f)) for f in self._floors]
 
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        for i in floor_buttons:
            i.setCheckable(True)
            i.clicked[bool].connect(self.floor_button_click)
            hbox.addWidget(i)
        hbox.addStretch(1)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(QtGui.QLabel("Show / Hide floor:"))
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        vbox.addWidget(QtGui.QLabel("Call the lift:"))
        call_buttons=[QtGui.QPushButton("Call {}".format(f)) for f in self._floors]
        hbox= QtGui.QHBoxLayout()
        hbox.addStretch(1)
        for i in call_buttons:
            i.clicked.connect(self.call_button_click)
            hbox.addWidget(i)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        
        vbox.addWidget(QtGui.QLabel("Command the lift:"))
        command_buttons=[QtGui.QPushButton("{}".format(f)) for f in self._floors]
        hbox= QtGui.QHBoxLayout()
        hbox.addStretch(1)
        for i in command_buttons:
            i.clicked.connect(self.command_button_click)
            hbox.addWidget(i)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('BHAM ControlGUI')    
        self.show()
        
    def floor_button_click(self,show):
         sender = self.sender()
         f=sender.text()[-1]
         print("Show or hide floor:",show,f)
         floor_name="Floor"
         if f=="B":
             floor_name+="LG"
         elif f=="G":
             floor_name+="UG"
         else:
             floor_name+=f
         self._morse.rpc('simulation', 'set_object_visibility',
                         floor_name, show, True)
         

    def call_button_click(self):
         sender = self.sender()
         f=sender.text()[-1]
         print("Call to ",f)
         self._call_floor(f)
    
    def command_button_click(self):
         sender = self.sender()
         f=sender.text()[-1]
         print("Command to ",f)
         self._cmd_floor(f)


if __name__ == '__main__':
    rospy.init_node("BHAM_CONTROL_GUI")
    app = QtGui.QApplication(sys.argv)
#    morse=None
    with pymorse.Morse() as morse:
        ex = ControlGUI(morse)
        sys.exit(app.exec_())

