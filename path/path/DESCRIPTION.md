La réponse à la question « Comment le shell trouve-t-il `ls` ? » est assez simple.
Il existe une variable spéciale du shell, appelée `PATH`, qui contient une liste de chemins de répertoires. Le shell y cherche les programmes correspondant aux commandes.
Si on vide cette variable, les choses tournent mal :

```console
hacker@dojo:~$ ls
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
hacker@dojo:~$ PATH=""
hacker@dojo:~$ ls
bash: ls: No such file or directory
hacker@dojo:~$
```

Sans `PATH`, bash ne trouve plus la commande `ls`.

Dans ce défi, on perturbe le fonctionnement du programme `/challenge/run`.
Ce programme **SUPPRIME** le fichier du flag avec la commande `rm`.
Pourtant, s'il ne trouve pas la commande `rm`, le flag ne sera pas supprimé, et le défi le donnera !
Il faut donc faire en sorte que `/challenge/run` ne trouve pas non plus la commande `rm` !

À noter : si l'on ne réussit pas, et que le flag est supprimé, il faut redémarrer le défi pour recommencer.
