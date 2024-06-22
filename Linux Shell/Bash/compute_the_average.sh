#!/bin/bash

read count

sum=0

for (( i=1; i<=$count; i++ ))
do
    read number
    sum=$(echo "$sum + $number" | bc)
done

average=$(echo "scale=3; $sum / $count" | bc)
printf "%.3f\n" $average