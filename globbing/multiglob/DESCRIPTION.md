Jusqu'ici, on a utilisé un motif à la fois, mais on peut faire davantage !
Bash permet de développer plusieurs motifs dans un même mot.
Par exemple :

```console
hacker@dojo:~$ cat /*fl*
pwn.college{YEAH}
hacker@dojo:~$
```

Ce qui se passe ci-dessus : le shell cherche tous les fichiers de `/` dont le nom commence par n'importe quoi (y compris rien), contient un `f` puis un `l`, et se termine par n'importe quoi (y compris `ag`, ce qui donne `flag`).

À nous de jouer.
Plusieurs fichiers aux noms variés se trouvent dans `/challenge/files`.
Se placer dans ce répertoire avec `cd` et lancer `/challenge/run` avec un seul argument : un mot globbé court (trois caractères au maximum), contenant deux motifs `*`, qui couvre tous les mots contenant la lettre `p`.
