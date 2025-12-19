#!/usr/bin/env bash

export EMAIL=$(jq -r '.email' /data/options.json)
export PASSWORD=$(jq -r '.password' /data/options.json)
export DEVICE_ID=$(jq -r '.device_id' /data/options.json)

python /app/app.py