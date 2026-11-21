Ensuite, on découvre `[]`.
Les crochets sont en quelque sorte une forme limitée de `?` : au lieu de correspondre à n'importe quel caractère, `[]` est un joker pour un sous-ensemble de caractères, précisé entre les crochets.
Par exemple, `[pwn]` correspond au caractère `p`, `w` ou `n`.
Par exemple :

```console
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a	file_b	file_c
hacker@dojo:~$ echo Look: file_[ab]
Look: file_a file_b
```

Essayons ici !
Nous avons placé plusieurs fichiers dans `/challenge/files`.
Se placer dans `/challenge/files`, puis lancer `/challenge/run` avec un seul argument qui, par globbing avec des crochets, correspond à `file_b`, `file_a`, `file_s` et `file_h` !
