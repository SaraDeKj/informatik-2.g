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

- puls styrer fart på dronen  
- tegnsprogs styring
- hoved styrringm. motiondetector.
- danse måtte
- puppeteer  

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
![image](https://github.com/SaraDeKj/informatik-2.g/blob/a87fe1e2282e2c179d0e0c0bdc01250b84262fc8/drone%20flowchart%201.pdf)


