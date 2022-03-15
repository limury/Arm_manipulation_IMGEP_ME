#!/bin/bash

i=0

mkdir -p ../IMGEP_data
dirs=$(find -name "IMGEP*" -type d)
for dir in $dirs        
do 
  cd $dir
  for f in *
  do
    mv -- "$f" "$i-$f"
  done
  cd ..
  ((i=i+1))

  mv $dir/* ../IMGEP_data/
  rm -rf $dir

done 
