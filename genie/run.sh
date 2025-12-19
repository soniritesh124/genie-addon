#!/usr/bin/env sh
set -e

echo "Starting Genie Cloud Bridge"

# If running as Home Assistant add-on, options.json exists
if [ -f /data/options.json ]; then
  echo "Reading Home Assistant options.json"
  export EMAIL="$(jq -r '.email // empty' /data/options.json)"
  export PASSWORD="$(jq -r '.password // empty' /data/options.json)"
  export DEVICE_ID="$(jq -r '.device_id // empty' /data/options.json)"
else
  echo "options.json not found, using existing environment variables"
fi

echo "EMAIL=${EMAIL}"
echo "PASSWORD_SET=$( [ -n "$PASSWORD" ] && echo yes || echo no )"
echo "DEVICE_ID=${DEVICE_ID}"

exec python /app/app.py
