Le système de fichiers Linux contient une multitude de répertoires et de fichiers.
On se déplace entre les répertoires avec la commande `cd` (pour `c`hange `d`irectory, « changer de répertoire »), en lui passant un chemin en argument, comme ceci :

```console
hacker@dojo:~$ cd /some/new/directory
hacker@dojo:/some/new/directory$
```

Cela modifie le « répertoire de travail courant » de notre processus (ici, le shell bash).
Chaque processus se trouve dans un répertoire donné.
Les raisons de cela apparaîtront plus tard dans le module.

Au passage, on comprend maintenant ce qu'était le `~` du prompt !
Il indique le chemin dans lequel se trouve le shell.

Ce défi demande d'exécuter le programme `/challenge/run` depuis un chemin précis (que le défi indique).
Il faut utiliser `cd` pour se placer dans ce répertoire avant de relancer le programme du défi.
Bonne chance !
