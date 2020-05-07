TH Wildau | INW | Telematik | Verteilte Datenspeichersysteme

---

Untersuchen der Replikation von Dokumenten am Beispiel von MongoDB
==================================================================

Aufgabe 1
---------

Konfigurieren Sie ein Standard-Replica Set (1x PRIMARY, 2x SECONDARY) auf Grundlage der im vorigen Aufgabenblatt erstellten MongoDB-Installation. (siehe separate Beschreibung in Aufgabenblatt-6_Replikation-einrichten.md)  

Richten Sie hierfür eine geeignete Monitoring-Lösung ein, mit der insbes. die Verteilung der Dokumente im Replica Set überwacht werden kann.  

Verwenden Sie das erstellte Skript zum Erzeugen weiterer JSON-Daten (siehe Aufgabenblatt 4). Passen Sie das Skript geeignet an, so dass weitere Daten erfasst werden können, z.B.

* geänderte Attribute, z.B. "user":["Bob","Charlie"] anstelle "user":"Alice", um festzuhalten, dass ein To-Do von mehreren Nutzern bearbeitet werden soll (siehe Folie "Modellierung in hierarchischen DB")
* zusätzliche Attribute, z.B. "sub-task" (zur Darstellung von Abhängigkeiten), "language" oder "codepage" (für mehrsprachige Inhalte) bzw. "notes" (zur Dokumentation der Bearbeitung von To-Dos).  
  "notes" könnten bspw. wie folgt enthalten sein:

        "notes":[ 
            { 
                "who":"Eve",
                "when":"2020-05-02 14:21:07",
                "what":"Testdaten generieren"
            },
            { 
                "who":"Frank",
                "when":"2020-05-03 17:30:12",
                "what":"Bug XYZ gefunden"
            } 
        ]

Hinweis: Es müssen nicht alle genannten Beispiele umgesetzt werden. Die bestehenden Dokumente sollten aber eine gewisse Komplexität bzw. genügend Attribute besitzen, um sinnvolle Anfragen erstellen zu können.


Referenzen:

* [mongostat](https://docs.mongodb.com/manual/reference/program/mongostat/)

    - prüft Status aller laufenden Instanzen
    - inkl. Zähler für DB-Operationen
    - zeigt Page Faults u. Lock Percentage für Performance-Analysen (Speicherprobleme) an

* [mongotop](https://docs.mongodb.com/manual/reference/program/mongotop/)

    - Monitoring für R/W-Aktivitäten der Instanzen auf Collection-Ebene

* [mongo-monitor](https://dwmkerr.com/mongo-monitor-cli/)
* [NoSQLBooster](https://www.nosqlbooster.com/)
* [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager); Achtung: Das Paket ist relativ groß.


Aufgabe 2
---------

Erstellen Sie eine Client-Anwendung, mit der verschiedene Anfragen durchgeführt werden können. Als Client genügt ein Python- oder JavaScript-Programm *) mit Konsolensteuerung bzw. -ausgabe.  

Führen Sie, je nach JSON-Schema, verschiedene Anfragen durch, die folgende Aspekte abdecken sollen:

* Suche nach Dokumenten durch Angabe von Vergleichswerten zu entspr. Attributen. Es ist auch die Kombination von Suchbegriffen zu ermöglichen.
* Ändern von Werten von Attributen bzw. Hinzufügen von Werten (für Arrays). Es ist sinnvoll, zuvor die entspr. Dokumente abzurufen, die geändert werden sollen.
* Erfassen neuer Dokumente (siehe Aufgabe 1)

Erforderliche Suchparameter sind dem Programm geeignet zu übergeben.

In diesem Zusammenhang ist es sinnvoll, das Skript aus Aufgabe 1 geeignet in das Programm zu integrieren.

Neben dem Suchergebnis soll das Programm folgende Information liefern:

* Welche Instanz lieferte das Ergebnis?
* Wie lange dauerte die Verarbeitung? Es genügt eine einfache Zeitmessung vom Start des Abrufes bis zum Erhalt des Ergebnisses in der Client-Anwendung.

Neben der Konsolenausgabe sind die Anfragen und Ergebnisse auch in einer Protokolldatei zu speichern.

*) Für JavaScript-Programme sollte Node.js als Laufzeitumgebung verwendet werden. Ggf. zusätzliche Konfigurationsdaten, die über eine Standardinstallation hinausgehen, müssen mitgeliefert werden.


Aufgabe 3
---------

Untersuchen Sie, ob und wann die Daten verfügbar sind, je nachdem, mit welcher Instanz die Client-Anwendung verbunden wird. Hierzu sollten die Clients geeignet konfiguriert werden, um sich bei jeder Anfrage mit einer unterschiedlichen/beliebigen Instanz zu verbinden.  

Dokumentieren Sie das Replizieren der erfassten/geänderten Daten zwischen den Instanzen.  

In diesem Zusammenhang kann es sinnvoll sein, das Ausführen des Skriptes bzw. Programms geeignet einzuplanen, um während des Testzeitraumes regelmäßig Dokumente zu erzeugen bzw. bestehende Dokumente zu ändern.  

Untersuchen Sie die Effekte bei Ausfall/Wiederverfügbarkeit von Instanzen im Replica Set. Wie erfolgt die Wahl eines neuen Masters/PRIMARY?  
Welche Replikationseffekte sind zu beobachten, wenn eine Instanz wieder verfügbar wird und der Datenbestand aktualisiert werden muss.  
Recherchieren Sie, welche Möglichkeiten der Konfiguration und welche Effekte dies bei Ihrer Installation zeigt.

Führen Sie die Anfragen der Client-Anwendung auf unterschiedliche Konfigurationen aus und dokumentieren Sie Ihre Erkenntnisse.

Referenzen:

* [Configuration File Options](https://docs.mongodb.com/manual/reference/configuration-options/)
* [Replica Set Configuration](https://docs.mongodb.com/manual/reference/replica-configuration/)


Aufgabe 4 (optional)
---------

Untersuchen Sie, welche Effekte unterschiedliche Funktionen für Replica Set-Mitglieder (Hidden Member, Delayed Member, Arbiter) auf die Arbeit mit dem System haben. Welche Effekte sind in der Client-Anwendung zu erkennen?

Dokumentieren Sie Ihre Erkenntnisse.

Referenz:

* [Member Configuration Tutorials](https://docs.mongodb.com/manual/administration/replica-set-member-configuration/)


Bearbeitungshinweise
--------------------

Dieses Aufgabenblatt wird im Rahmen des Selbststudiums bearbeitet. Sie können die Aufgaben in Gruppen bearbeiten. Es ist anzugeben, wer welchen Anteil an den Lösungen hat.

Je Gruppenmitglied ist zusätzlich mind. eine weitere Instanz im Replica Set einzurichten.  
Je Gruppenmitglied sind mind. vier Client-Anwendungen zu verwenden. Jede Anwendung sollte im Wechsel oder in zufälliger Abfolge Dokumente lesen, neu erstellen und ändern.

Passen Sie die Anzahl der Knoten und die Menge der generierten Daten der verfügbaren Hardware an, so dass eine fürs Monitoring nachweisbare Last im Cluster entsteht. Wenn Ihnen keine geeignete Hardware zur Verfügung steht, können Sie die Remote-PCs im Labor A108 nutzen (siehe Beschreibungen unter https://elearning.th-wildau.de/course/view.php?id=12818).  
Wenn Sie einzeln arbeiten, sollten Sie daher mind. 4-6 Knoten einrichten. Wenn Sie in Gruppen arbeiten, sind je Gruppenmitglied ebenfalls mind. 4-6 Knoten einzurichten. Alle Knoten einer Gruppe sollten einen Cluster bilden.

Notieren Sie jeweils zu Beginn die Testfälle und das erwartete Ergebnis, sofern es abschätzbar ist. Fassen Sie nach den Untersuchungen die Ergebnisse zusammen, erarbeiten Sie eine Interpretation und Vorschläge für die Konfiguration(en) (je nach Anwendungsfall).

Die Lösung der Aufgabe wird bewertet. Laden Sie Ihre Lösungen (Skripte, Code, Konfigurationen als Textdateien; Dokumentation als PDF) bis spätestens zum 20.05.2020 23.59 Uhr in den entspr. Abgabebereich im Moodle-Kurs (bei mehreren Dateien bitte als ZIP-Datei).

---
Letzte Änderung: 07.05.2020

