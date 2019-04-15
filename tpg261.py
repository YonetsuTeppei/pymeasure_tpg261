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
         raw1 = self.tpg261.readline()
         status = raw1[0:1]
         pressure = str(raw1[2:13])

    def pressure_both(self,raw1):
         self.tpg261.write(b"PRX \r\n")
         time.sleep(0.3)
         self.tpg261.write(b"\x05")
         time.sleep(0.3)
         raw1 = self.tpg261.readline()
         status1 = raw2[0:1]
         status2 = raw2[14:15]
         pressure1 = str(raw2[2:13])
         pressure2 = str(raw2[16:27])

    def gauge_check(self,gauge1 = 0,gauge2 = 0):
        self.tpg261.write(b"SEN , gague1 , gague2 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status1 = str(get[0:1])
        status2 = str(get[2:3])

    def gauge_change(self,gague1,gague2):
        self.tpg261.write(b"SEN , gague1 , gague2 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status1 = str(get[0:1])
        status2 = str(get[2:3])

    def change_gague1(self):
        self.tpg261.write(b"SCT , 0\r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status = str(get[0:1])

    def change_gague2(self):
        self.tpg261.write(b"SCT , 1\r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status = str(get[0:1])

    def query_error(self):
        self.tpg261.write(b"ERR \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status = str(get[0:4])
