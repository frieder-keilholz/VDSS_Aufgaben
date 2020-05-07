# Replikation mit MongoDB einrichten (lokal)

Die folgende Beschreibung bezieht sich auf ein Linux-System und beschreibt die Einrichtung eines Replica Sets (a.k.a. Cluster) unter MongoDB.  
Es wird eine Standard-Installation von MongoDB vorausgesetzt.


## Allgemeine Einrichtung

* Ggf. Server stoppen

        $ service mongod stop

    oder 

        $ systemctl stop mongod

* Instanzen starten

    Die Hinweise gelten für alle Instanzen, siehe auch Punkt "Weitere Instanzen für RS starten" weiter unten.

    Je Instanz in einem Terminalfenster:

        $ mongod --port PORT --dbpath "DB_DATA_PATH" --replSet "REPLICA_SET_INSTANCE_NAME"

    oder im Hintergrund:

        $ mongod --port PORT --dbpath "DB_DATA_PATH" --replSet "REPLICA_SET_INSTANCE_NAME" &

    Je Instanz ist ein anderer Port und DB_DATA_PATH erforderlich. Beachte [Standard-Ports](https://docs.mongodb.com/manual/reference/default-mongodb-port/)  
    Die DB_DATA_PATH-Ordner müssen manuell angelegt werden. Nach dem Start einer Instanz werden in jedem DB_DATA_PATH-Ordner Daten der Instanz angelegt.  
    Instanzen, die zu einem Replica Set gehören sollen, müssen mit dem gleichen REPLICA_SET_INSTANCE_NAME gestartet werden. Der Name kann frei gewählt werden.
﻿
    Alternativ: Parameter in [Konfig.-Datei](https://docs.mongodb.com/manual/reference/configuration-options/) hinterlegen  
    Standardaufruf: 

        $ mongod --config "CONFIG_FILE_PATH"

    Falls Instanzen im Hintergrund gestartet wurden...

    Anzeige aller Hintergrund-Jobs

        $ jobs

    In den Vordergrund-Holen eines Jobs:

        $ fg [JOB_NUMBER]

* Client starten

        $ mongo --port PORT

    Von dieser Instanz wird der Cluster aufgebaut.

* Grundkonfiguration f. Replica Set (RS)

    - Replica Set initiieren:

        > rs.initiate()

    - RS-Konfiguration prüfen:

        > rs.conf()

    - RS-Status prüfen:

        > rs.status()

      bzw.

        > rs.status().members

    Hinweis: Es ist sinnvoll, Dokumente zu erfassen, damit beim Hinzufügen von Instanzen zum RS die Datenreplikation beobachtet werden kann.

* Weitere Instanzen für RS starten (siehe auch oben)

        $ mongod --port ANOTHER_PORT --dbpath "ANOTHER_DATA_PATH" --replSet "SAME_REPLICA_SET_INSTANCE_NAME"

* Mitglieder zum RS hinzufügen:

    - Hostname der Instanz ermitteln (in jeweiliger Instanz; bei lokaler Installation gilt wie gewohnt `localhost`):
	
        > db.serverStatus().host

    - Instanz dem RS hinzufügen (im Master/PRIMARY):

        > rs.add("HOST_NAME:PORT")

    - Hinweis: Voting funktioniert erst ab 3 Instanzen

    - RS-Status erneut prüfen:

        > rs.status().members

    - Wer ist Master/PRIMARY?
 
        > db.isMaster()


## Client mit RS verbinden (lokal)

* Angabe aller RS-Mitglieder im Connection String, z.B.

        mongodb://localhost:27100,localhost:27200,localhost:27300/?replicaSet=rsDemo

* Für Python dementspr. ...

        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27100,localhost:27200,localhost:27300/?replicaSet=rsDemo") 

    Siehe [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/)


## Weitere Aspekte

* Steuern der Verfügbarkeit geschriebener Dokumente

    Daten sind erst dauerhaft (für Clients) verfügbar, wenn auf der Mehrheit der RS-Mitglieder repliziert und im Journal dokumentiert wurde.  
    Aus Performance-Gründen, z.B. bei sehr großen Dokumenten, kann die Verfügbarkeit mittels "Write Concerns" gesteuert werden:

        > db.collection.insert( {... neues Dokument ...}, {writeConcern: {w: 3, wtimeout: 5000}} )

    Die Operation liefert eine Rückmeldung (an Client), ...  
	... nachdem das Dokument auf 3 Instanzen verteilt (geschrieben) wurde (Standard-RS mit 1x PRIMARY u. 2x SECONDARY)  
    ... oder nachdem ein Timeout nach 5 Sekunden auftritt.

    Entspr. Einstellungen sind auch in der Konfig.-Datei möglich (siehe oben).

* Blockieren der Replikation

    Dies kann sinnvoll sein, wenn o.a. Write Concerns erfüllt sind und ein weiteres Warten nicht notwendig ist, um Clients eine Rückmeldung zu geben.

        > db.runCommand({getLastError: 1, w: N, “wtimeout”: 5000});

    Die Operation initiiert das Blockieren der Replikation an weitere RS-Mitglieder, wenn auf N Mitglieder repliziert wurde.  
    Die Rückmeldung an einen Client wird ausgeführt, wenn N Replikate verfügbar sind -- oder weniger als 2. ;)

    Hinweis: Das Blockieren reduziert die Lese-Performance, falls N zu groß ist.

---
Last modified: 2020-05-07

