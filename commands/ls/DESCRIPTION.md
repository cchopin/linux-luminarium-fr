Jusqu'ici, on indiquait soi-même quels fichiers utiliser.
Mais les répertoires peuvent contenir beaucoup de fichiers et de sous-répertoires, et nous ne serons pas toujours là pour en donner les noms.
Il faut apprendre à **l**i**s**ter leur contenu avec la commande `ls` !

`ls` affiche les fichiers de chaque répertoire donné en argument, et du répertoire courant si aucun argument n'est donné.
Observons :

```console
hacker@dojo:~$ ls /challenge
run
hacker@dojo:~$ ls
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
hacker@dojo:~$ ls /home/hacker
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
hacker@dojo:~$
```

Dans ce défi, le programme `/challenge/run` porte un nom aléatoire !
Lister les fichiers de `/challenge` pour le trouver.
Puis exécuter son chemin absolu pour obtenir le flag.
