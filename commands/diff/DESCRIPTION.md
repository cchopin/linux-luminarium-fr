Pour repérer les modifications entre des fichiers semblables, les comparer à l'œil n'est pas forcément la méthode la plus efficace !
C'est là que la commande `diff` devient précieuse.

`diff` compare deux fichiers ligne par ligne et montre exactement ce qui diffère entre eux.
Par exemple :

```console
hacker@dojo:~$ cat file1
hello
world
hacker@dojo:~$ cat file2
hello
universe
hacker@dojo:~$ diff file1 file2
2c2
< world
---
> universe
```

La sortie indique que la ligne 2 a changé (`2c2`) : `world` dans le premier fichier (`<`) est remplacé par `universe` dans le second (`>`).

Parfois, lorsque de nouvelles lignes sont ajoutées, on voit ceci :

```console
hacker@dojo:~$ cat old
pwn
hacker@dojo:~$ cat new
pwn
college
hacker@dojo:~$ diff old new
1a2
> college
```

Cela signifie qu'après la ligne 1 du premier fichier, le second fichier contient une ligne supplémentaire (`1a2` signifie « après la ligne 1 du fichier 1, ajouter la ligne 2 du fichier 2 »).

Passons au défi !
Il y a deux fichiers dans `/challenge` :
- `/challenge/decoys_only.txt` contient 100 faux flags ;
- `/challenge/decoys_and_real.txt` contient les 100 faux flags, plus le vrai flag.

Utiliser `diff` pour trouver ce qui diffère entre ces fichiers, et obtenir le flag !
