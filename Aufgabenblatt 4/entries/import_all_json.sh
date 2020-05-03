for filename in *.json; do
	echo $filename
	#	mongoimport $filename --db VDSS_5 --collection test --jsonArray
	mongoimport --db VDSS_5 --collection test3 --file $filename --jsonArray
done
