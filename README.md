# Trip planner project (TPP)
 
####### README.md (explain what is your project and how to run it, what were the issues, what are the key results, ...)
## Description 

TPP est un programme destiné à faciliter la planification de vos vacances. 
Pour votre séjour, si vous devez visiter une ville bien précise ou encore, si vous prévoyez de partir en vacances à un mois bien déterminé ignorant votre destination, TPP peut vous accompagner dans vos prépartions.

Dépendamment de votre cas, il vous permet d'obtenir la meilleure période à visiter une ville ou les meilleures destinations pour un mois donné, les 10 meilleurs endroits à visiter dans la ville selectionnée et les meilleurs restaurants où manger. 

## Utilisation

TPP a été conçu afin de faciliter son utilisation auprès des utilisateurs. A cet effet, l'utilisateur doit suivre les étapes suivantes :

I- Afin de disposer de l'environnement adéquat

   1. Télécharger le fichier Trip-planner-project et l"enregistrer dans un dossier sur son ordinateur
   2. Télécharger Chromedriver.exe et l'enregistrer dans le dossier trip-planner

II- Pour lancer TPP et obtenir les informations souhaitées

   3. Ouvrir le terminal à partir de la fenêtre du dossier trip-planner-project
   4. Entrer la commande qui suit et attendre que tous les packages nécessaires soient installés :
 
    python allpackages.py
    
   5. Entrer la commande ci-après pour lancer le logiciel. Une fenêtre va s'ouvrir pour aider l'utilisateur à choisir ses paramètres (Ville et/ou mois de voyage) : 
        
    python tripPlanner.py

   6. Entrer la commande ci-après pour afficher le dashboard : 
   
    streamlit run dashborad.py

Un fichier excel comportant vos informations est également créé et stocké dans le fichier.

# Le fichier Trip-planner-project
## Composantes
Le fichier téléchargé comporte 11 fichiers python avec une extension (.py). Chacun de ces fichiers est un module contenant une fonction devant permettre l'extraction des différentes informations souhaitées. Nous pouvons citer alphabétiquement : 
    
     1. BestCities.py
     2. BestMonth.py
     3. Dashboard.py
     4. Error.py
     5. Interface.py
     6. Interface_nocity.py
     7. Interface_nomonth.py
     8. Place2visit.py
     9. Restaurants.py
    10. Temp.py
    11. TripPlanner.py
###### 1. BestCities.py
Ce module contient la fonction permettant de déterminer les meilleures destinations pour un mois donné. Grâce à l'outil Selenium, les données sont recueillies sur le site "Où et quand partir" de Ouest France : https://partir.ouest-france.fr/. Son principe de fonctionnement consiste à récupérer et retourner la liste des 10 meilleures destinations à visiter pour le mois choisi.

   **Outils/ Packages** : *Selenium*

###### 2. BestMonth.py
Ce module permet de trouver les meilleurs mois pour visiter une ville déterminée en se basant notamment sur la température durant cette période. La fonction définie permet, grâce aux outils BeautifulSoup et Selenium, de récolter les informations nécessaires sur le site "Où et quand" : https://www.ou-et-quand.net/partir/quand/.
    
   **Outils/ Packages** : *BeautifulSoup, Selenium, time*
   
###### 3. Dashboard.py
Le module Dashboard permet d'afficher les informations enregitrées dans le fichier excel créé à la fin du lancement de TriPlanner. 

   **Outils/ Packages** : *Streamlit, pandas*

###### 4. Error.py
Le module error permet d'afficher un message d'erreur au cas où l'utilisateur oublierait d'insérer une critère de recherche dans la première boite de dialogue qui s'affiche.

   **Outils/ Packages** : *tkinter*

###### 5. Interface.py



###### 6. Interface_nocity.py


###### 7. Interface_nomonth.py


###### 8. Place2visit.py


###### 9. Restaurants.py


###### 10. Temp.py


###### 11. TripPlanner.py


