Le globbing s'applique à des _chemins_, si bien qu'on peut développer des chemins entiers avec des arguments globbés.
Par exemple :

```console
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a	file_b	file_c
hacker@dojo:~$ echo Look: /home/hacker/file_[ab]
Look: /home/hacker/file_a /home/hacker/file_b
```

À nous de jouer.
Nous avons encore placé plusieurs fichiers dans `/challenge/files`.
Depuis le répertoire personnel, lancer `/challenge/run` avec un seul argument qui, par globbing avec des crochets, correspond aux chemins absolus des fichiers `file_b`, `file_a`, `file_s` et `file_h` !
