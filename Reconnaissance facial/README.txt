1- Les deux fichier servent pour le detect-humains.py et il filtre une banque de [photos] pour se filtrer dans 	[humains]
	[] = folder.name

	- res10_300x300_ssd_iter_140000 
	- deploy

2- filtrer d'avantage les images [humains] tu peux filtrer les images ayant du textes ex : screenshot, snapchat, modified images...

	tu dois telecharger tesseract [https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0]
	PS : Reduit le url si version ulterieur pour la recherche

 assure toi qu'il est ben telecharger et dans filtrer-humains.py modifie le path du tesseract.exe au besoin.

final :  dans tous les cas ouvre le terminal dans le folder du projet pout lancer les fichier py.

python filtrer-humains.py
python detect-humains.py
