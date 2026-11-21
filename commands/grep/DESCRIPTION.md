Il arrive que les fichiers qu'on lit avec `cat` soient trop volumineux.
Heureusement, la commande `grep` permet de chercher le contenu dont on a besoin !
On l'apprendra dans ce défi.

Il existe de nombreuses façons d'utiliser `grep`. Nous en verrons une ici :

```console
hacker@dojo:~$ grep SEARCH_STRING /path/to/file
```

Utilisée ainsi, `grep` parcourt le fichier à la recherche des lignes contenant `SEARCH_STRING`, et les affiche dans le terminal.

Dans ce défi, on a placé cent mille lignes de texte dans le fichier `/challenge/data.txt`.
Il faut utiliser `grep` pour y trouver le flag !

INDICE : le flag commence toujours par le texte `pwn.college`.
