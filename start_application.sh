#!/bin/bash

cd src

sudo ipfixprobe -i 'raw;ifc=ens3' -p "pstats" -p "tls" -o "unirec;i=u:mysocket:timeout=WAIT;p=(pstats,tls)" &
/usr/bin/nemea/unirecfilter -F 'port == 443' -i u:mysocket,u:filtered &
src/flowclassifier.py -i u:filtered,u:logged &
/usr/bin/nemea/logger -i u:logged -t