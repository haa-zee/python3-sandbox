# Jegyzetek a régi logok migrációjához
### Ami eszembe jut, de nem tudom rögtön lekódolni (később törölhető)

- Jó lenne a gzip-be csomagolt fájlokat folyamatosan olvasni, nem egyenként, így lenne lehetőség az új neveknek megfelelő fájlok előállítására (facility_yyyymmdd.gz helyett facility_yyyyww esetleg gzippel csomagolva, ahol yyyy=évszám, mm=hónap, dd=nap, ww=hét sorszáma - utóbbit a unix time alapján kell előállítani)
- időpontok kiegészítése/javítása nagyon fontos lenne, a módja elég szerteágazó és a fenti olvasási móddal nem is fér össze. A bejegyzések elejére be kell szúrni az 1970 óta eltelt másodpercek számát (unix timestamp), ami a bejegyzés valós idejét tartalmazná. Akkor is, ha az 'May  5' lenne, ami az esetek nagy részében nem valódi májust jelöl, hanem a router rebootját.
  - Amikor a log utolsó sorai May  5 dátumúak, akkor az egyetlen támpont a becsomagolt fájl utolsó módosításának dátuma, ezt a GzipFile.mtime tartalmazza. A valós időt ebből kell majd visszaszámolni
  - Ha eltérő dátumú bejegyzések közé kerül May  5, akkor az első korrekt időpontot tartalmazó sor időpontja-1mp-től kell indulni a visszaszámolással, ami csak közelítő érték, de remélhetőleg nincs jelentősége. ( **annyira közelítő, hogy ha nem a kern-\* logokat veszem alapul, akkor akár több napos csúszás is összejöhet!!** )
  - A valóban májusi fájlokkal egyelőre nem tudom, mit lehet kezdeni, mert van rá példa, hogy májusi log, amiben valós Május 5. szerepel, tartalmaz reboot miatt keletkezett May  5 kezdetű bejegyzést is...
  - Muszáj ragaszkodnom ahhoz, hogy router reboot=May  5 időpont, mert a logokban található nagyobb kihagyások vagy negatív változások lehetnek azért, mert eleve ritkán íródik a log vagy épp a téli-nyári időszámítás váltása miatt
