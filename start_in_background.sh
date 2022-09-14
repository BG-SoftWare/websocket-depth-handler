#!/bin/bash
source buildname
rm .stopped_by_user
screen -dmS $BUILDNAME ./start.sh