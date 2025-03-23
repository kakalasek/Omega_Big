#!/bin/bash

function cleanup {
    exit 0
}

trap cleanup SIGINT
trap cleanup SIGQUIT

sudo ipfixprobe -i 'raw;ifc=ens3' -p "pstats" -p "tls" -o "unirec;i=u:mysocket:timeout=WAIT;p=(pstats,tls)" &
/usr/bin/nemea/unirecfilter -F 'port == 443' -i u:mysocket,u:filtered &
./flow_classifier.py -i u:filtered,u:logged &
/usr/bin/nemea/logger -i u:logged -t