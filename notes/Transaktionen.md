# Transaktionen

## Definitionen

### Aktionen und Transaktionen

Eine **Aktion** auf einer Datenbank kann entweder $\mathrm{read}_i(X)$ oder $\mathrm{write}_i(X)$ sein. 
Wir schreiben als Kurzform auch $\mathrm{r}_i(X)$ und $\mathrm{w}_i(X)$. 
Dabei gibt $i$ an, zu welcher Transaktion eine Aktion gehört und $X$ ist das Datenbankobjekt, das gelesen oder geschrieben wird.
Eine **Transaktion** ist eine Folge von Aktionen, die eine Datenbank von einem konsistenten Zustand in einen anderen konsistenten Zustand überführt.


### ACID-Eigenschaften von Transaktionen

- **Atomicity/Atomarität:** Eine Transaktion wird ganz oder garnicht ausgeführt.
- **Consistency/Konsistenz:** Eine DB ist nach einer Transaktion in einem konsistenten Zustand, wenn sie es davor auch war.
- **Isolation:** Eine Transaktion hat den Eindruck, alleine auf der DB zu arbeiten.
- **Durability/Dauerhaftigkeit:** Die Ergebnisse einer Transaktion sollen nicht nur temporär gespeichert werden.


### Konflikte

Ein Konflikt entsteht, falls zwei Aktionen aus verschiedenen Transaktionen ($\mathrm{I}$) das selbe Datenbankelement $X$ betreffen und ($\mathrm{II}$) mindestens eine der Aktionen $\mathrm{write}(X)$ ist.
Für zwei verschiedene Transaktionen $T_i$, $T_j$ und ein Datenbankelement $X$ stehen die Aktionen
- $\mathrm{w}_i(X)$ und $\mathrm{r}_j(X)$
- $\mathrm{w}_i(X)$ und $\mathrm{w}_j(X)$

in Konflikt.


### Schedules

Eine **Schedule** einer Menge von Transaktionen definierte eine Reihenfolge, in der die Aktionen der Transaktionen ausgeführt werden.
Dabei müssen alle Aktionen der Transaktionen in der Schedule enthalten sein und die Reihenfolge von Aktionen innerhalb der Transaktion muss mit der Reihenfolge der Aktionen in der Schedule übereinstimmen

#### Seriell/serialisierbar

Wir nennen eine Schedule **seriell**, wenn alle Transaktionen in der Schedule hintereinander ausgeführt werden.

Eine Schedule ist **serialisierbar**, wenn deren Effekt identisch zum Effekt einer seriellen Schedule ist.

#### Konfliktäquivalenz/Konfliktserialisierbarkeit

Zwei Schedules heißen *konfliktäquivalent*, wenn die Reihenfolge aller Paare von konfligierenden Aktionen in beiden Schedules gleich ist.

Ein Schedule ist *konfliktserialisierbar*, wenn er konfliktäquivalent zu einem seriellen Schedule ist.

Alle konfliktserialisierbaren Schedules sind auch serialisierbar. Nicht alle serialisierbaren Schedules sind auch konfliktserialisierbar.

---

## Mögliche Probleme bei serieller Ausführung mehrerer Transaktionen

#### Dirty Read

Eine Transaktion $T_2$ liest den Wert eines Datenbankobjekts $X$, der von einer anderen Transaktion $T_1$ geschrieben, aber nicht committed wurde.
Problem: Es kann sein, dass $T_1$ noch abgebrochen wird, wodurch $T_2$ einen falschen Wert von $X$ gelesen hätte.

| $T_1$ | $T_2$ |
| :---: |:---:|
| $\mathrm{r}_1(X)$ | |
| $\mathrm{w}_1(X)$ | |
| | $\mathrm{r}_2(X)$ |
| | $\mathrm{w}_2(X)$ |
| | $\verb\|commit\|$ |
| $\verb\|abort\|$ | |
  
#### Non-repeatable Read

Es existieren verschiedene Versionen des non-repeatable read in der Literatur. 
Aus diesem Grund unterscheiden wir nun zwischen zwei Fällen.
- non-repeatable read
- inconsistent read

Ein **non-repeatable read** tritt auf, wenn ein Wert während einer Transaktion zwei mal gelesen wird und sich die Werte unterscheiden.
Hier liest $T_1$ $X$ mehrfach und bekommt unterschiedliche Werte dafür zurück.

| $T_1$ | $T_2$ |
| :---: |:---:|
| $\mathrm{r}_1(X)$ | |
| | $\mathrm{w}_2(X)$ |
| | $\verb\|commit\|$ |
| $\mathrm{r}_1(X)$ | |
| $\verb\|commit\|$ | |

Ein **inconsitent read** tritt auf, wenn sich, nach dem ein Wert gelesen wurde, eine andere Transaktion diesen Wert ändert (und mit $\verb|commit|$ schreibt).
Zu dem Zeitpunkt, an dem $T_1$ mit $\verb|commit|$ beendet wird, stimmt der Wert, den $T_1$ für $X$ gelesen hat, schon nicht mehr.

| $T_1$ | $T_2$ |
| :---: |:---:|
| $\mathrm{r}_1(X)$ | |
| | $\mathrm{w}_2(X)$ |
| | $\verb\|commit\|$ |
| $\verb\|commit\|$ | |

#### Lost Update

Beim lost update Problem überschreibt eine Transaktion die Änderung einer anderen Transaktion, ohne die überschriebene Änderung zu berücksichtigen.

| $T_1$ | $T_2$ |
| :---: |:---:|
| $\mathrm{r}_1(X)$ | |
| | $\mathrm{r}_2(X)$ |
| $\mathrm{w}_1(X)$ | |
| | $\mathrm{w}_2(X)$ |
| | $\verb\|commit\|$ |
| $\verb\|commit\|$ | |

#### Phantom Problem

Während einer Transaktion, die sich auf mehrere Werte mit einer bestimmten Eigenschaft bezieht ($\rightarrow$ SQL), fügt eine andere Transaktion neue Werte in die DB ein, die auch die bestimmte Eigenschaft besitzen.

#### Unterschied zwischen Non-Repeatable Read und Phantom Read

Bei einem non-repeatable read unterscheiden sich die *Werte* der gelesenen Datenbankobjekte, während sich bei einem phantom read die Datenbankobjekte *selber* unterscheiden.

---

## Überprüfung von Konflikt-/Serialisierbarkeit


#### Test auf Serialisierbarkeit

So lange Aktionen, die nicht in Konflikt stehen, tauschen, bis aus einem Schedule ein serieller Schedule wird. 
Falls das klappt, ist der Schedule serialisierbar.



#### Test auf Konfliktserialisierbarkeit

Sei $S$ eine Schedule. Wir definieren $G(S)=\left(V,E\right)$ als *Konfliktgraph* von $S$, wobei
- die Knotenmenge $V$ je einen Knoten pro Transaktion enthält und
- die Kantenmenge $E$ für jedes Paar von konfligierenden Aktionen aus verschiedenen Transaktionen eine gerichtete Kante enthält, wobei die Kantenrichtung der Reihenfolge der Aktionen in $S$ entspricht.

$S$ ist *konfliktserialisierbar* genau dann, wenn $G(S)$ keine Zyklen enthält. Enthält $G$ einen Zyklus, so ist $S$ nicht konfliktserialisierbar und damit auch nicht serialisierbar.



---

## Linksammlung

- [Unterschied non-repeatable read und dirty read](https://stackoverflow.com/questions/18297626/difference-between-non-repeatable-read-vs-dirty-read?noredirect=1&lq=1)
- [Unterscheid non-repeatable read und phantom read](https://stackoverflow.com/questions/11043712/what-is-the-difference-between-non-repeatable-read-and-phantom-read)

