L'un des usages courants de la redirection de sortie consiste à enregistrer des résultats de commandes pour les analyser plus tard.
Souvent, on veut le faire pour plusieurs commandes à la fois : en lancer une série, enregistrer leurs sorties, puis chercher dedans avec `grep`.
Dans ce cas, on voudrait que toutes les sorties s'ajoutent au même fichier, mais `>` crée un nouveau fichier de sortie à chaque fois, en effaçant l'ancien contenu.

On peut rediriger la sortie en mode _ajout_ avec `>>` au lieu de `>`, comme ceci :

```console
hacker@dojo:~$ echo pwn > outfile
hacker@dojo:~$ echo college >> outfile
hacker@dojo:~$ cat outfile
pwn
college
hacker@dojo:$
```

Pour s'entraîner, il faut lancer `/challenge/run` avec une redirection de sortie en mode ajout vers le fichier `/home/hacker/the-flag`.
Le défi écrit la première moitié du flag dans ce fichier, et la seconde moitié sur `stdout` si `stdout` est redirigé vers le fichier.
Si la redirection est faite en mode ajout, la seconde moitié s'ajoute à la première. Si elle est faite en mode troncature (`>`), la seconde moitié _écrase_ la première et le flag n'est pas obtenu !

Il est temps de s'y mettre !
