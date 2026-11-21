Quand on envoie des données d'une commande vers une autre par un tube, on ne les voit évidemment plus à l'écran.
Ce n'est pas toujours souhaitable : on peut vouloir observer les données qui circulent entre les commandes pour comprendre un résultat inattendu (par exemple « pourquoi cette deuxième commande ne fonctionne-t-elle pas ? »).

Heureusement, il existe une solution !
La commande `tee`, dont le nom vient d'un « té » de plomberie qui divise un tuyau, duplique les données qui traversent un tube vers autant de fichiers que l'on indique sur la ligne de commande.
Par exemple :

```console
hacker@dojo:~$ echo hi | tee pwn college
hi
hacker@dojo:~$ cat pwn
hi
hacker@dojo:~$ cat college
hi
hacker@dojo:~$
```

Comme on a fourni deux fichiers à `tee`, on obtient trois copies des données reçues : une sur la sortie standard, une dans le fichier `pwn`, et une dans le fichier `college`.
On peut imaginer s'en servir pour déboguer un enchaînement qui dérape :

```console
hacker@dojo:~$ command_1 | command_2
Command 2 failed!
hacker@dojo:~$ command_1 | tee cmd1_output | command_2
Command 2 failed!
hacker@dojo:~$ cat cmd1_output
Command 1 failed: must pass --succeed!
hacker@dojo:~$ command_1 --succeed | command_2
Commands succeeded!
```

Il est temps d'essayer ! Ici, il faut faire passer la sortie de `/challenge/pwn` vers `/challenge/college`, mais il faut d'abord intercepter les données pour voir ce dont `pwn` a besoin.
Utiliser `tee` pour dupliquer la première tentative dans un fichier, examiner la sortie enregistrée, puis relancer l'enchaînement avec ce qu'on a appris.
