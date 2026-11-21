Chaque utilisateur possède un _répertoire personnel_ (home directory), généralement situé sous `/home`.
Dans le dojo, l'utilisateur est `hacker`, et son répertoire personnel est `/home/hacker`.
Le répertoire personnel est l'endroit où un utilisateur range la plupart de ses fichiers personnels.
Au fil de pwn.college, c'est là que l'on rangera la plupart de ses solutions.

En général, une session de shell démarre dans le répertoire personnel, qui sert alors de répertoire de travail courant.
Regardons l'invite de départ :

```console
hacker@dojo:~$
```

Le `~` de cette invite est le répertoire de travail courant, `~` étant un raccourci pour `/home/hacker`.
Bash propose ce raccourci et l'utilise, parce que la plupart du temps, on passe son temps dans le répertoire personnel.
Ainsi, dès que bash voit `~` au début d'un argument qui ressemble à un chemin, il le remplace par le répertoire personnel.
Regardons :

```console
hacker@dojo:~$ echo LOOK: ~
LOOK: /home/hacker
hacker@dojo:~$ cd /
hacker@dojo:/$ cd ~
hacker@dojo:~$ cd ~/asdf
hacker@dojo:~/asdf$ cd ~/asdf
hacker@dojo:~/asdf$ cd ~
hacker@dojo:~$ cd /home/hacker/asdf
hacker@dojo:~/asdf$
```

Notons que le remplacement de `~` donne un chemin _absolu_, et seul le `~` placé en début d'argument est remplacé.
Ainsi, `~/~` sera remplacé par `/home/hacker/~`, et non par `/home/hacker/home/hacker`.

Petite particularité : `cd` utilise le répertoire personnel comme destination par défaut :

```console
hacker@dojo:~$ cd /tmp
hacker@dojo:/tmp$ cd
hacker@dojo:~$
```

À notre tour de jouer !
Dans ce défi, `/challenge/run` écrit une copie du flag dans le fichier que l'on indique en argument sur la ligne de commande, avec ces contraintes :

1. L'argument doit être un chemin absolu.
2. Le chemin doit se trouver dans le répertoire personnel.
3. Avant expansion, l'argument doit comporter trois caractères ou moins.

Il faut indiquer le chemin en _argument_ de `/challenge/run`, comme ceci :

```console
hacker@dojo:~$ /challenge/run YOUR_PATH_HERE
```
