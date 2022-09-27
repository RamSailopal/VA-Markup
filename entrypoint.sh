#!/bin/bash
apt-get update
apt-get install -y wget python3 python3-pip pandoc
pip3 install pyOpenSSL==22.0.0
pip3 install scrapy wget
