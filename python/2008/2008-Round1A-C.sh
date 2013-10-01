#!/bin/bash

#Solves small dataset only, can't output after 256 digits

COUNTER=0
for i in `cat $1`; do
    NUMBER=`genius --maxdigits=256 --exec="(3 + sqrt(5))^$i" | cut -d '.' -f 1`

    if [ $COUNTER -gt 0 ]; then
        MOD=`genius --maxdigits=256 --exec="$NUMBER % 1000"`
        if [ $MOD -le 9 ]; then
            echo "Case #$COUNTER: 00$MOD"
        elif [ $MOD -le 99 ]; then
            echo "Case #$COUNTER: 0$MOD"
        else
            echo "Case #$COUNTER: $MOD"
        fi
    fi
    COUNTER=`expr $COUNTER + 1`
done
