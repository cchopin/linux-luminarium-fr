Jusqu'ici, on a surtout manipulé les permissions de *lecture*.
C'est logique, puisqu'on a rendu le fichier `/flag` lisible pour le lire.
Dans ce niveau, on explore les permissions d'exécution.

Quand on lance un programme, comme `/challenge/run`, Linux ne l'exécute réellement que si l'on a l'accès en exécution sur le fichier du programme.
Observons :

```console
hacker@dojo:~$ ls -l /challenge/run
-rwxr-xr-x 1 root root    0 May 22 13:42 /challenge/run
hacker@dojo:~$ /challenge/run
Successfully ran the challenge!
hacker@dojo:~$
```

Ici, `/challenge/run` s'exécute parce que l'utilisateur `hacker` peut l'exécuter.
Comme le fichier appartient à l'utilisateur `root` et au groupe `root`, cela suppose que le bit d'exécution est positionné pour les permissions de `other`, c'est-à-dire des autres utilisateurs.
Si l'on retire ces permissions, l'exécution échoue !

```console
hacker@dojo:~$ chmod o-x /challenge/run
hacker@dojo:~$ ls -l /challenge/run
-rwxr-xr-- 1 root root    0 May 22 13:42 /challenge/run
hacker@dojo:~$ /challenge/run
bash: /challenge/run: Permission denied
hacker@dojo:~$
```

Dans ce défi, le programme `/challenge/run` donne le flag, mais il faut d'abord le rendre exécutable !
Il suffit de se souvenir de `chmod` pour faire afficher le flag par `/challenge/run`.
