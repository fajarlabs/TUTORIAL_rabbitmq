#!/bin/sh

# initial MQTT account
hostname="sanscloud.sanscloud.co.id"
port=1883
username="sans"
password="Rab2410"
id="GTW1"
topic="channels/kementan/publish"
iot_file="/tmp/store.log"

minimumsize=20000
actualsize=$(wc -c <"$iot_file")
if [ $actualsize -ge $minimumsize ]; then
    echo "Size is over $minimumsize bytes"
    rm /tmp/store.log
    touch /tmp/store.log
else 
    echo "File size is normal"
fi

if [ ! -e "$iot_file" ]; then
    echo "File not exist"
else
    # read file
    while read line; do
        # reading each line
        msg_line = ${line:1}
        msg_line = ${msg_line::-1}
        msg_line = $id-$msg_line
        echo $msg_line
        # remove line first
        mosquitto_pub -d -h $hostname -p $port -u $username -P $password -q l -i $id -t $topic -m "$msg_line"
        # remove per-line 
        sed -i '1d' $iot_file
        # done
    done < $iot_file
fi
