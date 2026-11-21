On a déjà écrit son premier script shell, mais l'appeler avec `bash script.sh` est pénible.
Pourquoi a-t-on besoin de ce `bash` ?

Quand on exécute `bash script.sh`, on lance bien sûr la commande `bash` avec l'argument `script.sh`.
Cela demande à bash de lire ses commandes dans `script.sh` au lieu de l'entrée standard : le script shell est donc exécuté.

Il est possible de se passer d'appeler `bash` à la main.
Si le fichier du script est *exécutable* (voir [Permissions de fichiers](https://pwn.college/linux-luminarium-fr/permissions)), on peut l'appeler directement par son chemin relatif ou absolu !
Par exemple, si l'on crée `script.sh` dans son répertoire personnel *et qu'on le rend exécutable*, on peut l'appeler par `/home/hacker/script.sh`, par `~/script.sh`, ou (si le répertoire courant est `/home/hacker`) par `./script.sh`.

À essayer ici !
Il faut écrire un script shell qui appelle `/challenge/solve`, le rendre exécutable, puis le lancer sans appeler explicitement `bash`.
