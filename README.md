# Ievads
Pandēmijas sākumā ļoti daudz cilvēku steigā meklēja ko iesākt garajās stundās, kuras pavadītas mājās. Viena no šādām sfērām bija virtuālās sacīkstes. Kaut arī šajā nozarē darbojos kā organizators jau pirms pandēmijas, tieši tās laikā sāku to darīt profsionāli. Darbojoties studijā viena no lielākajām problēmām bija rezultātu parādīšana pēc sacīkstēm tiešraidē, ko tajā laikā veicām vienkārši rādot rezultātu lapu. Labāku veidu nevarējām izdomāt, jo gatavu risinājumu tajā laikā nebija, un paši neko nemācējām. Priekšmeta iedvesmots sāku pētīt vai ir kādi veidi kā šo situāciju labot. Pēc "web-scraping" apgūšanas kursa laikā sāku spēlēties ar rezultātu iegūšanu caur to, bet tad atklāju, ka servera vadības sistēmai ir API, tad nu apguvu kā apieties ar API un visu ar to saistīto. Tā arī radās šis skripts.
## Mērķi
- Iegūt rezultātu sarakstu no [API](https://wiki.emperorservers.com/assetto-corsa-server-manager/web-api).
- Iegūt jaunākās sacīkstes rezultāta failu.
- Apstrādāt to, un izvadīt sacensību rezultātu izvēlētajā straumēšanas programmā.
## Izmantotie moduļi
- Requests - izmantots priekš API, lai iegūtu attiecīgos failus. Iebūvēts Python, nav vajadzīga instalācija. 
- Regular expression (re) - Lietots konkrētu datu meklēšanai "string" mainīgajos. Iebūvēts Python, nav vajadzīga instalācija.
- datetime - Modulis izmantots, lai pārveidotu API doto laiku milisekundēs uz mm:ss.SSS formātu.
## Sekcijas



## Jaunas tēmas
Jaunas tēmas, par kurām iemācījos šajā darbā:
- Kā strādāt ar vienkāršiem API. Nojausma par API man jau bija, bet nebiju strādājis at tiem. Viss izrādījās vienkāršāk, kā domāju
- pareiza *string* mainīgo sastādīšana no *substring* vai citiem mainīgajiem. Iepriekš izmantoju *str(a + "." + b)*
- *datetime* modulis. Iepriekš tādu neesmu lietojis, tas palīdzēja vienkāršot procesu. 