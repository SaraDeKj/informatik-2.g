# Informatik notesbog 
## Kapitel 1. 
### Tello dronen
__3 lags modellen__  
- _Præsentation_  
  Appen til dronen (både grafik og klik fra brugeren)  
  knapper på dronen fx. tænd og sluk.  
  censorer (kamera)
   
- _Logik_  
  Beregner længde fra forskelige ting ud fra input kemera  
  bergner fart osv ud fra input fra app  
  Tager kode fra datalaget for at flyve
  
- _Data_  
  Kode der beskriver hvordan den flyver

## Logbog:
### 16.08-2024
Vi har leget med dronen idag og lavet et script der kan få dronen til at flyve i en firkant og lave flips. Filnavn 

### 26.08-24
fokus på innovation.  
idegenerering til styring af stello drone.

- puls styrer fart på dronen. Jo hurtigere puls, jo hurtigere kører dronen, evt. noget der kan måle pulsen, en måde at dreje dronen på??
- tegnsprogs styring. Effekter ved hjælp af motiondetector måske? Reagere på Hænderne, evt. AI
- hoved styrringm. motiondetector. Brug af et motionsensor, hvor dronen følger hovedets bevægelser, hvis muligt. Dronen flyver evt. i den retning brugeren kigger.
- danse måtte. Ligesom de der spil, hvor der hvor man træder er højre, venstre, lige ud osv. Evt. AI?
- Puppeteer: En puppeteer kontrollere hvor dronen styres gennem bevægelser igennem tråde som i en dukke. En tiltswitch eller anden sensor fastgjort til snorene bruges til at registrere vejene snorene drejes, hælder osv, til at sende videre bevægelserne til hvor dronen så gå

vi vælger at lave puppeteer. Denne ide er radikal på positions området i de 4 p'er model.
Fordi Vi bruger allerede existerende teknologi på et andet område som det er ikke er blevet brugt på før.


Vi har valgt, at bruge en tiltswitch, eller vi vil teste, om den kan sættes fast med en snor, hvor man kan "lege" puppeteer med den, og om den kan reagere til inputsne fra hvordan man kontrollere snorene

Krav til Systemet:

Tiltswitches, der registerer bevægelsen af snorene, hvilken retning osv.
Arduino, der behandler dataene fra tiltswitchene og giver det videre til TELLO dronen
Kommandoer til TELLO dronen via en computer, eller andet
Evt. mulighed for en visuel feedback, så brugeren ved hvordan bevægelserne påvirker dronen

Blokdiagram:
![image](https://github.com/user-attachments/assets/02548c5d-0ed8-4f24-8d31-f9e2266ccc8b)

Flowchart: 
(bemærk at vi ikke har fundet en måde at lande dronen på endu)
![drone flowchart image](https://github.com/user-attachments/assets/9b1fab64-d9b9-4d64-8787-4a6a89a49e5c)

 ### 12.09-24
 Vi har lavet et trello board   
 https://trello.com/b/MWbsBEyX/informatik    
 Til vores styrring bruger vi Grove axel 6 til at måle hvilke veje vi tilter styrings boarded. Vi bruger et axelerometer da vi gerne vil kunne måle præcis hvilke veje, altså højrevenstre frem eller tilbage, som vi vipper boardet.   
 Vi bruger denne tutorial til data fra axelerometeret   
 https://wiki.seeedstudio.com/Grove-6-Axis_Accelerometer&Gyroscope_BMI088/ 

 ved at have stikket til højre gælder følgende vip.   
højre under -300 i 2. koordinat   
venstre over +300 i 2. koordinat   
lige ud uner -300 i 1. koordinat   
bagud over +300 i 1. kopordinat   

### 03.10-24
Vi har lavet en prototype og en bruger test ifht hvordan brugeren vil bruge vores controller
Det gjorde vi med et papir kryds der simulerer marionetdukke håndtaget som er vores inspiration



