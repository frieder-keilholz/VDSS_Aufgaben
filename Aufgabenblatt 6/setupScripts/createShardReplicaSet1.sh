for i in 1 2 3
do
	echo Erstelle Verzeichnis $i
	mkdir rs1_instance_${i}
done

for i in 1 2 3
do
	echo Starte ShardInstanz $i
	mongod --shardsvr --replSet rs1 --dbpath rs1_instance_${i}/ --bind_ip 192.168.2.162 --port 900${i}&
done



