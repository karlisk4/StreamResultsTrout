# Ievads
Pandēmijas sākumā ļoti daudz cilvēku steigā meklēja ko iesākt garajās stundās, kuras pavadītas mājās. Viena no šādām sfērām bija virtuālās sacīkstes. Kaut arī šajā nozarē darbojos kā organizators jau pirms pandēmijas, tieši tās laikā sāku to darīt profsionāli. Darbojoties studijā viena no lielākajām problēmām bija rezultātu parādīšana pēc sacīkstēm tiešraidē, ko tajā laikā veicām vienkārši rādot rezultātu lapu. Labāku veidu nevarējām izdomāt, jo gatavu risinājumu tajā laikā nebija, un paši neko nemācējām. Priekšmeta iedvesmots sāku pētīt vai ir kādi veidi kā šo situāciju labot. Pēc "web-scraping" apgūšanas kursa laikā sāku spēlēties ar rezultātu iegūšanu caur to, bet tad atklāju, ka servera vadības sistēmai ir API, tad nu apguvu kā apieties ar API un visu ar to saistīto. Tā arī radās šis skripts. Darbā tiek izmantots Assetto Corsa autosporta simulatora [ACSM sistēmas]() API.
## Mērķi
- Iegūt rezultātu sarakstu no [API](https://wiki.emperorservers.com/assetto-corsa-server-manager/web-api).
- Iegūt jaunākās sacīkstes rezultāta failu.
- Apstrādāt to, un izvadīt sacensību rezultātu izvēlētajā straumēšanas programmā.
## Izmantotie moduļi
- [Requests]() - izmantots priekš API, lai iegūtu attiecīgos failus. Iebūvēts Python, nav vajadzīga instalācija. 
- [Regular expression (re)]() - Lietots konkrētu datu meklēšanai "string" mainīgajos. Iebūvēts Python, nav vajadzīga instalācija.
- [datetime]() - Modulis izmantots, lai pārveidotu API doto laiku milisekundēs uz mm:ss.SSS formātu.
## Sekcijas
### Json iegūšana
Šajā sekcijā vispirms no ACSM API iegūst sesiju sarakstu,  izmantojot sekojošos parametrus:
- *q=RACE*, kas atlasa tikai sacīkstes sesijas.
- *sort-date*, kas rezultātus sakārto pēc datuma.
- *server=0*, kas izvēlās konkrēto serveri.
- *page=0*, kas atlasa lapu, lai samazinātu datu skaitu (sistēma sakārto failus grupās pa 20, lai tos parādītu [lapā]())

Tad ar *re* iegūst pirmo rezultātu, kas arī būs jaunakais rezultāts. Atkal izmantojot requests iegūst sacensību rezultātu faila objektu, kuru pārveido bibleotēkas formātā, lai varētu piekļūt JSON faila sekcijām.

Izveidots cilks, kurā apstrādā bibliotēkas "Results" sekcijas vienumus. Tajā braucēji atrodas finiša rezultātu kārtībā, tādēļ tālāka kārtošana nav vajadzīga.
### Braucēju vārdi
Šajā sekcijā iegūst katra vienuma parametru "DriverName", jeb braucēja vārdu un pievieno to sarakstam.
###  kvalifikācijas dati
Šajā sekcijā iegūst braucēja sacīkstes sākšanas pozīciju un salīdzina to ar beigu pozīciju, kas ir braucēja pozīciju kritums vai kāpums sacīkstes laikā.
### atrākais aplis
Šajā sekcijā iegūst braucēja ātrāko apļalaiku milisekundēs un pārveido to lasāmā formātā. Tā, kā šajā pielietojumā apļa laiki neilgs vairāk par viencipara minūšu skaitu, tad tiek noņemtas stundas un divcipara minūšu cipari, kā arī pēdējie 3 milisekunžu cipari
### finiša atstums no līdera
Šajā sekcijā vispirms tiek saskaitīts cik apļus veicis dalībnieks meklējot vārdu JSON faila "Laps" sekcijā. Pēc nelielas apskates atklāju, ka šim parametram bija jābūt "Results" sekcijā, par ko noziņoju platformas veidotājiem, [kuri to izskatīs](https://imgur.com/a/R3JWSQ9).

Atpakaļ pie tēmas, tālāk ir *if*, kurā:
- pārbauda vai tā ir pirmā pozīcija, kuras gadījumā atstatuma vietā ieliek kopējo apļu skaitu.
- Ja dalībnieks ir tajā pašā aplī kā līderis, tad finiša laiks tiek norādīts kā atstatums.
- Ja dalībnieks ir veicis mazāk apļus kā līderis, tad tiek parādīts zaudētais apļu skaits.
### gala sarakstu veidošana
Tiek izveidots saraksts, kurā tiek pievienota starta un finiša pozīciju atšķirība, ātrākais apļalaiks, un atstatums no līdera.
### teksta failu izveide
Tiek izveidoti teksta faili, kur vienā ir braucēju vārdi un pozīcija, otrā pārējie dati. Tie ir nodalīti, jo pozīciju un vārdu sarakstu var vajadzēt lietot atsevišķi. Tālāk šos failus var pievienot strumēšanas programmai kā teksta avotu, ka var automātiski atjaunoties.
## Jaunas tēmas
Jaunas tēmas, par kurām iemācījos šajā darbā:
- Kā strādāt ar vienkāršiem API. Nojausma par API man jau bija, bet nebiju strādājis at tiem. Viss izrādījās vienkāršāk, kā domāju
- moderna *string* mainīgo sastādīšana no *substring* vai citiem mainīgajiem izmantojot [*format*](). Iepriekš izmantoju *str(a + "." + b)*
- *datetime* modulis. Iepriekš tādu neesmu lietojis, tas palīdzēja vienkāršot procesu. 