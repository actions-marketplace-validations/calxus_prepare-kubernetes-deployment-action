#!/bin/sh

pip3 install -r /requirements.txt
python3 /prepare.py --service-name $2 --service-replica-count $3 --image-name $4 --image-namespace $5 --image-version $6 --service-envvars "$7"
if [ "$1" = true ] ; then
    cat /service/values.yaml
fi
cp -rp /service service