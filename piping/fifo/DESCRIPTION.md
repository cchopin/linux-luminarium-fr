On a appris à utiliser les tubes avec `|`, et l'on a vu que la substitution de processus crée des tubes nommés temporaires (comme `/dev/fd/63`).
On peut aussi créer ses propres tubes nommés _persistants_, qui restent sur le système de fichiers !
On les appelle des **FIFO**, abréviation de First (byte) In, First (byte) Out, c'est-à-dire « premier entré, premier sorti » (par octet).

On crée un FIFO avec la commande `mkfifo` :

```console
hacker@dojo:~$ mkfifo my_pipe
hacker@dojo:~$ ls -l my_pipe
prw-r--r-- 1 hacker hacker 0 Jan 1 12:00 my_pipe
hacker@dojo:~$ ls -l some_file
-rw-r--r-- 1 hacker hacker 0 Jan 1 12:00 some_file
hacker@dojo:~$
```

Le `p` au début des permissions indique qu'il s'agit d'un tube !
C'est très différent du `-` que l'on voit au début des fichiers normaux, comme `some_file` dans l'exemple ci-dessus.

Contrairement aux tubes nommés automatiques de la substitution de processus :

- on décide où les FIFO sont créés ;
- ils persistent tant qu'on ne les supprime pas ;
- n'importe quel processus peut écrire dedans par son chemin (par exemple `echo hi > my_pipe`) ;
- on peut les voir avec `ls` et les examiner comme des fichiers.

Un inconvénient des FIFO est qu'ils « bloquent » toute opération tant que le côté lecture et le côté écriture du tube ne sont pas tous deux prêts.
Par exemple :

```console
hacker@dojo:~$ mkfifo myfifo
hacker@dojo:~$ echo pwn > myfifo
```

Pour exécuter `echo pwn > myfifo`, bash ouvre le fichier `myfifo` en écriture.
Cette opération reste bloquée tant que quelqu'un d'autre n'ouvre pas aussi le fichier en lecture (ce qui complète le tube).
Cela peut se faire dans un autre terminal :

```console
hacker@dojo:~$ cat myfifo
pwn
hacker@dojo:~$
```

Que s'est-il passé ?
Quand on a lancé `cat myfifo`, le tube disposait de ses deux extrémités, il a été débloqué, ce qui a permis à `echo pwn > myfifo` de s'exécuter : `pwn` a été envoyé dans le tube, puis lu par `cat`.

Bien sûr, on pourrait faire la même chose avec des fichiers normaux : on sait y écrire avec `echo` et les lire avec `cat`.
Pourquoi utiliser un FIFO ? Voici les différences essentielles :

1. **Pas de stockage sur disque :** les FIFO font transiter les données directement entre processus, en mémoire, sans rien enregistrer sur le disque.
2. **Données éphémères :** une fois lues dans un FIFO, les données disparaissent (contrairement aux fichiers, où elles persistent).
3. **Synchronisation automatique :** les écrivains attendent que les lecteurs soient prêts, et réciproquement. C'est très utile ! Dans l'exemple ci-dessus, peu importe que `cat myfifo` ou `echo pwn > myfifo` soit lancé en premier : chacun attendra l'autre. Avec des fichiers, il faut veiller à exécuter l'écrivain avant le lecteur.
4. **Flux de données complexes :** les FIFO facilitent les flux complexes, la fusion et la division de données de façons souples. Par exemple, ils acceptent plusieurs lecteurs et plusieurs écrivains.

Ce défi est une introduction simple aux FIFO.
Il faut créer un fichier `/tmp/flag_fifo`, puis rediriger la sortie standard de `/challenge/run` vers ce fichier.
En cas de réussite, `/challenge/run` écrit le flag dans le FIFO !
Il ne reste qu'à le faire !

----
**Indice :**
Le comportement bloquant des FIFO rend ce défi difficile à résoudre dans un seul terminal.
Il peut être utile d'utiliser le mode Desktop ou VSCode pour ce défi, afin de lancer deux terminaux.
