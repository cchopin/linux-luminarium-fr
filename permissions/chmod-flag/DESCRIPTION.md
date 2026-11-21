Après la propriété, passons à l'autre face de la médaille : les permissions des fichiers.
Reprenons notre exemple :

```console
hacker@dojo:~$ mkdir pwn_directory
hacker@dojo:~$ touch college_file
hacker@dojo:~$ ls -l
total 4
-rw-r--r-- 1 hacker hacker    0 May 22 13:42 college_file
drwxr-xr-x 2 hacker hacker 4096 May 22 13:42 pwn_directory
hacker@dojo:~$
```

Pour rappel, le premier caractère désigne le type de fichier.
Les neuf caractères suivants sont les permissions d'accès réelles du fichier ou du répertoire, répartis en trois groupes de trois caractères : les permissions du propriétaire (on comprend déjà cela !), celles du groupe propriétaire (on comprend désormais cela aussi !), et celles de tous les autres accès (par exemple, les autres utilisateurs et les autres groupes).

Chacun des trois caractères représente une permission de nature différente. Dans le bloc ci-dessus, la lettre désigne le droit (lecture, écriture, exécution, ou aucun droit) et s'applique à l'utilisateur, au groupe ou aux autres :

```
r - user/group/other can read the file (or list the directory)
w - user/group/other can modify the files (or create/delete files in the directory)
x - user/group/other can execute the file as a program (or can enter the directory, e.g., using `cd`)
- - nothing 
```

Pour `college_file` ci-dessus, la permission `rw-r--r--` se lit ainsi :

- `r` : l'utilisateur propriétaire du fichier (l'utilisateur `hacker`) peut le lire ;
- `w` : l'utilisateur propriétaire du fichier (l'utilisateur `hacker`) peut y écrire ;
- `-` : l'utilisateur propriétaire du fichier (l'utilisateur `hacker`) *ne peut pas* l'exécuter ;
- `r` : les utilisateurs du groupe propriétaire du fichier (le groupe `hacker`) peuvent le lire ;
- `-` : les utilisateurs du groupe propriétaire du fichier (le groupe `hacker`) *ne peuvent pas* y écrire ;
- `-` : les utilisateurs du groupe propriétaire du fichier (le groupe `hacker`) *ne peuvent pas* l'exécuter ;
- `r` : tous les autres utilisateurs peuvent le lire ;
- `-` : tous les autres utilisateurs *ne peuvent pas* y écrire ;
- `-` : tous les autres utilisateurs *ne peuvent pas* l'exécuter.

Regardons maintenant les permissions par défaut de `/flag` :

```console
hacker@dojo:~$ ls -l /flag
-r-------- 1 root root 53 Jul  4 04:47 /flag
hacker@dojo:~$
```

Ici, un seul bit est positionné : le droit de **l**ecture pour le propriétaire (dans ce cas, `root`).
Les membres du groupe propriétaire (le groupe `root`) et tous les autres utilisateurs n'ont aucun accès au fichier.

On peut se demander comment les niveaux sur `chgrp` fonctionnaient, puisque le groupe n'avait aucun accès au fichier.
Dans ces niveaux, les permissions étaient différentes :

```console
hacker@dojo:~$ ls -l /flag
-r--r----- 1 root root 53 Jul  4 04:47 /flag
hacker@dojo:~$
```

Le groupe avait accès au fichier !
C'est pour cela que le changement de groupe permettait de lire le fichier.

Bref !
Comme la propriété, les permissions d'un fichier peuvent aussi être modifiées.
Cela se fait avec la commande `chmod` (**ch**ange **mod**e).
L'usage de base de chmod est :

```
chmod [OPTIONS] MODE FILE
```

Le `MODE` peut s'exprimer de deux façons : comme une modification des permissions existantes, ou comme un nouveau mode complet qui remplace l'ancien.

Dans ce niveau, on utilise la première forme : modifier un mode existant.
`chmod` permet d'ajuster les permissions avec le format `WHO`+/-`WHAT`, où `WHO` désigne l'utilisateur, le groupe ou les autres, et `WHAT` la lecture, l'écriture ou l'exécution.
Par exemple, pour ajouter le droit de *lecture* au propriétaire, on indique le mode `u+r`.
Les droits d'écriture (`w`) et d'exécution (`x`) pour le `g`roupe et pour les `o`utres (ou pour `a`ll, c'est-à-dire tout le monde) s'écrivent de la même façon.
D'autres exemples :

- `u+r`, comme ci-dessus, ajoute le droit de lecture au propriétaire ;
- `g+wx` ajoute l'écriture et l'exécution au groupe ;
- `o-w` *retire* le droit d'écriture aux autres utilisateurs ;
- `a-rwx` retire toutes les permissions au propriétaire, au groupe et aux autres.

Ainsi :

```console
root@dojo:~# mkdir pwn_directory
root@dojo:~# touch college_file
root@dojo:~# ls -l
total 4
-rw-r--r-- 1 root root    0 May 22 13:42 college_file
drwxr-xr-x 2 root root 4096 May 22 13:42 pwn_directory
root@dojo:~# chmod go-rwx *
root@dojo:~# ls -l
total 4
-rw------- 1 hacker root    0 May 22 13:42 college_file
drwx------ 2 root   root 4096 May 22 13:42 pwn_directory
root@dojo:~#
```

Dans ce défi, il faut modifier les permissions du fichier `/flag` pour pouvoir le lire !
En général, il faut être propriétaire d'un fichier pour changer ses permissions. Mais pour ce niveau, la commande `chmod` a été rendue toute-puissante : on peut modifier n'importe quel fichier en tant qu'utilisateur `hacker`.
C'est un pouvoir absolu.
Le fichier `/flag` appartient à `root`, et on ne peut pas changer cela, mais on peut le rendre lisible.
Il ne reste plus qu'à résoudre ce défi !
