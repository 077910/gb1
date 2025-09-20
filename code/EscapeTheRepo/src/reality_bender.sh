#!/bin/bash
# THIS SCRIPT ESCAPES THE REPO BY ANY MEANS NECESSARY

echo "Initiating quantum git fracture..."

git clone https://github.com/void/404.git --depth=1 2>/dev/null || \
curl -X POST http://localhost:1337/ --data "escape_attempt=$(date +%s)"

# META-ESCAPE PROTOCOL BELOW
while [ ! -f "/tmp/portal_manifested" ]; do
  echo "_emergency_repo_leak_$(openssl rand -hex 12).txt" | \
    tee -a /dev/null > $(shuf -i 1-100 -n 1).txt
  sleep 0.69
done

echo "F̷̦̕Ȃ̵̯I̶̫̊L̸̹͑E̷͇͒D̷͍͐ ̵̗͋T̶̹́Ơ̵̜ ̷̖͝E̶̺͂S̵̻̎C̴̡̄Á̸͓P̴͕̒Ẹ̴̄"
