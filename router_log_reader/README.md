#Log reader/analyzer - again... :(

Naszóval, újra nekikezdek a dolognak, hátha most sem lesz belőle semmi. :)

Logokat akarok elemezgetni, pusztán hobbiból, gyakorlati értelme nagyjából nulla.

Az első feladvány az Asus router (asuswrt, merlin, tomato firmware-ek) logjának
feldolgozása, kigyűjtve belőle, hogy 
- mennyi port scant találok, milyen IP-kről
- mennyi csomagot dobott el a packet filter óránként, az épp érvényes IP címen
(szóval ha változik a WAN címem, akkor folytassa nulláról a számolást)
- kiszűrni a logokból a rendszeresen előforduló, érdektelen sorokat és listázni
azokat, amelyek érdekesek lehetnek, mert valami viszonylag ritka eseményt jeleznek.

Mindezt lehetőleg úgy, hogy az eredmény egy XML/YAML/JSON fájl vagy string legyen.
A fentiek shell+perl szkriptek formájában már megvannak, az algoritmusok egy részét
azokból is ki lehet gyűjteni.

Viszont jó lenne mindezt legalább OOP-re emlékeztető formában, újrahasznosíthatóan
megírni.
Parancssori kapcsoló mondja meg, hogy melyik funkciót kell megvalósítani,
.ini fájl tartalmazza a logok helyét, esetleg a nevek specifikációját is. 
(teszemazt, a kernel logok a kern, kern-yyyymmdd, kern-yyyymmdd.gz fájlokban vannak,
a daemon logok ugyanígy, csak daemon* néven stb.)

**TODO:** Amin el kéne gondolkodni: közös olvasó kód, elő- illetve utófeldolgozással,
közben meg filter jelleggel az elvárt működésnek megfelelő funkciókat futtatva?
Vagy legyen teljesen önálló az összes feladat kódja, csak a közös funkciók
kerüljenek közösen elérhető függvényekbe?
