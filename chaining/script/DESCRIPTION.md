À mesure qu'on combine des commandes pour obtenir des effets complexes, la ligne devient vite pénible à manipuler.
Dans ce cas, on peut placer ces commandes dans un fichier, appelé *script shell* (shell script), et l'exécuter.
Par exemple, prenons notre technique du point-virgule :

```console
hacker@dojo:~$ echo COLLEGE > pwn; cat pwn
COLLEGE
hacker@dojo:~$
```

On peut créer un script shell nommé `pwn.sh` (par convention, les scripts shell portent souvent le suffixe `sh`) :

```sh
echo COLLEGE > pwn
cat pwn
```

On l'exécute ensuite en le passant en argument à une nouvelle instance de notre shell (`bash`) !
Lorsqu'un shell est lancé ainsi, il ne prend pas ses commandes de l'utilisateur, mais les lit dans le fichier.

```console
hacker@dojo:~$ ls
hacker@dojo:~$ bash pwn.sh
COLLEGE
hacker@dojo:~$ ls
pwn
hacker@dojo:~$
```

On voit que le script a exécuté les deux commandes, en créant puis en affichant le fichier `pwn`.

Passons à la pratique ! Comme au niveau précédent, il faut exécuter `/challenge/pwn` puis `/challenge/college`, mais cette fois dans un script shell nommé `x.sh`, lancé avec `bash`.

---
**NOTE :** On n'a pas encore parlé de la riche collection d'éditeurs de texte de Linux.
En attendant, on peut utiliser l'application `Text Editor` en mode Bureau (`Applications->Accessories->Text Editor`) ou l'éditeur par défaut de l'espace de travail VSCode.
