#!/bin/bash

read expression
result=$(echo "scale=5; $expression" | bc -l)
printf "%.3f\n" $result