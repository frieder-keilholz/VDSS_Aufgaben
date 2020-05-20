for i in 7 8 9
do
	echo Erstelle Verzeichnis $i
	mkdir instance_${i}
done

for i in 7 8 9
do
	echo Starte Instanz $i
	mongod --replSet rs1 --dbpath instance_${i}/ --port 800${i} &
done



