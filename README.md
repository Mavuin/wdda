# Wdda Semesterarbeit
In this repository you can find our whole group project for the module WDDA from the BFH.

Our task is the following: 

Project description:

Im Rahmen der Projektarbeit werden Lösungen zu den Themen Datenmanagement und Datenanalyse anhand einer praktischen Aufgabenstellung erarbeitet. Für ein Datensatz mit realen Umweltdaten wird in Teil (a) ein relationales DB-Schema erstellt und die Daten in eine SQLite-DB eingelesen, sowie Anfragen über die Datenbank erstellt. In Teil (b) werden einzelne Anfragen über eine python-DB-Schnittstelle erstellt. In Teil (c) – s. separate Aufgabenstellung – werden (andere) Daten nach R Studio importiert und analysiert.
Datensatz: Der Datensatz basiert auf dem öffentlich zugänglichen Datensatz Startup Success/Fail Dataset from Crunchbase1 und enthält Informationen zu Start-ups weltweit und deren Erfolg. Der Datensatz wurde zu Übungszwecken angepasst, arbeiten Sie also bitte nur mit dem angepassten Datensatz auf Moodle und nicht mit den Originaldaten von kaggle. Die wichtigsten Änderungen:
- Spalte «country» mit dem ausgeschriebenen Namen des Landes
- Leere bzw. unbekannte Werte in den Spalten «homepage_url», «category_list», «country_code», «country», «state_code», «region», «city», «funding_total_usd», «founded_at» und «first_funding_at» wurden auf «N/A» gesetzt.
- Datenfehler korrigiert: Einige Firmen in Taiwan waren dem Land «China» statt «Taiwan» zugeordnet.
- Die Stadt Caracas war fälschlicherweise der Region «COL – Other» zugeordnet. Die Region wurde auf «Caracas» korrigiert.
Organisatorisches:
- 3er-Gruppen, maximal 4er-Gruppen. Schreiben Sie sich in eine der auf Moodle für Ihre Klasse angelegten Gruppen ein
- Abgabe via Moodle gegen Ende des Vorlesungszeitraums
- Begleittext zur Abgabe enthält Name, Vorname aller Gruppenmitglieder
- Die Projektarbeit zählt 40% zur Modulnote
- Abgabe Deadline:
o Teile (a) und (b): Dienstag, 13. Juni 2022 (Moodle)
- Für jede Teilaufgabe gibt es ein separates Abgabeverzeichnis auf Moodle
1 https://www.kaggle.com/datasets/yanmaksi/big-startup-secsees-fail-dataset-from-crunchbase
Berner Fachhochschule Bachelor Wirtschaftsinformatik (BWI)
Wirtschaft Modul Datenmanagement & Datenanalyse (WDDA)

Auftrag, Teil (a), 8 Punkte:

- Verständnis des Datensatzes, insbesondere Diskussion in der Gruppe über die Bedeutung der einzelnen Attribute, sowie auch möglicher funktionaler Abhängigkeiten und Verwendung von Nullwerten.
- Erstellen eines normalisierten Datenmodells als ER-Diagramm in StarUML. Hinweis: In der Spalte «category_list» ist eine durch «|» getrennte Liste von Kategorien enthalten. Um die Aufgabe nicht zu kompliziert zu machen, müssen die darin enthalten Werte nicht weiter separiert werden; in der Datenbank ist es also ausreichend, hier nur ein String-Attribut mit demselben Wert wie im CSV zu haben. Allerdings muss bei Abfragen berücksichtigt werden, dass in dem Feld mehrere Kategorien vorkommen können.
- Befüllen der Datenbank mit den Originaldaten
- Erstellung von SQL-Anfragen, um folgende Fragen zu beantworten. Fragen 2-6 müssen auf den Tabellen des erstellten Modells gemacht werden, also weder auf den Ausgangsdaten noch der rekonstruierten View:

1.
a) Erstellen Sie eine View, welche den ursprünglichen CSV-Datensatz aus dem aus den von Ihnen definierten und befüllten Tabellen rekonstruiert.
b) Wie viele Datensätze sind in der View?
c) Zeigen Sie alle Spalten und Zeilen der View mit Start-ups aus der Stadt «Évry» an.

2.
Wie viele unterschiedliche Start-ups gibt es in der Datenbank, die mehr als USD 2‘000‘000‘000 (2 Milliarden) Funding bekommen haben?

3.
Wie viele Start-ups gibt es in der Datenbank, die im Bereich Spiele («Games») unterwegs sind?

4.
Erzeugen Sie eine Liste aller Städte, absteigend sortiert nach dem durchschnittlichen Funding, dass die Startups in dieser Stadt erhalten haben. Angezeigt werden sollen der Name der Stadt, der Ländercode und das auf 2 Nachkommastellen gerundete durchschnittliche Funding.

5.
Einige Start-ups haben mehrere Finanzierungsrunden durchlaufen. Welches Unternehmen in Indien hat im Schnitt pro Finanzierungsrunde am meisten Geld eingenommen? Angezeigt werden sollen der «permalink», der Namen des Unternehmens, die durchschnittlichen Einnahmen pro Finanzierungsrunde und die Anzahl Finanzierungsrunden.

6.
Wie viele unterschiedliche Regionen gibt es in der Datenbank?
- Einzureichen sind: vollständiges ER-Diagram, kommentierte SQL-Anfragen für das Befüllen der DB (oder alternativ ein Python-Programm oder ein Jupyter Notebook) und für die Beantwortung der Fragen, ScreenCast über das Befüllen der DB und Ausführung aller SQL-Anfragen.
o In den Screencasts ist der Aufruf der Abfrage im DB-Browser zu zeigen, das Resultat der Abfrage (alle Spalten), sowie die Anzahl zurückgelieferter Datensätze.
- Bewertung:
o Korrektes Schema: 4 Punkte
o Korrekte Datenbefüllung und Abfragen: 4 Punkte
Berner Fachhochschule Bachelor Wirtschaftsinformatik (BWI)
Wirtschaft Modul Datenmanagement & Datenanalyse (WDDA)

Auftrag, Teil (b), 2 Punkte:

Im Teil b) soll von python aus auf die in Teil a) erstellte und gefüllte Datenbank zugegriffen werden. Die Datenbank wird lediglich mittels SELECT Statements gelesen. Es sollen die Anfragen 2 und 6 aus Teil a) programmiert werden. Für jede Anfrage sollte eine Python-Methode erstellt werden. Die Rückgaben (Returns) der Methoden sollen ausgedruckt werden. Nachfolgend wird gezeigt, wie die Methoden aufgerufen und ihre Rückgaben ausgegeben werden sollen. Das folgende Beispiel ist in Jupyter Notebook implementiert. Es ist jedoch optional, einen der Python-Editoren (z. B. Pycharm oder Visual Studio Code) zu verwenden.
Und der obige Code liefert die folgende Ausgabe:
Die beiden Methoden, die die SELECT-Abfragen enthalten, müssen implementiert werden. Bitte achten Sie darauf, dass die Methode der Abfrage 2 eine Eingabe vom Benutzer ("amount") erhält und diese beim Aufruf der SELECT-Abfrage verwendet wird.
Deliverables:
- Kommentiertes Python-Script; bitte Style Guide beachten (https://www.python.org/dev/peps/pep-0008 )
- Verbal kommentierter ScreenCast (<60 sec!) über die Ausführung des Python-Programms. Es muss jeweils die Ausführung des Programms inkl. der Ausgabe zu sehen sein, sowie eine fachlich angemessene Erläuterung des Python Codes. Das Kamerabild des Sprechers/der Sprecherin (oder auch der ganzen Gruppe) muss während der Aufzeichnung eingeschaltet sein. Eine Demo aus einem anderen Kurs steht zur Orientierung auf Moodle.
Bewertung:
- Bis zu 1,5 Punkten für funktionierendes Programm laut o.g. Anforderung
- 0.5 Punkte für Einhaltung der Code Conventions und gute (knappe) Kommentierung
