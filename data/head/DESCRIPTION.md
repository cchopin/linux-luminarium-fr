Au cours d'un parcours sous Linux, il arrivera de devoir ne récupérer que le début de la sortie de programmes très verbeux.
Pour cela, on utilise `head` !
La commande `head` affiche les premières lignes de son entrée :

```console
hacker@dojo:~$ cat /something/very/long | head
this
is
just
the
first
ten
lines
of
the
file
hacker@dojo:~$
```

Par défaut, elle affiche les 10 premières lignes, mais l'option `-n` permet de changer ce nombre :

```console
hacker@dojo:~$ cat /something/very/long | head -n 2
this
is
hacker@dojo:~$
```

Ce défi affiche une grande quantité de données avec `/challenge/pwn`, et il faut la faire passer par `head` pour ne garder que les 7 premières lignes, puis les envoyer vers `/challenge/college`, qui donnera le flag si l'on procède correctement !
La solution sera une longue commande composée, avec _deux_ tubes reliant trois commandes.
Bonne chance !
