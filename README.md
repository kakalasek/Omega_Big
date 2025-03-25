---
title: Pipuv-Network-Classifier
author: Josef Vetrovsky
date: 5. 5. 2025
school: SPSE Jecna
---

# About

This simple network classifier tightly works with the NEMEA framework by CESNET. It provides several different models to accomplish the task. By default, the best one is chosen.           
It simply classifies 443 services only by first 30 packets from the communication.

## Datasets

Two different datasets were used to train the models.           
First dataset is made up of **aggregated network captures from family members, friends and myself**. It is not so effective, but because the amount of data is not so great, the models could be trained in fair amount of time. It also cant really classify all the classes, simply because the data does not involve that many services.             
The second dataset is **a very large file of network flows from CESNET**. This dataset was annonymized before, so no IP addresses are present. It contains larger amount of different services and data in general. The best models offered are trained on this dataset.

## Dataset processing

1. **Extract our desired columns**      
    There is a lot of column in the datasets, which were not needed. Only packet sizes and directions of the first 30 packets in each flow and TLS_SNI field were extracted. The TLS_SNI field contains a value used for annotation.
2. **Multiply packet directions and sizes**                 
    In order to reflect the packet direction

# How to setup

This software is tested only on **Oracle Linux 9.3 and 9.5**.     
NEMEA needs an rpm based distribution in order to work properly and be setup easily.

## Requirements

**Git**, so you can clone the repo. The rest is done by the setup script.

## Prepare our VM

Simply run:

```Bash
sudo ./setup_vm.sh
```

This script will download all the needed packages and download and install ipfixprobe for you

## Run with simple logger

One of the provided scripts will start the application, which will simply log every classified packet to the screen terminal        
We also need to specify the network interface we want to monitor             
After setting up our vm, we can run:

```Bash
./start_application_logger.sh <network_interface_name>
```

Since starting Ipfixprobe needs sudo privileges, you will be asked to enter your password. Then you will probably need to wait a while until the system starts to log something, since Ipfixprobe first needs to catch some packets in order to return some flows.              
After some time the system should start to log in this format: *TIMESTAMP,DST_IP,SRC_IP,CLASS*

# Application diagram

Since NEMEA framework is based on microservices, also this project uses such a concept. Several NEMEA modules are connected together with unix sockets. At the end we have a special kind of module, which either does something with the classification or simply logs the data using the logger module.

![Diagram](omega_picture.svg)

The first module listens to an interface, creates flows from packets and returns the data in certain format.            
The unirec filter filters out all unneccessary data. We are only interested in services over port 443.           
Finally, our classifier classifies the flow and sends it to another unix socket.             
That final socket can be caught by a logger or any other specialized module.

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
