#!/bin/bash
directory="$HOME/gneiss/assignment_3"
# using ~ instead of $HOME fails here
if [ -d $directory ]; then
echo "Submission directory exists"
else
echo "You need to create it with \"mkdir\""
fi
