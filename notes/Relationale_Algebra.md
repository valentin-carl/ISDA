# Relationale Algebra

## Grundidee

Datenbanken haben im Alltag eines Informatikers zwei Funktionen: Zunächst sind sie der Ort, wo (große) Datenmengen gespeichert werden. Das Speichern der Daten ist nur dann sinnvoll, wenn es eine Möglichkeit gibt, um aus der Datenbank Informationen zu extrahieren. Dies ist die zweite Funktion. In der Praxis gibt es dafür Datenbankabfragesprachen wie SQL (nächstes Thema der Vorlesung). Das theoretische Fundament für solche Datenbankabfragesprachen ist die relationale Algebra.

Um ein intuitives Verständnis davon zu entwickeln, was relationale Agebra ist, ist es sinnvoll, sich Relationen und Algebren im Allgemeinen anzuschauen.

## Was sind Relationen?

> Das Folgende ist angelehnt an *Wagner, K. (2003) Theoretische Informatik – Eine kompakte Einführung. S. 7/8*.

### Tupel

Für normale Mengen ist die Reihenfolge egal. So gilt zum Beispiel die folgende Gleichung.

<img src="equations/RelationaleAlgebra/Reihenfolge.png" height="25">

Soll jetzt bei einer endlichen Menge die Reihenfolge eine Rolle spielen, sprechen wir von **n-Tupeln**, wobei *n* die Größe der Menge ist. So wird aus der vorherigen Gleichung nun eine Ungleichung.

<img src="equations/RelationaleAlgebra/Tupel.png" height="25">

### Kartesisches Produkt zweier Mengen

Ausgehend von den beiden Mengen *A* und *B*,

<img src="equations/RelationaleAlgebra/MengeA.png" height="25">

<img src="equations/RelationaleAlgebra/MengeB.png" height="25">

definieren wir das **kartesische Produkt** wie folgt.

<img src="equations/RelationaleAlgebra/kP.png" height="25">

Somit ist das kartesische Produkt

<img src="equations/RelationaleAlgebra/kartesischesProdukt.png" height="25">

*Hinweis:* Manchmal wird stattdessen auch vom **Kreuzprodukt** gesprochen, gemeint ist aber das gleiche.

### Relationen

Jetzt nennen wir die Menge *R* mit 

<img src="equations/RelationaleAlgebra/Relation.png" height="25">

eine Relation über *A* und *B*.

> Denjenigen, für die Relationen ein neues Konzept sind, empfehle ich, [hier](https://link.springer.com/content/pdf/10.1007/978-3-642-55452-0.pdf) die Seiten 5 bis 9 als kurze Einführung zu lesen; allen an Relationen Interessierten kann ich [hier](https://link.springer.com/content/pdf/10.1007%2F978-3-642-56792-6.pdf) das erste Kapitel für eine ausführlichere Erklärung empfehlen.

## Was ist eine Algebra?



## Relationale Algebra


---

## Literaturhinweise


