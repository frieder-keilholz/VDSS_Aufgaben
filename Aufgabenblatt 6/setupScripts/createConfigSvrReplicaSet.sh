for i in 1 2 3
do
	echo Erstelle Verzeichnis $i
	mkdir configSvrInstance_${i}
done

for i in 1 2 3
do
	echo Starte ConfigSvr Instanz $i
	mongod --configsvr --replSet cfgrs1 --dbpath configSvrInstance_${i}/ --bind_ip 192.168.2.162 --port 800${i}&
done



