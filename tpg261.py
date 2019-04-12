#! /usr/bin/env python3

import sys, time, pymeasure, rospy, std_msgs


class device(object):

    def pressure_device(self):
         tpg261_driver.tpg261.write(b"PR1 \r\n")
         time.sleep(0.3)
         tpg261_driver.tpg261.write(b"\x05")
         time.sleep(0.3)
         raw = tpg261_driver.tpg261.readline()
         status = raw[0:1]
         pressure = str(raw[2:13])

    def pressure_both(self):
         tpg261_driver.tpg261.write(b"PRX \r\n")
         time.sleep(0.3)
         tpg261_driver.tpg261.write(b"\x05")
         time.sleep(0.3)
         raw = tpg261_driver.tpg261.readline()
         status1 = raw[0:1]
         status2 = raw[14:15]
         pressure12 = str(raw[2:13],raw[16:27])

    def gauge_check(self,gauge1 = 0,gauge2 = 0):
        tpg261_driver.tpg261.write(b"SEN , gague1 , gague2 \r\n")
        time.sleep(0.3)
        tpg261_driver.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = tpg261_driver.tpg261.readline()
        status1 = str(get[0:1])
        status2 = str(get[2:3])

    def gauge_change(self,gague1,gague2):
        tpg261_driver.tpg261.write(b"SEN , gague1 , gague2 \r\n")
        time.sleep(0.3)
        tpg261_driver.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = tpg261_driver.tpg261.readline()
        status1 = str(get[0:1])
        status2 = str(get[2:3])

    def change_gague1(self):
        tpg261_driver.tpg261.write(b"SCT , 0\r\n")
        time.sleep(0.3)
        tpg261_driver.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = tpg261_driver.tpg261.readline()
        status = str(get[0:1])

    def change_gague2(self):
        tpg261_driver.tpg261.write(b"SCT , 1\r\n")
        time.sleep(0.3)
        tpg261_driver.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = tpg261_driver.tpg261.readline()
        status = str(get[0:1])

    def query_error(self):
        tpg261_driver.tpg261.write(b"ERR \r\n")
        time.sleep(0.3)
        tpg261_driver.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = tpg261_driver.tpg261.readline()
        status = str(get[0:4])
