Quand on tape le nom d'une commande, _quelque chose_ situé dans l'un des nombreux répertoires listés dans la variable `$PATH` est réellement exécuté (sauf si la commande est une primitive du shell !).
Mais _quel_ fichier, précisément ?
On peut le savoir avec la commande `which`, au nom bien trouvé :

```console
hacker@dojo:~$ which cat
/bin/cat
hacker@dojo:~$ /bin/cat /flag
YEAH
hacker@dojo:~$
```

Comme le fait le shell pour chercher les commandes, `which` parcourt chaque répertoire de `$PATH` dans l'ordre, et affiche le premier fichier dont le nom correspond à l'argument donné.

Dans ce défi, on a ajouté une commande `win` quelque part dans votre `$PATH`, mais elle ne donne pas le flag.
Elle se trouve dans le même répertoire qu'un fichier `flag` que nous avons rendu lisible pour vous !
Il faut trouver `win` (avec la commande `which`), et afficher le flag contenu dans ce répertoire avec `cat` !
