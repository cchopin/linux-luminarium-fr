Curieusement, `ls` n'affiche pas _tous_ les fichiers par défaut.
Linux suit une convention : les fichiers dont le nom commence par `.` n'apparaissent pas par défaut avec `ls`, ni dans quelques autres contextes.
Pour les afficher avec `ls`, il faut utiliser l'option `-a`, comme ceci :

```console
hacker@dojo:~$ touch pwn
hacker@dojo:~$ touch .college
hacker@dojo:~$ ls
pwn
hacker@dojo:~$ ls -a
.college	pwn
hacker@dojo:~$
```

À nous de jouer !
Il faut trouver le flag, caché sous la forme d'un fichier dont le nom commence par un point, dans `/`.
