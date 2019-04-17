#! /usr/bin/env python3

import sys, time, pymeasure, rospy, std_msgs, serial


class device(object):

    def __init__(self):
        self.tpg261 = serial.Serial("/dev/ttyUSB1",timeout=1)


    def pressure_device(self):
         self.tpg261.write(b"PR1 \r\n")
         time.sleep(0.3)
         self.tpg261.write(b"\x05")
         time.sleep(0.3)
         raw = self.tpg261.readline()
         status = raw[0:1]
         pressure = str(raw[2:13])

    def check(self):
        if raw == b'\x06\r\n':
            self.a = 0
        else:
            self.a = 1
        return self.a
