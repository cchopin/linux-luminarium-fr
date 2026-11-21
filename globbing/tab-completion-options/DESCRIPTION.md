Imaginons la situation suivante :

```console
hacker@dojo:~$ ls
flag  flamingo  flowers
hacker@dojo:~$ cat f<TAB>
```

Il existe plusieurs possibilités !
Que se passe-t-il ?

Le comportement dépend du shell utilisé et de sa configuration.
Par défaut, `bash` complète jusqu'au premier point où les possibilités divergent (ici, `fl`).
Si l'on appuie une _seconde_ fois sur Tab, il affiche ces possibilités.
D'autres shells et d'autres configurations, au contraire, font défiler les possibilités.

Ce défi contient un répertoire `/challenge/files` avec de nombreux fichiers dont le nom commence par `pwncollege`.
Compléter par tabulation à partir de `/challenge/files/p` ou presque, et atteindre le flag !
