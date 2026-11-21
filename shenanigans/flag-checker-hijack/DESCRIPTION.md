Dans le niveau précédent, vous avez détourné le `~/.bashrc` de Zardus pour lui faire exécuter des commandes à votre place.

Cette fois, Zardus ne garde plus le flag dans un fichier lisible après sa connexion.
Il lance une commande appelée `flag_checker`, et tape lui-même le flag pour vérification.

Votre mission : utiliser votre accès en écriture persistant au `.bashrc` de Zardus pour intercepter ce flag.
Vous vous souvenez de la façon dont vous avez détourné des commandes dans le module [Réflexion sur PATH](https://pwn.college/linux-luminarium-fr/path) ?
Pouvez-vous utiliser cette capacité pour détourner `flag_checker` ?

----
**INDICE :**
Zardus se méfie-t-il de votre détournement ?
Il est prudent : il vérifie que l'invite `flag_checker` est bien `Type the flag`.
Assurez-vous que votre détournement affiche aussi cette invite (par exemple avec `echo "Type the flag"`).
En dehors de cette invite, votre faux `flag_checker` peut soit a) afficher la saisie de Zardus sur la sortie standard (par exemple `cat with no arguments`, c'est-à-dire `cat` sans argument), soit b) lire la saisie dans une variable avec `read`, puis l'afficher avec `echo`.
À vous de choisir !

----
**INDICE :**
N'oubliez pas de rendre votre faux `flag_checker` exécutable, comme vous l'avez appris dans le module [Perception des droits](https://pwn.college/linux-luminarium-fr/permissions) !
