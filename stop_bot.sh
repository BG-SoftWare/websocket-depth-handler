#!/bin/bash
source buildname
touch .stopped_by_user
screen -S $BUILDNAME -X stuff "^C"
