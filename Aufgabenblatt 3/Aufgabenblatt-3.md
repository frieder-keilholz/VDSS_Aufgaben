TH Wildau | INW | Telematik | Verteilte Datenspeichersysteme

---

Arbeiten mit einem Cluster am Beispiel von Redis
================================================


Aufgabenstellung
----------------

Erstellen Sie ein einfaches verteiltes System (a.k.a. Cluster) mittels Redis auf Grundlage der im vorigen Aufgabenblatt erstellten Redis-Installation.  

Verwenden Sie das im vorigen Aufgabenblatt bearbeitete Beispiel (To-Do-Anwendung) zum Erzeugen weiterer Daten.  

Die Anwendung ist dahingehend zu erweitern, dass zu jedem To-Do-Eintrag gespeichert wird, von wem der Eintrag stammt (Nutzername) bzw. auf welchem System der Eintrag erfasst wurde (Name oder IP-Adresse/Port des Redis-Knotens). Welche Variante Sie wählen, ist Ihnen überlassen. Diese Information kann bei der Nachverfolgung der Verteilung helfen.  

Es wird empfohlen, sowohl initiale als auch weitere Daten mittels Skript zu erzeugen und den Redis-Knoten zu übergeben. Es ist sinnvoll, hierbei wie folgt vorzugehen:  

1. Richten Sie mehrere Redis-Knoten ein. Dies sollte schon mit der Cluster-Option erfolgen (siehe redis.conf).
2. Starten Sie die den ersten Knoten.
3. Erzeugen Sie eine ausreichende Menge an Daten (z.B. 1000 Einträge oder mehr) und weisen Sie diese dem Knoten zu.
4. Beenden Sie den Knoten.
5. Fahren Sie für jeden Knoten mit den Schritten 2 bis 4 fort.

Damit sollte jeder Knoten einen initialen Datenbestand besitzen

6. Starten Sie den Cluster.
7. Verarbeiten Sie mittels Skript regelmäßig weitere Daten (Hinzufügen neuer Daten, Ändern bestehender Daten, Löschen bestehender Daten) und weisen Sie diese (entspr. des Erstellers des Eintrages) dem entspr. Knoten zu.

Mit Schritt 7 soll simuliert werden, dass mit dem System gearbeitet wird.


Aufgaben
--------

Bearbeiten Sie die folgenden Aufgaben:

* Fragen Sie regelmäßig Daten sowie Informationen über den Cluster bzw. die einzelnen Knoten ab. Auch dies kann skript-gesteuert erfolgen.
* Richten Sie eine geeignete Monitoring-Lösung ein, um insbes. die Verteilung der Daten im Cluster überwachen zu können.
* Untersuchen Sie, ob und wann die erfassten/geänderten Daten auf anderen Knoten verfügbar sind.
* Experimentieren Sie mit unterschiedlichen Replikationsfaktoren. Welche Effekte können Sie beobachten?
* Untersuchen Sie, wie sich der Cluster beim Ausfall/Hinzufügen von Knoten verhält. Welche Effekte können Sie beobachten?

* (optional) Übertragen Sie die komplette Datenbank eines Knotens auf andere Knoten (Backup & Restore), bevor diese in den Cluster aufgenommen werden.
* (optional) Experimentieren Sie, wie viele Knoten auf Ihrer Hardware laufen. Je nach verfügbarer Hardware können Sie die Knoten lokal, mittels Docker, VM oder auf mehreren physischen Geräten betreiben.

Sämtliche Arbeitsschritte und -ergebnisse sind zu dokumentieren.


Hilfreiche Quellen:

* [Redis cluster tutorial](https://redis.io/topics/cluster-tutorial)
* [Setting Up A High Available Multi Node Redis Cluster](https://cleanprogrammer.net/setting-up-a-high-available-multi-node-redis-cluster/)
* Redis-Cluster-Client für Python: [redis-py-cluster](https://redis-py-cluster.readthedocs.io/en/master/)
* [How to Monitor Redis](https://blog.serverdensity.com/monitor-redis/)
* [Redis Persistence](https://redis.io/topics/persistence)
* [Guide to Backup and Restore Redis Database and Automate](https://www.basezap.com/guide-to-backup-and-restore-redis-database-and-automate-backups/)


Bearbeitungshinweise
--------------------

Dieses Aufgabenblatt wird im Rahmen des Selbststudiums bearbeitet. Sie können die Aufgaben einzeln oder in Gruppen bearbeiten. Es ist anzugeben, wer welchen Anteil an den Lösungen hat.

Passen Sie die Anzahl der Knoten und die Menge der generierten Daten der verfügbaren Hardware an, so dass eine fürs Monitoring nachweisbare Last im Cluster entsteht.  
Wenn Sie einzeln arbeiten, sollten Sie daher mind. 4-6 Knoten einrichten. Wenn Sie in Gruppen arbeiten, sind je Gruppenmitglied ebenfalls mind. 4-6 Knoten einzurichten. Alle Knoten einer Gruppe sollten einen Cluster bilden.

Die erfolgreiche Bearbeitung der als optional gekennzeichneten Aufgaben wird im Rahmen der Bewertung zusätzlich honoriert.

Die Lösung der Aufgabe wird bewertet. Laden Sie Ihre Lösungen (Skripte, Code, Konfigurationen als Textdateien; Dokumentation als PDF) bis spätestens zum 22.04.2020 23.59 Uhr in den entspr. Abgabebereich im Moodle-Kurs (bei mehreren Dateien bitte als ZIP-Datei).


---
Letzte Änderung: 09.04.2020
