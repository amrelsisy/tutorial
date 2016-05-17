#!/bin/bash
i=0

#1440 minutes in a day
echo "Machine2: Finding closest pair” >> machine2Stat.txt
while [ $i -lt 1440 ]
do
    i=$(($i+1))

    date +"%r" >> machine2Stat.txt
    #storage info in human readable format
    df -h | tail -1 | awk '{print "Disk: " "Used " $3 ", Avail " $4 }' >> machine2Stat.txt
    
    #check memory usage
    free | head -2 | tail -1 | awk '{print "Memory: " "Used " $3 ", Free " $4 }' >> machine2Stat.txt 

    #get cpu usage
    echo -n "CPU usage: " >> machine2Stat.txt
    ps aux | awk 'BEGIN{ cpuTotal = 0} {cpuTotal += $3}; END{print cpuTotal}' >> machine2Stat.txt
    echo >> machine2Stat.txt
    sleep 60
done


