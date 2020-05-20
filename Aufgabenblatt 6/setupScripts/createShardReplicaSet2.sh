for i in 1 2 3 4 5 6
do
	echo Erstelle Verzeichnis $i
	mkdir rs2_instance_${i}
done

for i in 1 2 3 4 5 6
do
	echo Starte ShardInstanz $i
	mongod --shardsvr --replSet rs2 --dbpath rs2_instance_${i}/ --bind_ip 192.168.2.162 --port 910${i}&
done

