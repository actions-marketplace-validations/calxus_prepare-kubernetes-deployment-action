#!/bin/sh

pip3 install -r requirements.txt
python3 /prepare.py --service-name $1 --service-replica-count $2 --image-name $3 --image-namespace $4 --image-version $5