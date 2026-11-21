On a lancé des processus, on les a observés, et maintenant on apprend à les _terminer_ !
Sous Linux, cela se fait avec la commande `kill`, au nom assez explicite.
Avec les options par défaut (les seules présentées dans ce niveau), `kill` termine un processus en lui laissant la possibilité de finir proprement ses tâches avant de cesser d'exister.

Imaginons un processus `sleep` gênant (`sleep` est un programme qui attend simplement le nombre de secondes indiqué sur la ligne de commande, ici 1337 secondes) lancé dans un autre terminal, comme ceci :

```console
hacker@dojo:~$ sleep 1337
```

Comment s'en débarrasser ?
On utilise `kill` pour le terminer, en lui passant en argument l'identifiant du processus (le `PID` obtenu avec `ps`), comme ceci :

```console
hacker@dojo:~$ ps -e | grep sleep
 342 pts/0    00:00:00 sleep
hacker@dojo:~$ kill 342
hacker@dojo:~$ ps -e | grep sleep
hacker@dojo:~$
```

Il est maintenant temps de terminer un premier processus !
Dans ce défi, `/challenge/run` refuse de s'exécuter tant que `/challenge/dont_run` tourne !
Il faut trouver le processus `dont_run` et le `kill`.
En cas d'échec, pwn.college niera toute connaissance de la mission de `pwn.college`.
Bonne chance.
