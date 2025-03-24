---
title: Pipuv-Network-Classifier
author: Josef Vetrovsky
date: 5. 5. 2025
school: SPSE Jecna
---

# How to setup

This software is tested only on **Oracle Linux 9.3 and 9.5**.     

## Requirements

**Git**, so you can clone the repo.

## Prepare our VM

Simply run:

```Bash
sudo ./setup_vm.sh
```

This script will download all the needed packages and download and install ipfixprobe for you

## Run with simple logger

One of the provided scripts will start the application, which will simply log the every classified packet to the screen      
After setting up our vm, we can run:

```Bash
./start_application_logger.sh
```

# 3d-party libraries

Cesnet NEMEA - https://github.com/CESNET/Nemea              
Cesnet Ipfixprobe - https://github.com/CESNET/ipfixprobe                
Nemea-pytrap and all other modules used are also part of the NEMEA project

# Sources

Cesnet NEMEA documentation on Github - https://github.com/CESNET/Nemea          
Cesnet Ipfixprobe documentation on Github - https://github.com/CESNET/Nemea                
Cesnet Ipfixprobe documentation on Github Pages - https://cesnet.github.io/ipfixprobe/          
Cesnet Nemea-pytrap documentation - https://nemea.liberouter.org/doc/pytrap/index.html          
All other modules used are also a part of the NEMEA project       

# Resume
