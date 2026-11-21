Le premier motif que nous apprenons est `*`.
Lorsqu'il rencontre un caractère `*` dans un argument, le shell le traite comme un « joker » et tente de remplacer cet argument par les fichiers qui correspondent au motif.
C'est plus facile à montrer qu'à expliquer :

```console
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a	file_b	file_c
hacker@dojo:~$ echo Look: file_*
Look: file_a file_b file_c
```

Bien sûr, si le motif donne plusieurs arguments dans cet exemple, il peut tout aussi bien n'en correspondre qu'à un seul.
Par exemple :

```console
hacker@dojo:~$ touch file_a
hacker@dojo:~$ ls
file_a
hacker@dojo:~$ echo Look: file_*
Look: file_a
```

Si aucun fichier ne correspond, le shell laisse le motif tel quel par défaut :

```console
hacker@dojo:~$ touch file_a
hacker@dojo:~$ ls
file_a
hacker@dojo:~$ echo Look: nope_*
Look: nope_*
```

Le `*` correspond à n'importe quelle partie d'un nom de fichier, sauf le `/` et un caractère `.` placé au début du nom.
Par exemple :

```console
hacker@dojo:~$ echo ONE: /ho*/*ck*
ONE: /home/hacker
hacker@dojo:~$ echo TWO: /*/hacker
TWO: /home/hacker
hacker@dojo:~$ echo THREE: ../*
THREE: ../hacker
```

À nous de nous entraîner !
Depuis le répertoire personnel, il faut passer dans `/challenge` avec `cd`, mais en utilisant un motif pour que l'argument donné à `cd` ne fasse pas plus de quatre caractères !
Une fois arrivé, lancer `/challenge/run` pour obtenir le flag.
