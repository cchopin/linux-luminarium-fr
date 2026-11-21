Bien sûr, on peut aussi _créer_ des fichiers !
Il existe plusieurs façons de le faire, mais nous verrons ici une commande simple.
On crée un fichier vide en le _touchant_ avec la commande `touch` :

```
hacker@dojo:~$ cd /tmp
hacker@dojo:/tmp$ ls
hacker@dojo:/tmp$ touch pwnfile
hacker@dojo:/tmp$ ls
pwnfile
hacker@dojo:/tmp$
```

C'est aussi simple que cela !
Dans ce niveau, il faut créer deux fichiers : `/tmp/pwn` et `/tmp/college`, puis lancer `/challenge/run` pour obtenir le flag !
