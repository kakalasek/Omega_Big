#!/usr/bin/env python3

import pytrap
import sys
import json
import os
from ipaddress import ip_address

def aggregate(rec, agg_dict: dict, write: int, agg_file: str):

    ipaddr = str(rec.SRC_IP) if ip_address(str(rec.SRC_IP)).is_private else str(rec.DST_IP)
    service = str(rec.CLASS)

    if ipaddr in agg_dict.keys():
        if service in agg_dict[ipaddr].keys():
            agg_dict[ipaddr][service] += 1
        else:
            agg_dict[ipaddr][service] = 1
    else:
        agg_dict[ipaddr] = {}
        agg_dict[ipaddr][service] = 1

    if write:
        with open(agg_file, "w") as file:
            json.dump(agg_dict, file)
        

outputfile = "./agg.json"

trap = pytrap.TrapCtx()
trap.init(sys.argv, 1, 0)

inputspec = "ipaddr SRC_IP,ipaddr DST_IP,string CLASS"
trap.setRequiredFmt(0, pytrap.FMT_UNIREC, inputspec)
rec = pytrap.UnirecTemplate(inputspec)

json_agg = {}
write = 20

# Main loop

print("Aggregation has started")

while True:
    try:
        data = trap.recv()
    except pytrap.FormatChanged as e:
        fmttype, inputspec = trap.getDataFmt(0)
        rec = pytrap.UnirecTemplate(inputspec)
        data = e.data
    if len(data) <= 1:
        break

    rec.setData(data)

    write -= 1

    aggregate(rec, json_agg, write <= 0, outputfile)

    if write <= 0:
        write = 20

    print(write)

trap.finalize()

    