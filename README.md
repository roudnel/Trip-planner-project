# Trip planner project (TPP)
 
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
        
    python TripPlanner.py

   6. Entrer la commande ci-après pour afficher le dashboard : 
   
    streamlit run dashboard.py

Un fichier excel comportant vos informations est également créé et stocké dans le fichier.

# Le fichier Trip-planner-project
## Composantes
Le fichier téléchargé comporte 12 fichiers python avec une extension (.py). Chacun de ces fichiers est un module contenant une fonction devant permettre l'extraction des différentes informations souhaitées. Nous pouvons citer alphabétiquement : 
    
     1. allpackages.py
     2. BestCities.py
     3. BestMonth.py
     4. Dashboard.py
     5. Error.py
     6. Interface.py
     7. Interface_nocity.py
     8. Interface_nomonth.py
     9. Place2visit.py
    10. Restaurants.py
    11. Temp.py
    12. TripPlanner.py

#### 1. allpackages.py
Ce package contient l'ensemble des packages utilisés pour ce programme. Si l'ordinateur de l'utilisateur ne les a pas, ils pourront être installés dès le lancement de ce module.

#### 2. BestCities.py
Ce module contient la fonction permettant de déterminer les meilleures destinations pour un mois donné. Grâce à l'outil Selenium, les données sont recueillies sur le site "Où et quand partir" de Ouest France : https://partir.ouest-france.fr/. Son principe de fonctionnement consiste à récupérer et retourner la liste des 10 meilleures destinations à visiter pour le mois choisi.

   **Outils/ Packages** : *Selenium*

#### 3. BestMonth.py
Ce module permet de trouver les meilleurs mois pour visiter une ville déterminée en se basant notamment sur la température durant cette période. La fonction définie permet, grâce aux outils BeautifulSoup et Selenium, de récolter les informations nécessaires sur le site "Où et quand" : https://www.ou-et-quand.net/partir/quand/.
    
   **Outils/ Packages** : *BeautifulSoup, Selenium, time*
   
#### 4. Dashboard.py
Le module Dashboard permet d'afficher les informations enregitrées dans le fichier excel créé à la fin du lancement de TriPlanner. 

   **Outils/ Packages** : *Streamlit, pandas*

#### 5. Error.py
Le module error permet d'afficher un message d'erreur au cas où l'utilisateur oublierait d'insérer une critère de recherche dans la première boite de dialogue qui s'affiche.

   **Outils/ Packages** : *tkinter*

#### 6. Interface.py
Ce module contient la fonction qui affiche la première boite de dialogue devant interragir avec l'utilisateur. Elle lui donne la possibilité d'insérer la ville de son choix et/ou le mois désiré puis de lancer la recherche.

   **Outils/ Packages** : *tkinter*

#### 7. Interface_nocity.py
Dans le cas où l'utilisateur ne choisit que le mois, ce module intervient grâce à sa fonction définie pour extraire les 10 meilleures destinations pour le mois choisi. La fenêtre qui s'affiche offre alors dix possibilités à choix unique et obligatoire à l'utilisateur. 

   **Outils/ Packages** : *tkinter*

#### 8. Interface_nomonth.py
Dans le cas où l'utilisateur ne choisit que la ville et à partir de la fonction qui y est définie, ce module propose une fenêtre avec les 12 mois de l'année accompagnée de la situation de la météo. L'utilisateur dispose alors d'un choix unique et obligatoire.

   **Outils/ Packages** : *tkinter*

#### 9. Place2visit.py
Ce module contient la fonction capable de lister les 10 endroits à visiter d'une ville donnée. Elle exploite le site https://www.tripadvisor.fr/ notamment grâce à Selenium.

   **Outils/ Packages** : *Selenium, time, pyautogui*

#### 10. Restaurants.py
Ce module permet de sortir la liste des 10 meilleurs restaurants d'une ville. Les données sont exploitées sur le site https://www.tripadvisor.fr/Restaurants à partir des outils Selenium et BeautifulSoup. La fonction définie prend en compte la ville sélectionnée par l'utilisateur pour accéder aux meilleurs restaurants.

   **Outils/ Packages** : *Selenium, BeautifulSoup, time*

#### 11. Temp.py
Ce module s'occupe de la température. En effet, il extrait les températures mensuelles pour la ville sélectionnée sur le site https://www.ou-et-quand.net/partir/quand/. Les données recueillies permettent à l'utilisateur de savoir quelle est la tendance habituelle météologique de la ville à visiter pour chaque mois.

   **Outils/ Packages** : *BeautifulSoup, Selenium, time*
   
#### 12. TripPlanner.py
Ce derniere module est en réalité une version compactée du code du programme. Il permet de lancer l'ensemble des fonctions que contient les autres modules. En plus de faire appel à tous les modules précités, il utilise également pandas pour enregistrer à la fin les données dans un fichier excel.

   **Outils/ Packages** : *pandas*
