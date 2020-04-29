TH Wildau | INW | Telematik | Verteilte Datenspeichersysteme

---

Vorbereitung für die Arbeit mit Dokumentenspeichern
===================================================

Aufgabe
-------

Entwickeln Sie ein Skript o. Programm, das die Einträge der To-Do-Anwendung (siehe vorige Aufgabenblätter) aus den Redis-Datenbanken ausliest und in ein JSON-Dokument konvertiert. Je Nutzer (siehe Aufgabenblatt 3) soll ein separates JSON-Dokument erstellt werden.   
Jedes Dokument sollte eine eindeutige ID (Attribut _id) erhalten.  

Die Struktur des JSON-Dokumentes hängt von den verwendeten Key/Value-Daten in der Redis-Anwendung ab. Im Folgenden ein Beispiel:

    {
      "_id":"5cb82e80810c19729de860ea",
      "todo":"Skript schreiben",
      "text":"Skript erstellen, das Daten aus Redis ausliest und nach MongoDB schreibt",
      "until":"2020-04-29 23:59:59",
      "user":"Max Muster",
      "nodes":["node-1","node-3","node-5"]
    }

Hinweise:  

* Das Attribut _id steht für die [ObjektId](https://docs.mongodb.com/manual/reference/method/ObjectId/) in MongoDB.  
  Im Rahmen der Aufgabe genügt ein eindeutiger 12-stelliger hexadezimaler Wert.
* Ob der until-Wert nach ISO 8601 gebildet oder als Unix Timestamp (dezimal oder hexadezimal) angegeben wird, ist Ihnen überlassen.
* Die nodes enthalten die Namen aller Knoten, auf denen die entspr. Information gespeichert wird, als Array.

Die Wahl der Programmiersprache ist Ihnen freigestellt.


Bearbeitungshinweise
--------------------

Dieses Aufgabenblatt wird im Rahmen des Selbststudiums bearbeitet. Sie können die Aufgaben in Gruppen bearbeiten.

Laden Sie Ihre Lösungen (Code als Textdatei, sonst PDF) ins Diskussionsforum im Moodle-Kurs. Die Diskussion der Lösungsvorschläge erfolgt in der kommenden Veranstaltung bzw. im Diskussionsforum.


---
Letzte Änderung: 23.04.2020
