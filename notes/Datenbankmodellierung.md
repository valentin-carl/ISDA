# Datenbankmodellierung

## Das Entity-Relationship-Modell

Das Entitiy-Relationship-Modell (kurz: ER-Modell) ist das Standardmodell für den Entwurf eines Datenbankschemas.
Das Modell besteht aus Entity-Typen, Relationship-Typen, Attributen und Integritätsbeziehungen.
Dabei sind die *entities* die Objekte, die verschiedene Attribute besitzen, *relationships* beschreiben die Beziehungen zwischen den Objekten und Integritätsbedingungen schränken die Beziehungen zwischen Objekten ein.

---

## Wie erstellt man ein Entity-Relationship-Diagramm?

1. Welche Entity-Typen gibt es?
    * Sonderfall: schwache Entity-Typen

2. Welche Relationship-Typen gibt es?
    * Sonderfälle:
       * mehrere Relationship-Typen zwischen zwei Entity-Typen
       * rekursive Relationship-Typen
       * n-äre Relationship-Typen

3. Welche Attribute haben die Entity- & Relationship-Typen?
    * Für Entity-Typen: Was sind die Schlüssel und müssen ggf. neue hinzugefügt werden?
    * Sonderfälle:
       * komplexe/zusammengesetzte Attribute
       * mengenwertige Attribute
       * abgeleitete Attribute

4. Was sind die Kardinalitäten?

5. Wo soll es Totalitäten geben?
