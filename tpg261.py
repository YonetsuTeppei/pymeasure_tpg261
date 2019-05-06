#! /usr/bin/env python3

import sys, time, pymeasure, rospy, std_msgs, serial


class device(object):

    def __init__(self):
        self.tpg261 = serial.Serial("/dev/ttyUSB1",timeout=1)


    def pressure(self):
         self.tpg261.write(b"PR1 \r\n")
         time.sleep(0.3)
         self.tpg261.write(b"\x05")
         time.sleep(0.3)
         self.raw_p = self.tpg261.readline()
         pressure = str(self.raw_p[2:13])
         pressure = pressure.strip("b'")
         return pressure

    def pressure_error(self):
         status_p = self.raw_p[0:1]
         return status_p

    def check(self):
        if self.raw_p == b'\x06\r\n' :
            self.a = 0
        else:
            self.a = 1
        return self.a

    def gauge_query(self):
        self.tpg261.write(b"SEN , 0, 0 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        self.raw_g = self.tpg261.readline()
        status1_g = self.raw_g[0:1]
        status2_g = self.raw_g[2:3]

    def gauge1_check(self):
        status1_g = self.raw_g[0:1]
        return status1_g

    def gauge2_check(self):
        status2_g = self.raw_g[2:3]
        return status2_g

    def gauge_change_1(self):
        self.tpg261.write(b"SEN , 2 , 1 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status1_g = str(get[0:1])
        status2_g = str(get[2:3])

    def gauge_change_2(self):
        self.tpg261.write(b"SEN , 1 , 2 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status1_g = str(get[0:1])
        status2_g = str(get[2:3])

    def gauge_change_Off1_2(self):
        self.tpg261.write(b"SEN , 1 , 1 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status1_g = str(get[0:1])
        status2_g = str(get[2:3])



    def pres_unit_bar(self):
        self.tpg261.write(b"UNI,0 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        self.raw_bar = self.tpg261.readline()
        unit = self.raw_bar[0:1]
        return unit

    def pres_unit_torr(self):
        self.tpg261.write(b"UNI,1 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        self.raw_torr = self.tpg261.readline()
        unit = self.raw_torr[0:1]
        return unit

    def pres_unit_pa(self):
        self.tpg261.write(b"UNI,2 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        self.raw_pa = self.tpg261.readline()
        unit = self.raw_pa[0:1]
        return unit

'''
 def pressure_both(self):
         self.tpg261.write(b"PRX \r\n")
         time.sleep(0.3)
         self.tpg261.write(b"\x05")
         time.sleep(0.3)
         rawb = self.tpg261.readline()
         status1 = rawb[0:1]
         status2 = rawb[14:15]
         pressure1 = str(raw2[2:13])
         pressure2 = str(raw2[16:27])


    def gauge_change_1(self):
        self.tpg261.write(b"SEN , 2 , 1 \r\n")
        time.sleep(0.3)
        self.tpg261.write(b"\x05")
        time.sleep(0.3)
        get = self.tpg261.readline()
        status1 = str(get[0:1])
        status2 = str(get[2:3])

    def gauge_change_2(self):
        self.tpg261.write(b"SEN , 1 , 2 \r\n")
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
'''
