# Jegyzetek a régi logok migrációjához
### Ami eszembe jut, de nem tudom rögtön lekódolni (később törölhető)

- Jó lenne a gzip-be csomagolt fájlokat folyamatosan olvasni, nem egyenként, így lenne lehetőség az új neveknek megfelelő fájlok előállítására (facility_yyyymmdd.gz helyett facility_yyyyww esetleg gzippel csomagolva, ahol yyyy=évszám, mm=hónap, dd=nap, ww=hét sorszáma - utóbbit a unix time alapján kell előállítani)
- időpontok kiegészítése/javítása nagyon fontos lenne, a módja elég szerteágazó és a fenti olvasási móddal nem is fér össze. A bejegyzések elejére be kell szúrni az 1970 óta eltelt másodpercek számát (unix timestamp), ami a bejegyzés valós idejét tartalmazná. Akkor is, ha az 'May  5' lenne, ami az esetek nagy részében nem valódi májust jelöl, hanem a router rebootját.
