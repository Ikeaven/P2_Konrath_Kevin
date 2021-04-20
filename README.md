# P2_Konrath_Kevin
Projet n°2 Openclassrooms les bases de Python - BS4


## initialisation du projet : 

Dans un terminal ou invite de commande executez les commandes suivantes : 
Naviguez vers le repertoire souhaité, à l'aide de cd / ls 


### 1. Récupérer le projet
$ git clone https://github.com/Ikeaven/P2_Konrath_Kevin.git


### 2. activer un environnement vituel 
$ cd P2_KONRATH_KEVIN
$ python3 -m venv env 
$ source env/bin/activate 


### 3. installer les dépencances projets 
$ pip install -r requirements.txt


### 4. executer le programme :
$ python3 main_scrapper.py [url]

exemple :

#### Pour récupérer toutes les catégorie :
$ python3 main_scrapper.py https://books.toscrape.com/ 

#### pour récupérer une catégorie, remplacer l'url par l'url d'une catégorie :
$ python3 main_scrapper.py https://books.toscrape.com/catalogue/category/books/travel_2/index.html

#### Pour récupérer un livre remplacer l'url par l'url d'un livre : 
$ python3 main_scrapper.py https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html



