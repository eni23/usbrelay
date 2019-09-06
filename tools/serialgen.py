#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3
import datetime
import uuid

DEVICE="usb-button"
FLAGS="p........"

H_TPL = """
#define USB_CFG_SERIAL_NUMBER       {0}
#define USB_CFG_SERIAL_NUMBER_LEN   {1}
"""


def get_db(path):
    c = sqlite3.connect(path)
    c.execute('''
        CREATE TABLE IF NOT EXISTS serial (
            id INTEGER PRIMARY KEY,
            serial TEXT,
            date TEXT,
            device TEXT,
            flags TEXT
        )''')
    c.commit()
    return c



def new_device(conn):
    now = str(datetime.datetime.now())
    serial = str(uuid.uuid4().hex)[:-16]
    sqldata = (None, serial, now, DEVICE, FLAGS)
    conn.execute('INSERT INTO serial VALUES (?,?,?,?,?)', sqldata)
    conn.commit()
    res = ""
    for i in serial:
        res += "'{0}', ".format(i)
    print(H_TPL.format(
        res[:-2],
        len(serial)
    ))



def main():
    spath = os.path.dirname(os.path.dirname(
        os.path.realpath( __file__ )
    ))
    dbpath = f"{spath}/serial/serial.db"
    conn = get_db(dbpath)
    new_device(conn)



if __name__ == '__main__':
    main()
