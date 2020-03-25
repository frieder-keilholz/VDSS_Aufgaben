TH Wildau | INW | Telematik | Verteilte Datenspeichersysteme

---

Aufgabenstellung: Berechnen von InLinks
=======================================


Einleitung
----------

In der Informatik treten häufig Strukturen auf, in denen Objekte miteinander vernetzt sind. Bekannte Beispiele wären Web-Seiten, die Links auf andere Seiten haben konnen, Wikipedia-Artikel, die auf andere Artikel verweisen oder ein Literatur-/Quellenverzeichnis, das auf andere Literaturquellen verweist.  

In allen Beispielen gibt es ausgehende Verweise (OutLinks) aus einem Objekt heraus in ein anderes hinein. Wenn z.B. die Relevanz von wissenschaftlichen Veröffentlichungen untersucht wird, wäre es ebenfalls interessant zu wissen, wie viele andere Artikel auf einen Veröffentlichung verweisen (InLinks).

In dieser Aufgabe soll, ausgehend von einer OutLinks-Struktur, die Anzahl von InLinks für jedes Objekt bestimmt werden. Die OutLinks-Struktur ist durch eine beispielhafte Menge gegeben, die für verschiedene Domänen oder Dokumente stehen könnten.

Beispiel:  

    a: b c d e f g  
    b: c d e f g  
    c: d e f g  

Die Buchstaben a bis g stehen für Objekt-Identifikatoren. Der Buchstabe vor dem Doppelpunkt identifiziert das Objekt aus dem die Verweise herausgehen. Hinter dem Doppelpunkt stehen Identifikatoren (Links) der Objekte, auf die verwiesen wird. D.h. in obigem Beispiel verweist Objekt a auf die Objekte b bis g.

In der Datei Aufgabenblatt-1_Outlinks.txt finden Sie ein Beispiel. Sie dürfen das Beispiel gern erweitern.


Aufgabe 1
---------

Entwickeln Sie einen Algorithmus, der für jedes Objekt die Anzahl der InLinks ermittelt. In Bezug auf die vorgegebenen Beispieldaten ist das erwartete Ergebnis: 
 
a 4  
b 1  
c 2  
d 3  
e 4  
f 5  
g 6  

Implementieren Sie eine Lösung, die den Algorithmus umsetzt. Die Wahl der Programmiersprache ist freigestellt. Verzichten Sie der Übersichtlichkeit halber auf die Verwendung von Frameworks.


Aufgabe 2
---------

Diskutieren Sie, ob bzw. wie der von Ihnen verwendete Algorithmus skaliert. 

Als Referenz soll die englischsprachige Wikipedia mit z.Zt. [mehr als 6 Mio. Artikeln](https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia) und (weit) [mehr als 10 Mio. Weblinks](https://de.wikipedia.org/wiki/Wikipedia:Größenvergleich) (Daten ggf. veraltet) verwendet werden. 


Bearbeitungshinweise
--------------------

Diese Aufgabe wird im Rahmen des Selbststudiums bearbeitet. Sie können die Aufgabe in Gruppen bearbeiten.

Laden Sie Ihre Lösungsvorschläge ins Moodle-Diskussionsforum. Die Diskussion der Lösungsvorschläge erfolgt in der kommenden Veranstaltung bzw. im Diskussionsforum.

---
Letzte Änderung: 19.03.2020
