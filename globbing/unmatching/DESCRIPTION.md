Parfois, on veut filtrer des fichiers dans un motif !
Heureusement, `[]` permet justement de le faire.
Si le premier caractère entre crochets est un `!` ou (dans les versions récentes de bash) un `^`, le motif s'inverse : cette partie du motif correspond aux caractères qui ne sont _pas_ listés.
Par exemple :

```console
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a	file_b	file_c
hacker@dojo:~$ echo Look: file_[!ab]
Look: file_c
hacker@dojo:~$ echo Look: file_[^ab]
Look: file_c
hacker@dojo:~$ echo Look: file_[ab]
Look: file_a file_b
```

Muni de ces connaissances, aller dans `/challenge/files` et lancer `/challenge/run` avec tous les fichiers dont le nom ne commence ni par `p`, ni par `w`, ni par `n` !

**NOTE :** le caractère `!` a une signification différente dans bash lorsqu'il n'est pas le premier caractère d'un motif `[]` : garder cela à l'esprit si quelque chose semble incohérent. `^` n'a pas ce problème, mais n'est pas compatible avec les anciens shells.
