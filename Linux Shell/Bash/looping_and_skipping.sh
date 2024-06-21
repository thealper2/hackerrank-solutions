#!/bin/bash

for sayi in {1..99}
do
    if [[ `expr $sayi % 2` == 1 ]]
    then
        echo $sayi
    fi
done