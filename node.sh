#!/usr/bin/env bash

java -jar seleniumserver.jar \
    -role node \
    -hub http://localhost:4444/grid/register \
    -Dwebdriver.chrome.driver="./chromedriver" \
    -browser browserName=chrome,maxInstances=5 \
    -browser browserName=firefox,maxInstances=5
