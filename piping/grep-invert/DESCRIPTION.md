La commande `grep` possède une option très pratique : `-v` (inversion de la correspondance).
Alors que `grep` simple affiche les lignes qui CORRESPONDENT à un motif, `grep -v` affiche les lignes qui NE correspondent PAS à ce motif :

```console
hacker@dojo:~$ cat data.txt
hello hackers!
hello world!
hacker@dojo:~$ cat data.txt | grep -v world
hello hackers!
hacker@dojo:~$
```

Parfois, le seul moyen de ne garder que les données voulues consiste à retirer les données que l'on ne veut pas.
Dans ce défi, `/challenge/run` affiche le flag sur la sortie standard, mais il affiche aussi plus de 1000 faux flags (contenant le mot `DECOY` quelque part), mêlés au vrai flag.
Il faut retirer les faux flags tout en conservant le vrai !

Utiliser `grep -v` pour filtrer toutes les lignes contenant « DECOY » et révéler le vrai flag !
