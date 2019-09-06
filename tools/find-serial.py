#!/usr/bin/env python

import sys
import time
import glob
import serial

SERIAL_TIMEOUT      = .5
SERIAL_PORT_GLOB    = '/dev/ttyACM[0-9]'


def find_serial(regexp):
    port_blacklist = []
    while True:
        ports = glob.glob(regexp)
        for port in ports:
            if port in port_blacklist:
                continue
            try:
                ser = serial.Serial(
                    port = port,
                    timeout = SERIAL_TIMEOUT
                )
            except serial.serialutil.SerialException:
                port_blacklist.append(port)
                continue
            ser.close()
            return port

        time.sleep(SERIAL_FIND_PAUSE)



def main():
    try:
        regexp = sys.argv[1]
    except IndexError:
        regexp = SERIAL_PORT_GLOB

    print(find_serial(regexp))

if __name__ == "__main__":
    main()
