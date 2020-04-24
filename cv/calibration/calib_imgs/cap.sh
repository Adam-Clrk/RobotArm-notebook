#!/bin/bash
#
# Example:
# ./cap.sh 20
# will prompt to take 20 photos
#

for i in $(seq -f "%02g" 1 $1)
do
  echo "Press enter to take picture out_$i.jpg"
  read
  raspistill -n -w 2592 -h 1936 -o aout_$i.jpg
  echo "out_$i.jpg done"
done
