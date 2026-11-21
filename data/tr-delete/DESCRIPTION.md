`tr` peut aussi remplacer des caractères par rien, c'est-à-dire les _supprimer_.
Cela se fait avec l'option `-d`, suivie des caractères à supprimer :

```console
hacker@dojo:~$ echo PAWN | tr -d A
PWN
hacker@dojo:~$
```

Très simple !
Essayons maintenant.
Dans la sortie de `/challenge/run`, on a intercalé des caractères parasites (précisément `^` et `%`) parmi les caractères du flag.
Il faut utiliser `tr -d` pour les retirer !
