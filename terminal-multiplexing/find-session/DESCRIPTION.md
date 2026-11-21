Il est temps de mener une petite enquête avec screen !

Quand on utilise screen régulièrement, on finit inévitablement avec plusieurs sessions en cours.
Comment trouver celle à laquelle se rattacher ?

Il suffit de les lister :

```console
hacker@dojo:~$ screen -ls
There are screens on:
        23847.mysession   (Detached)
        23851.goodwork    (Detached)
        23855.morework    (Detached)
3 Sockets in /run/screen/S-hacker.
```

Les identifiants des sessions sont le PID de chaque processus screen, suivi d'un point, puis du nom de la session.
Pour se rattacher à une session précise, on donne son nom ou son PID en argument de `screen -r`.

```console
hacker@dojo:~$ screen -r goodwork
```

Dans ce défi, trois sessions screen ont été créées.
L'une contient le flag, les deux autres sont des leurres !

Il faut vérifier chacune jusqu'à trouver le bon flag.
Ne pas oublier de se détacher (Ctrl-A d) avant de passer à la session suivante !
