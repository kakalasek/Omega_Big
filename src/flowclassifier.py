#!/usr/bin/env python3

import pytrap
import sys
import pandas as pd
import numpy as np
import pickle
import json

trap = pytrap.TrapCtx()
trap.init(sys.argv, 1, 1)

inputspec = "ipaddr DST_IP,ipaddr SRC_IP,int8* PPI_PKT_DIRECTIONS,uint16* PPI_PKT_LENGTHS"
trap.setRequiredFmt(0, pytrap.FMT_UNIREC, inputspec)
rec = pytrap.UnirecTemplate(inputspec)

outputspec = "ipaddr DST_IP,ipaddr SRC_IP,string CLASS"
output = pytrap.UnirecTemplate(outputspec)
trap.setDataFmt(0, pytrap.FMT_UNIREC, outputspec)

output.createMessage()

class_mapping = {}

with open("classes/classes_mapping.json", "r") as file:
    class_mapping =  json.load(file)

loaded_model = pickle.load(open('models/network_classificator_cesnet_ghbt.dat', 'rb'))

def do_classification(rec):
    # Write algorhitm here

    if len(rec.PPI_PKT_LENGTHS) > 0:

        t = np.array(rec.PPI_PKT_DIRECTIONS) * np.array(rec.PPI_PKT_LENGTHS)
        t = np.resize(t, 30)
        t = t.reshape(1, -1)

        d = pd.DataFrame(t, columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'])

        prediction = str(loaded_model.predict(d).tolist()[0])

        traffic_class = class_mapping[prediction]

        output.SRC_IP = rec.SRC_IP
        output.DST_IP = rec.DST_IP
        output.CLASS = traffic_class

        trap.send(output.getData(), 0)

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

    do_classification(rec)


trap.finalize()