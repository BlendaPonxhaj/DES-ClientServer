# DES-ClientServer

 DES-ClientServer është një mënyrë komunikimi ku përdoret algoritmi Data Encryption Standard (DES) për të mbrojtur të dhënat që shkëmbehen midis klientit dhe serverit. Në këtë model, informacioni enkriptohet me 
një çelës të përbashkët para se të dërgohet dhe më pas dekriptohet nga pala tjetër, duke parandaluar qasjen e paautorizuar gjatë transmetimit. Serveri i përpunon të dhënat pasi i dekripton dhe mund të kthejë 
përgjigje gjithashtu të enkriptuara. Megjithatë, për shkak të sigurisë së kufizuar të DES, ai sot përdoret më pak dhe shpesh zëvendësohet me algoritme më të avancuara si AES.

Projekti demonstron mënyrën se si realizohet komunikimi i sigurt në rrjet përmes socket-eve, ku mesazhet fillimisht kalojnë në procesin e enkriptimit para transmetimit. Klienti dërgon kërkesa të enkriptuara te serveri, ndërsa serveri i pranon, i dekripton dhe sipas kërkesës kthen përgjigje ose mesazhin e pranuar. Ky implementim shërben si shembull praktik për përdorimin e kriptografisë simetrike në aplikacione klient/server dhe për të kuptuar bazat e sigurisë së komunikimit në rrjet.

# Enkriptimi dhe Dekriptimi i Mesazheve në Python përmes DES

Ky projekt është realizuar nga studentë të vitit të dytë të Universitetit "Hasan Prishtina" – Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike, në kuadër të lëndës **Data Security**.

## Përshkrimi i Projektit

DES-ClientServer është një mënyrë komunikimi ku përdoret algoritmi **Data Encryption Standard (DES)** për të mbrojtur të dhënat që shkëmbehen midis klientit dhe serverit. Në këtë model, informacioni enkriptohet me një çelës të përbashkët para se të dërgohet dhe më pas dekriptohet nga pala tjetër, duke parandaluar qasjen e paautorizuar gjatë transmetimit.

Serveri i përpunon të dhënat pasi i dekripton dhe mund të kthejë përgjigje gjithashtu të enkriptuara. Megjithatë, për shkak të sigurisë së kufizuar të DES, ai sot përdoret më pak dhe shpesh zëvendësohet me algoritme më të avancuara si **AES**.

Projekti demonstron mënyrën se si realizohet komunikimi i sigurt në rrjet përmes socket-eve, ku mesazhet fillimisht kalojnë në procesin e enkriptimit para transmetimit. Klienti dërgon kërkesa të enkriptuara te serveri, ndërsa serveri i pranon, i dekripton dhe sipas kërkesës kthen përgjigje ose mesazhin e pranuar.

Ky implementim shërben si shembull praktik për përdorimin e kriptografisë simetrike në aplikacione klient/server dhe për të kuptuar bazat e sigurisë së komunikimit në rrjet.

## Struktura e Projektit

Projekti përfshin dy skripta Python:

- `server.py` – skripta që ekzekuton serverin. Ai pranon lidhje nga klientët, dekripton mesazhet që merr dhe dërgon përgjigje të enkriptuara.
- `client.py` – skripta që ekzekuton klientin. Përdoruesi shkruan një mesazh, ai enkriptohet dhe dërgohet te serveri, ndërsa përgjigjja e serverit dekriptohet dhe shfaqet në ekran.

## Si të përdoret projekti

Për të përdorur këtë projekt, duhet të keni Python dhe libraritë e nevojshme të instaluara në sistemin tuaj.

1. Sigurohuni që keni të instaluar Python.
2. Instaloni librarinë e nevojshme me komandën:
pip install pyDes
3. Ruani kodin e klientit në një fajll me emrin `client.py`.
4. Ruani kodin e serverit në një fajll me emrin `server.py`.
5. Ekzekutoni serverin me komandën:
python server.py
6. Në një terminal tjetër, ekzekutoni klientin me komandën:
python client.py

## Rezultatet e Pritshme

Gjatë ekzekutimit të projektit pritet që:

- Klienti të fillojë dhe të shkruajë një mesazh.
- Mesazhi i klientit të enkriptohet duke përdorur çelësin e paracaktuar DES.
- Mesazhi i enkriptuar të dërgohet në server.
- Serveri ta marrë mesazhin dhe ta dekriptojë duke përdorur të njëjtin çelës.
- Serveri të dërgojë një prompt të enkriptuar tek klienti.
- Klienti ta dekriptojë prompt-in, të japë një përgjigje dhe ta enkriptojë përsëri.
- Serveri, në bazë të përgjigjes së përdoruesit, të kthejë mesazhin e pranuar ose një mesazh tjetër si përgjigje.

## Qëllimi i Projektit

Qëllimi i këtij projekti është të tregojë në mënyrë praktike:

- përdorimin e algoritmit DES për enkriptim dhe dekriptim,
- komunikimin klient/server përmes socket-eve,
- transmetimin e sigurt të të dhënave në rrjet,
- dhe zbatimin e kriptografisë simetrike në Python.
