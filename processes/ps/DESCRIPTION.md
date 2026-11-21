On commence par lister les processus en cours avec la commande `ps`.
Selon l'interlocuteur, `ps` signifie « process snapshot » (instantané des processus) ou « process status » (état des processus) : elle liste les processus.
Par défaut, `ps` se contente de lister les processus lancés dans le terminal courant, ce qui n'est pas très utile :

```console
hacker@dojo:~$ ps
    PID TTY          TIME CMD
    329 pts/0    00:00:00 bash
    349 pts/0    00:00:00 ps
hacker@dojo:~$
```

Dans l'exemple ci-dessus, on voit le shell (`bash`) et le processus `ps` lui-même, et ce sont les seuls processus qui tournent sur ce terminal.
On constate aussi que chaque processus possède un identifiant numérique (le _Process ID_, ou PID), un nombre qui identifie de manière unique chaque processus en cours sous Linux.
On voit également le terminal sur lequel les commandes s'exécutent (ici `pts/0`), et le temps total de _processeur_ déjà consommé par le processus (ces processus sont si peu gourmands qu'ils n'ont pas encore consommé la moindre seconde !).

Dans la plupart des cas, c'est tout ce qu'on voit avec un `ps` par défaut.
Pour le rendre utile, il faut passer quelques arguments.

Comme `ps` est un utilitaire très ancien, son usage est un peu confus.
Il existe deux façons de spécifier les arguments.

**Syntaxe « standard » :** avec cette syntaxe, `-e` liste « tous » les processus et `-f` affiche un format « complet », incluant les arguments.
Ces options peuvent être combinées en un seul argument `-ef`.

**Syntaxe « BSD » :** avec cette syntaxe, `a` liste les processus de tous les utilisateurs, `x` liste les processus qui ne tournent pas dans un terminal, et `u` affiche un format lisible par l'utilisateur.
Ces options peuvent être combinées en un seul argument `aux`.

Ces deux méthodes, `ps -ef` et `ps aux`, donnent des sorties légèrement différentes, mais faciles à relier entre elles.

Essayons dans le dojo :

```console
hacker@dojo:~$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
hacker         1       0  0 05:34 ?        00:00:00 /sbin/docker-init -- /bin/sleep 6h
hacker         7       1  0 05:34 ?        00:00:00 /bin/sleep 6h
hacker       102       1  1 05:34 ?        00:00:00 /usr/lib/code-server/lib/node /usr/lib/code-server --auth=none -
hacker       138     102 11 05:34 ?        00:00:07 /usr/lib/code-server/lib/node /usr/lib/code-server/out/node/entr
hacker       287     138  0 05:34 ?        00:00:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/ou
hacker       318     138  6 05:34 ?        00:00:03 /usr/lib/code-server/lib/node --dns-result-order=ipv4first /usr/
hacker       554     138  3 05:35 ?        00:00:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/ou
hacker       571     554  0 05:35 pts/0    00:00:00 /usr/bin/bash --init-file /usr/lib/code-server/lib/vscode/out/vs
hacker       695     571  0 05:35 pts/0    00:00:00 ps -ef
hacker@dojo:~$
```

On voit ici les processus d'initialisation de l'environnement du défi (`docker-init`), un délai d'attente qui met fin au défi automatiquement pour préserver les ressources de calcul (`sleep 6h`, qui expire au bout de 6 heures), l'environnement VSCode (plusieurs processus auxiliaires `code-server`), le shell (`bash`), et ma commande `ps -ef`.
C'est pratiquement la même chose avec `ps aux` :

```
hacker@dojo:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
hacker         1  0.0  0.0   1128     4 ?        Ss   05:34   0:00 /sbin/docker-init -- /bin/sleep 6h
hacker         7  0.0  0.0   2736   580 ?        S    05:34   0:00 /bin/sleep 6h
hacker       102  0.4  0.0 723944 64660 ?        Sl   05:34   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       138  3.3  0.0 968792 106272 ?       Sl   05:34   0:07 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       287  0.0  0.0 717648 53136 ?        Sl   05:34   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       318  3.3  0.0 977472 98256 ?        Sl   05:34   0:06 /usr/lib/code-server/lib/node --dns-result-order=
hacker       554  0.4  0.0 650560 55360 ?        Rl   05:35   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       571  0.0  0.0   4600  4032 pts/0    Ss   05:35   0:00 /usr/bin/bash --init-file /usr/lib/code-server/li
hacker      1172  0.0  0.0   5892  2924 pts/0    R+   05:38   0:00 ps aux
hacker@dojo:~$
```

Les deux commandes ont beaucoup de points communs : elles affichent l'utilisateur (colonne `USER`), le PID, le TTY, l'heure de démarrage du processus (`STIME`/`START`), le temps total de processeur utilisé (`TIME`) et la commande (`CMD`/`COMMAND`).
`ps -ef` affiche en plus l'_identifiant du processus parent_ (`PPID`), c'est-à-dire le PID du processus qui a lancé celui-ci, alors que `ps aux` affiche le pourcentage du processeur et de la mémoire du système utilisé par le processus.
Il existe aussi bien d'autres informations, que l'on n'aborde pas maintenant.

Bref !
Passons à la pratique.
Dans ce niveau, `/challenge/run` a encore été renommé avec un nom de fichier aléatoire, et cette fois il est impossible de faire un `ls` sur le répertoire `/challenge` !
Mais comme il a été lancé, on peut retrouver son nom dans la liste des processus en cours, puis le relancer directement pour obtenir le flag !
Bonne chance !

**Note :** `ps -ef` et `ps aux` tronquent la liste des commandes à la largeur du terminal (c'est pourquoi les exemples ci-dessus s'alignent si bien sur le côté droit de l'écran).
Si l'on ne peut pas lire le chemin complet du processus, il faut peut-être agrandir le terminal, ou rediriger la sortie quelque part pour éviter cette troncature !
On peut aussi passer l'option `w` _deux fois_ (par exemple `ps -efww` ou `ps auxww`) pour désactiver la troncature.
