Commençons par la redirection de la sortie standard vers des fichiers.
On y parvient avec le caractère `>`, comme ceci :

```console
hacker@dojo:~$ echo hi > asdf
```

Cela redirige la sortie de `echo hi` (qui vaut `hi`) vers le fichier `asdf`.
On peut ensuite afficher ce fichier avec un programme comme `cat` :

```console
hacker@dojo:~$ cat asdf
hi
```

Dans ce défi, il faut utiliser cette redirection de sortie pour écrire le mot `PWN` (en majuscules) dans le fichier nommé `COLLEGE` (en majuscules).
