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

## Kapitel 2  
### Kryptering 10.01-25  
  
Vi snakker om kryptering.  
![image](https://github.com/user-attachments/assets/537395d1-710a-49c2-8c97-e6a7ef15934a)

 
### Kryptering af beskeder
#### RSA
- Public key
    - Public og sendes us til alle så de kan kryptere information med den og sende den. Kan dekrypteres med modtageren secret key.
- secret key
    - Kun en selv der har den key som bruges til at aflæse beskeder krypteres med ens egen publickey.

Kryptering ved hjælp af primtal  
N= p * q   
hvor p og q er primtal  
For at lave e værdi gør vi følgende  
r=(p-1)*(q-1)  
Vi skal så have et tal der giver 1 mod r som vi kalder k  
Det skal så faktoriseres til to numre som vi kalder d og e, hvor e*d mod r = 1  

nu har vi d, e og N  

- public key
    -(msg)^e Mod N
    - er nu krypteret
- secret key 
    - (chifer)^d Mod N
    - er nu dekrypteret
man kan sende sin public key som andre kan bruge til at kryptere dataen men man er den enste der kan dekryptere den fordi man er den eneste der har sin secret key

### Projekt kryptering
Projektet ligger under denne github:https://github.com/MichaelHNH/SIGINT   

Projektet går ud på at lave et program der kan kryptere og dekryptere beskeder.   
Problem formulering: Hvordan kan vi lave et program der kan sende hemmelige beskeder ved hjælp af lyd.   
![image](https://github.com/user-attachments/assets/ffed0a42-5872-4132-9455-3c0f9253a31c)


### Cybermesterskaberne
#### AES encryptioner
[<img src="https://github.com/user-attachments/assets/aee76d11-4729-4d20-921c-aaf1cd96127f" width="400"/>](https://github.com/user-attachments/assets/aee76d11-4729-4d20-921c-aaf1cd96127f)

Jeg bruger en AES decrypter online og indsæter information fra siden   
[<img src="https://github.com/user-attachments/assets/fcbecfbb-cbb4-48e1-8e9d-e81f82671f50" width="400"/>](https://github.com/user-attachments/assets/fcbecfbb-cbb4-48e1-8e9d-e81f82671f50)

Jeg får denne key: DDC{S3cr3t_C0d3}  

### Cyber security Webstuff 27/03/2025
Begreber:   
* bug-bounty
* sårbarheder
* CVE liste
  *   https://www.cve.org/   

Vi leger med terminalen på vores computer og internet.
* curl
  * Viser rå data fra en webserver
* nmap
  * Viser åbne porte til en bestemt IP
* ncat
  * Forbindelse mellem computere der sender rå data, plane tekst.
  * den ene åbner bestemt port på samme netværk den anden forbinder til port med port nummer og ip på netværk.
  * ![image](https://github.com/user-attachments/assets/e4f931dd-9f83-49f0-bb5f-a27b57079242)

### sql injection

En del af brugernavnt indeholder sql som computeren så kører

