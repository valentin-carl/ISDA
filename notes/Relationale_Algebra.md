# Relationale Algebra

## Grundidee

Datenbanken haben im Alltag eines Informatikers zwei Funktionen: Zunächst sind sie der Ort, wo (große) Datenmengen gespeichert werden. Das Speichern der Daten ist nur dann sinnvoll, wenn es eine Möglichkeit gibt, um aus der Datenbank Informationen zu extrahieren. Dies ist die zweite Funktion. In der Praxis gibt es dafür Datenbankabfragesprachen wie SQL (nächstes Thema der Vorlesung). Das theoretische Fundament für solche Datenbankabfragesprachen ist die relationale Algebra.

Um ein intuitives Verständnis davon zu entwickeln, was relationale Agebra ist, ist es sinnvoll, sich Relationen und Algebren im Allgemeinen anzuschauen.

### Was sind Relationen?

#### Karthesisches Produkt zweier Mengen

\begin{equation}
	A \cross B = \{(a,b) \mid a \in A, b \in B\}
\end{equation}

Denjenigen, für die Relationen ein neues Konzept sind, empfehle ich, [hier](https://link.springer.com/content/pdf/10.1007/978-3-642-55452-0.pdf) die Seiten 5 bis 9 als kurze Einführung zu lesen; allen an Relationen Interessierten kann ich [hier](https://link.springer.com/content/pdf/10.1007%2F978-3-642-56792-6.pdf) das erste Kapitel für eine ausführlichere Erklärung empfehlen.

### Was ist eine Algebra?


