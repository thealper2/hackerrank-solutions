#!/bin/bash

declare -a A

while read text
do
    A=(${A[@]} $text)
done

echo "${A[@]}" | tr ' ' '\n' | sort | uniq -u | tr '\n' ' '