Ensuite, apprenons `?`.
Lorsqu'il rencontre un caractère `?` dans un argument, le shell le traite comme un joker qui correspond à **un seul** caractère.
Cela fonctionne comme `*`, mais ne correspond qu'à _un_ caractère.
Par exemple :

```console
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_cc
hacker@dojo:~$ ls
file_a	file_b	file_cc
hacker@dojo:~$ echo Look: file_?
Look: file_a file_b
hacker@dojo:~$ echo Look: file_??
Look: file_cc
```

Maintenant, à nous de nous entraîner !
Depuis le répertoire personnel, passer dans `/challenge` avec `cd`, mais en utilisant le caractère `?` à la place de `c` et de `l` dans l'argument donné à `cd` !
Une fois arrivé, lancer `/challenge/run` pour obtenir le flag.
