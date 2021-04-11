# P2_Konrath_Kevin
Projet n°2 Openclassrooms les bases de Python - BS4

$ pip install -r requirements.txt


Tous les fichiers générés sont déposés dans un dossier ./exports/ à la racine du projet. 
Si le dossier 'exports' n'exsiste pas, il sera créé lors du lancement d'une commande.  

## Récupérer les infos d'un livre
$ python3 getBookInfo.py [url_du_livre] [nom_d_une_catégorie]

exemple:

$ python3 getBookInfo.py http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html Test






## Récupérer les infos d'une catégorie complète 
$ python3 getCategoryInfo.py [url_de_categorie]

exemple:

$ python3 getCategoryInfo.py http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html




## Récupérer les infos de toutes les catégories
$ python3 getAllCategoryInfo.py 
