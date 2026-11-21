On peut aussi _déplacer_ des fichiers avec la commande `mv`.
L'usage est simple :

```console
hacker@dojo:~$ ls
my-file
hacker@dojo:~$ cat my-file
PWN!
hacker@dojo:~$ mv my-file your-file
hacker@dojo:~$ ls
your-file
hacker@dojo:~$ cat your-file
PWN!
hacker@dojo:~$
```

Ce défi demande de déplacer le fichier `/flag` vers `/tmp/hack-the-planet`. À faire !
Attention : il faut _obligatoirement_ utiliser la commande `mv`, et non une autre méthode (comme renommer le fichier dans VSCode).
Une fois cela fait, lancer `/challenge/check`, qui vérifie le travail et donne le flag.
