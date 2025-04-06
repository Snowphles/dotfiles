#!/bin/sh
sed -i \
         -e 's/#090C10/rgb(0%,0%,0%)/g' \
         -e 's/#ffffff/rgb(100%,100%,100%)/g' \
    -e 's/#0d1117/rgb(50%,0%,0%)/g' \
     -e 's/#ffffff/rgb(0%,50%,0%)/g' \
     -e 's/#0d1117/rgb(50%,0%,50%)/g' \
     -e 's/#d3dae3/rgb(0%,0%,50%)/g' \
	"$@"
