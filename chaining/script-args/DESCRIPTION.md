On sait déjà écrire des scripts shell, mais jusqu'ici ce ne sont que des listes de commandes.
Les scripts gagnent beaucoup en puissance lorsqu'ils acceptent des arguments !
Cela peut ressembler à ceci :

```console
hacker@dojo:~$ bash myscript.sh hello world
```

Le script accède à ces arguments grâce à des variables spéciales :
- `$1` contient le premier argument (« hello »)
- `$2` contient le deuxième argument (« world »)
- `$3` contiendrait le troisième argument (s'il y en avait un)
- ...et ainsi de suite

Voici un exemple simple :
```bash
hacker@dojo:~$ cat myscript.sh
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
hacker@dojo:~$ bash myscript.sh hello world
First argument: hello
Second argument: world
hacker@dojo:~$
```

Dans ce défi, il faut écrire un script `/home/hacker/solve.sh` qui :
1. Prend deux arguments
2. Les affiche dans l'ordre INVERSE (le deuxième argument d'abord, puis le premier)

Par exemple :
```console
hacker@dojo:~$ bash /home/hacker/solve.sh pwn college
college pwn
hacker@dojo:~$
```

Une fois le script fonctionnel, il ne reste plus qu'à lancer `/challenge/run` pour obtenir le flag !
