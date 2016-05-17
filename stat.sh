#!/bin/bash
i=0

#1440 minutes in a day
echo "Machine1: Downloading cnn.com and google.com " >> machine1Stat.txt
while [ $i -lt 1440 ]
do
    i=$(($i+1))

    date +"%r" >> machine1Stat.txt
    #storage info in human readable format
    df -h | tail -1 | awk '{print "Disk: " "Used " $3 ", Avail " $4 }' >> machine1Stat.txt
    
    #check memory usage
    free | head -2 | tail -1 | awk '{print "Memory: " "Used " $3 ", Free " $4 }' >> machine1Stat.txt 

    #get cpu usage
    echo -n "CPU usage: " >> machine1Stat.txt
    ps aux | awk 'BEGIN{ cpuTotal = 0} {cpuTotal += $3}; END{print cpuTotal}' >> machine1Stat.txt
    echo >> machine1Stat.txt
    sleep 60
done


