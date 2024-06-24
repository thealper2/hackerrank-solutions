#!/bin/bash

A=($(cat))
A=("${A[@]}" "${A[@]}" "${A[@]}")
echo ${A[@]}