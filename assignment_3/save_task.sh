#!/bin/bash

newTask="think of a sample task"
echo $newTask >> ~/task_database.txt

echo "one"
echo "first arg: $1"
echo "two"
echo "first arg: $2"
echo "three"
echo "first arg: $3"

newTask=$1
echo "$newTask"
