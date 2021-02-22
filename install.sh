#!/bin/bash

if ! python3 -v COMMAND &> /dev/null
then
    echo "installing Python3..."
    brew install python
fi
if ! python3 -c 'import pandas' 2>/dev/null 
then
    echo "installing pandas..."
    pip3 install pandas
fi
if ! python3 -c 'import matplotlib' 2>/dev/null 
then
    echo "installing matplotlib..."
    pip3 install matplotlib
fi 

echo -e "Python3 and modules installed.\nUsage:\npython3 train.py [--plot]\npython3 predict.py [--plot]"