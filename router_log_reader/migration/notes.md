# Jegyzetek a régi logok migrációjához
### Ami eszembe jut, de nem tudom rögtön lekódolni (később törölhető)

- Jó lenne a gzip-be csomagolt fájlokat folyamatosan olvasni, nem egyenként, így lenne lehetőség az új neveknek megfelelő fájlok előállítására (facility_yyyymmdd.gz helyett facility_yyyyww esetleg gzippel csomagolva, ahol yyyy=évszám, mm=hónap, dd=nap, ww=hét sorszáma - utóbbit a unix time alapján kell előállítani)
- időpontok kiegészítése/javítása nagyon fontos lenne, a módja elég szerteágazó és a fenti olvasási móddal nem is fér össze. A bejegyzések elejére be kell szúrni az 1970 óta eltelt másodpercek számát (unix timestamp), ami a bejegyzés valós idejét tartalmazná. Akkor is, ha az 'May  5' lenne, ami az esetek nagy részében nem valódi májust jelöl, hanem a router rebootját.
  - Amikor a log utolsó sorai May  5 dátumúak, akkor az egyetlen támpont a becsomagolt fájl utolsó módosításának dátuma, ezt a GzipFile.mtime tartalmazza. A valós időt ebből kell majd visszaszámolni
  - Ha eltérő dátumú bejegyzések közé kerül May  5, akkor az első korrekt időpontot tartalmazó sor időpontja-1mp-től kell indulni a visszaszámolással, ami csak közelítő érték, de remélhetőleg nincs jelentősége. ( **annyira közelítő, hogy ha nem a kern-\* logokat veszem alapul, akkor akár több napos csúszás is összejöhet!!** )
  - A valóban májusi fájlokkal egyelőre nem tudom, mit lehet kezdeni, mert van rá példa, hogy májusi log, amiben valós Május 5. szerepel, tartalmaz reboot miatt keletkezett May  5 kezdetű bejegyzést is...
  - Muszáj ragaszkodnom ahhoz, hogy router reboot=May  5 időpont, mert a logokban található nagyobb kihagyások vagy negatív változások lehetnek azért, mert eleve ritkán íródik a log vagy épp a téli-nyári időszámítás váltása miatt
- A logok neve \<facility\>-\<utolso_bejegyzes_datuma\>.gz, ezt két lépcsőben lehet konvertálni az új formára: 
  1. Létrehozni az azonos <facility> alá tartozó fájlokat úgy, hogy az összes tartalmát egyesével konvertálom __és__ javítom, az elejére beírom a unix timestamp-et és append módban írom a javított sorokat a <facility>_<YYYYWW> nevű text file-okba úgy, hogy minden bejegyzés unix timestamp-je alapján a saját időpontjához tartozó fájlba kerüljön.
  Például a 2019 Jan  1 13:44 sor a kernel logból, a kern_201901, a 2019 Dec 31 23:59 kernel logból pedig kern_201952 lesz.
  2. Az elkészült logokat újratömöríteni, de... itt nem elég simán gzip-pel végigmenni rajtuk, mert a fájlok utolsó módosításának
  dátuma meg kellene, hogy egyezzen az utolsó sorban szereplő idővel. Ez azt hiszem, legegyszerűbben az os.utime(???) függvénnyel
  oldható meg: beolvasni a fájlt a memóriába, az utolsó sorból kiszedni a unix timestamp értékét és ezt beállítani az os.utime segítségével,
  majd akár os.system("gzip ...")
  
