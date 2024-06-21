#!/bin/bash

read -p "" character

if [[ ( $character == "Y") || ( $character == "y" ) ]]
then
    echo "YES"
elif [[ ( $character == "N") || ( $character == "n") ]]
then
    echo "NO"
fi