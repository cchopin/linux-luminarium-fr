Le partage est une bonne chose, et il est intégré à la conception de Linux.
Les fichiers ont à la fois un _utilisateur_ et un _groupe_ propriétaires.
Un groupe peut compter plusieurs utilisateurs, et un utilisateur peut appartenir à plusieurs groupes.

On peut vérifier les groupes auxquels on appartient avec la commande `id` :

```console
hacker@dojo:~$ id
uid=1000(hacker) gid=1000(hacker) groups=1000(hacker)
hacker@dojo:~$
```

Ici, l'utilisateur `hacker` appartient _uniquement_ au groupe `hacker`.
Le cas d'usage le plus courant des groupes est de contrôler l'accès à différentes ressources du système.
Par exemple, le « mode privilégié » de pwn.college accorde les droits `root` pour faciliter le débogage, etc.
Cela se fait en ajoutant un groupe supplémentaire lors du lancement en mode privilégié :

```console
hacker@dojo:~$ id
uid=1000(hacker) gid=1000(hacker) groups=1000(hacker),27(sudo)
hacker@dojo:~$
```

L'utilisateur principal d'un bureau Linux typique appartient à de *très* nombreux groupes.
Par exemple, voici le bureau de Zardus :

```console
zardus@yourcomputer:~$ id
uid=1000(zardus) gid=1000(zardus) groups=1000(zardus),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),114(bluetooth),117(lpadmin),120(scanner),995(docker)
zardus@yourcomputer:~$
```

Ces groupes permettent à Zardus de lire des CD et des disquettes (qui fait encore ça ?), d'administrer le système, de jouer de la musique, d'écrire sur l'écran vidéo, d'utiliser le bluetooth, et ainsi de suite.
Ce contrôle d'accès passe souvent par la propriété de groupe sur le système de fichiers !
Par exemple, l'affichage graphique peut se faire via le fichier spécial `/dev/fb0` :

```console
zardus@yourcomputer:~$ ls -l /dev/fb0
crw-rw---- 1 root video 29, 0 Jun 30 23:42 /dev/fb0
zardus@yourcomputer:~$
```

Ce fichier est un *fichier de périphérique* (le type `c` indique un « périphérique caractère »), et interagir avec lui modifie l'affichage (et non le stockage sur disque, comme pour un fichier ordinaire !).
Le compte de Zardus peut interagir avec ce fichier parce que son groupe propriétaire est `video`, et que Zardus est membre du groupe `video`.

Mais le fichier `/flag` du dojo n'a pas cette chance !
Observons :

```console
hacker@dojo:~$ id
uid=1000(hacker) gid=1000(hacker) groups=1000(hacker)
hacker@dojo:~$ ls -l /flag
-r--r----- 1 root root ... /flag
hacker@dojo:~$ cat /flag
cat: /flag: Permission denied
hacker@dojo:~$
```

Ici, le fichier flag appartient à l'utilisateur `root` et au groupe `root`. L'utilisateur `hacker` n'est ni `root`, ni membre du groupe `root` : le fichier est donc inaccessible.
Heureusement, la propriété de groupe peut être modifiée avec la commande `chgrp` (**ch**ange **gr**ou**p**). Sauf si l'on est propriétaire du fichier *et* membre du nouveau groupe, cette opération demande en général les droits `root`. Regardons donc ce qu'elle fait en tant que `root` :

```console
root@dojo:~# mkdir pwn_directory
root@dojo:~# touch college_file
root@dojo:~# ls -l
total 4
-rw-r--r-- 1 root root    0 May 22 13:42 college_file
drwxr-xr-x 2 root root 4096 May 22 13:42 pwn_directory
root@dojo:~# chgrp hacker college_file
root@dojo:~# ls -l
total 4
-rw-r--r-- 1 root hacker    0 May 22 13:42 college_file
drwxr-xr-x 2 root root   4096 May 22 13:42 pwn_directory
root@dojo:~#
```

Dans ce niveau, le flag a été rendu lisible par le groupe qui le possède, mais ce groupe est actuellement `root`.
Par chance, la commande `chgrp` peut aussi être exécutée par l'utilisateur `hacker` dans ce défi !
Il faut changer le groupe propriétaire du fichier flag, puis lire le flag !
