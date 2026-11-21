Bien sûr, il n'est pas nécessaire de suspendre des processus pour les passer en arrière-plan : on peut les lancer directement en arrière-plan !
C'est simple : il suffit d'ajouter un `&` à la commande, comme ceci :

```console
hacker@dojo:~$ sleep 1337 &
[1] 1771
hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker      1709 Ss   bash
hacker      1771 S    sleep 1337
hacker      1782 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$ 
```

Ici, `sleep` tourne activement en arrière-plan, _sans_ être suspendu.
Il est temps de s'entraîner !
Lancer `/challenge/run` en arrière-plan pour obtenir le flag !
