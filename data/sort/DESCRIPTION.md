Les fichiers (ou les lignes de sortie des commandes) ne sont pas toujours dans l'ordre souhaité !
La commande `sort` permet d'organiser les données.
Elle lit les lignes de son entrée (ou de fichiers) et les affiche dans l'ordre trié :

```console
hacker@dojo:~$ cat names.txt
  hack
  the
  planet
  with
  pwn
  college
hacker@dojo:~$ sort names.txt
  college
  hack
  planet
  pwn
  the
  with
hacker@dojo:~$
```

Par défaut, `sort` trie les lignes par ordre alphabétique.
Des arguments permettent de modifier ce comportement :

- `-r` : ordre inverse (de Z à A)
- `-n` : tri numérique (pour des nombres)
- `-u` : seulement les lignes uniques (suppression des doublons)
- `-R` : ordre aléatoire !

Dans ce défi, le fichier `/challenge/flags.txt` contient 100 faux flags, parmi lesquels se cache le vrai flag.
Une fois trié par ordre alphabétique, le vrai flag se trouve à la fin (on s'en est assuré en générant les faux flags).
Il ne reste plus qu'à le récupérer !
