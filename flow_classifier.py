#!/usr/bin/env python3

import pytrap
import sys
import pandas as pd
import numpy as np

trap = pytrap.TrapCtx()
trap.init(sys.argv, 1, 0)

inputspec = "string TLS_SNI,int8* PPI_PKT_DIRECTIONS,uint16* PPI_PKT_LENGTHS"
trap.setRequiredFmt(0, pytrap.FMT_UNIREC, inputspec)
rec = pytrap.UnirecTemplate(inputspec)

def do_classification(rec):
    # Write algorhitm here

    if len(rec.PPI_PKT_LENGTHS) > 0:

        pkt_directions = np.array(rec.PPI_PKT_DIRECTIONS)
        pkt_lengths = np.array(rec.PPI_PKT_LENGTHS)

        print(rec.PPI_PKT_DIRECTIONS)

        pkts = pkt_directions*pkt_lengths

        print(pkts)

    #print(rec.TLS_SNI)

    #ktrap.send(rec.TLS_SNI, 0)

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