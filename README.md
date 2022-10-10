# Trip planner project (TPP)
 
#######README.md (explain what is your project and how to run it, what were the issues, what are the key results, ...)
## Description 

TPP est un programme destiné à faciliter la planification de vos vacances. 
Pour votre séjour, si vous devez visiter une ville bien précise ou encore, si vous prévoyez de partir en vacances à un mois bien déterminé ignorant votre destination, TPP peut vous accompagner dans vos prépartions.

Dépendamment de votre cas, il vous permet d'obtenir la meilleure période à visiter une ville ou les meilleures destinations pour un mois donné, les 10 meilleurs endroits à visiter dans la ville selectionnée et les meilleurs restaurants où manger. 

# Utilisation

TPP a été conçu afin de faciliter son utilisation auprès des utilisateurs. A cet effet, l'utilisateur doit suivre les étapes suivantes :

I- Afin de disposer de l'environnement adéquat

   1. Télécharger le fichier Trip-planner et l"enregistrer dans un dossier sur son ordinateur
   2. Télécharger Chromedriver.exe et l'enregistrer dans le dossier trip-planner

II- Pour lancer TPP et obtenir les informations souhaitées

   3. Ouvrir le terminal à partir de la fenêtre du dossier trip-planner
   4. Entrer la commande qui suit et attendre que tous les packages nécessaires soient installés :
 
    python allpackages.py
    
   5. Entrer la commande ci-après pour lancer le logiciel. Une fenêtre va s'ouvrir pour aider l'utilisateur à choisir ses paramètres (Ville et/ou mois de voyage) : 
        
    python trip-planner.py

   6. Entrer la commande ci-après pour afficher le dashboard : 
   
    streamlit run dashborad.py

Un fichier excel comportant vos informations est également créé et stocké dans le fichier.


