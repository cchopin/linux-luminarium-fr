On connaît maintenant le principe d'un chemin absolu et le fonctionnement du changement de répertoire.
Si l'on utilise partout des chemins absolus, le répertoire dans lequel on se trouve n'a aucune importance, comme on l'a sans doute constaté dans les trois défis précédents.

En revanche, le répertoire courant compte pour les chemins **relatifs**.

- Un chemin relatif est tout chemin qui ne part pas de la racine (c'est-à-dire qui ne commence pas par `/`).
- Un chemin relatif s'interprète **par rapport** au répertoire de travail courant (`cwd`, pour **c**urrent **w**orking **d**irectory).
- Le `cwd` est le répertoire dans lequel se trouve l'invite au moment considéré.

Cela signifie que la manière de désigner un fichier donné dépend de l'endroit où se trouve l'invite.

Imaginons que l'on veuille accéder à un fichier situé dans `/tmp/a/b/my_file`.

- Si le `cwd` est `/`, un chemin relatif vers le fichier est `tmp/a/b/my_file`.
- Si le `cwd` est `/tmp`, un chemin relatif vers le fichier est `a/b/my_file`.
- Si le `cwd` est `/tmp/a/b/c`, un chemin relatif vers le fichier est `../my_file`. Le `..` désigne le répertoire parent.

Changer de répertoire et lancer un programme sont deux actions distinctes.
Par exemple :

```console
hacker@dojo:~$ cd /
hacker@dojo:/$ bin/echo Hello
Hello
```

La première commande place le répertoire de travail courant sur `/`.
La seconde invoque `/bin/echo` à l'aide du chemin relatif `bin/echo`.

Essayons ici !
Commencer par placer le répertoire de travail courant sur `/`.
Puis lancer `/challenge/run` avec un chemin relatif.
Pour ce niveau, voici un indice : le chemin relatif commence par la lettre `c` 😊
