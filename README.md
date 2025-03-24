---
title: Pipuv-Network-Classifier
author: Josef Vetrovsky
date: 5. 5. 2025
school: SPSE Jecna
---

# About

This simple network classifier tightly works with the NEMEA framework by CESNET. It provides several different models to accomplish the task. By default, the best one is chosen.           
It simply classifies 443 services only by first 30 packets fo the communication.

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

# Application diagram

Since NEMEA framework is based on microservices, also this project uses such a concept. Several NEMEA modules are connected together with unix sockets. At the end we have a special kind of module, which either does something with the classification or simply logs the data using the logger module.

![Diagram](omega_picture.svg)

The first module listens to an interface, creates flows from packets and returns the data in certain format.            
The unirec filter filters out all unneccessary data. We are only interested in services over 443.           
Finally our classifier classifies the flow and sends it to another unix socket.             
That final socket can by caught by a logger or any other specialized module.

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
