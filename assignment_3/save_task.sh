#!/bin/bash

newTask="think of a sample task"
echo $newTask >> ~/task_database.txt

newTask="when you see this the task text has been expanded"

echo $newTask
echo "$newTask"
echo '$newTask'

echo "one"
echo "first arg: $1"
echo "two"
echo "first arg: $2"
echo "three"
echo "first arg: $3"

newTasj=$1
echo "$newTask"
