Commençons par le plus important : la propriété des fichiers.
Sous Linux, chaque fichier appartient à un utilisateur du système.
Au quotidien, cet utilisateur est le plus souvent celui avec lequel on ouvre sa session chaque jour.

Sur un système partagé (comme dans un laboratoire informatique), plusieurs personnes ont des comptes différents, chacune avec ses fichiers dans son répertoire personnel.
Mais même sur un système non partagé (comme un PC personnel), Linux possède encore de nombreux comptes « de service » pour différentes tâches.

Les deux comptes les plus importants sont :

1. Le compte utilisateur de la session ! Sur pwn.college, c'est l'utilisateur `hacker`, quel que soit le nom d'utilisateur réel.
2. `root`. C'est le compte d'administration et, dans la plupart des situations de sécurité, la prise ultime. Si l'on prend le contrôle de l'utilisateur `root`, l'objectif d'un pirate est presque toujours atteint !

Et alors ?
Eh bien, si l'on empêche de faire simplement `cat /flag`, c'est parce que `/flag` appartient à l'utilisateur `root`, que ses permissions ne laissent lire le fichier à aucun autre utilisateur (on apprendra plus tard comment faire), et que le défi lui-même s'exécute en tant que `root` (on apprendra aussi comment faire cela). Le résultat, lorsqu'on fait `cat /flag`, est :

```console
hacker@dojo:~$ ls -l /flag
-r-------- 1 root root 53 Jul  4 04:47 /flag
hacker@dojo:~$ cat /flag
cat: /flag: Permission denied
hacker@dojo:~$
```

On voit que le flag appartient à l'utilisateur `root` (le premier `root` de la ligne) et au groupe `root` (le second `root`).
Lorsque l'on tente de le lire en tant qu'utilisateur `hacker`, l'accès est refusé.
En revanche, en tant que `root` (le rêve de tout pirate !), la lecture de ce fichier ne pose aucun problème :

```console
root@dojo:~# cat /flag
pwn.college{demo_flag}
root@dojo:~#
```

Il est intéressant de constater qu'on peut modifier la propriété des fichiers !
Cela se fait avec la commande `chown` (**ch**ange **own**er) :

```
chown [username] [file]
```

En général, seul l'utilisateur `root` peut exécuter `chown`.
Faisons comme si l'on était à nouveau `root` (ça ne lasse jamais !), et observons un usage typique de `chown` :

```console
root@dojo:~# mkdir pwn_directory
root@dojo:~# touch college_file
root@dojo:~# ls -l
total 4
-rw-r--r-- 1 root root    0 May 22 13:42 college_file
drwxr-xr-x 2 root root 4096 May 22 13:42 pwn_directory
root@dojo:~# chown hacker college_file
root@dojo:~# ls -l
total 4
-rw-r--r-- 1 hacker root    0 May 22 13:42 college_file
drwxr-xr-x 2 root   root 4096 May 22 13:42 pwn_directory
root@dojo:~#
```

Le propriétaire de `college_file` est devenu l'utilisateur `hacker`, qui peut désormais faire avec ce fichier tout ce que `root` pouvait faire !
Si c'était le fichier `/flag`, l'utilisateur `hacker` pourrait donc le lire !

Dans ce niveau, il faut changer le propriétaire du fichier `/flag` pour l'utilisateur `hacker`, puis lire le flag.
Pour ce défi seulement, la commande `chown` est utilisable à volonté par l'utilisateur `hacker` (en général, elle exige d'être `root`).
Cette puissance doit être utilisée avec sagesse. Il ne reste plus qu'à s'y mettre !
