Il arrive qu'on veuille récupérer des colonnes précises de données, comme la première colonne, la troisième, ou la quarante-deuxième.
Pour cela, il existe la commande `cut`.

Imaginons par exemple le fichier de données suivant :

```console
hacker@dojo:~$ cat scores.txt
hacker 78 99 67
root 92 43 89
hacker@dojo:~$
```

On peut utiliser `cut` pour extraire des colonnes précises :

```console
hacker@dojo:~$ cut -d " " -f 1 scores.txt
hacker
root
hacker@dojo:~$ cut -d " " -f 2 scores.txt
78
92
hacker@dojo:~$ cut -d " " -f 3 scores.txt
99
43
hacker@dojo:~$
```

L'argument `-d` indique le _délimiteur_ des colonnes (le caractère qui les sépare).
Ici, c'est un espace. Il doit être entre guillemets, pour que le shell sache que cet espace fait partie de l'argument et non qu'il sépare des arguments !
L'argument `-f` indique le _numéro de champ_ (la colonne à extraire).

Dans ce défi, le programme `/challenge/run` donne plusieurs lignes contenant des nombres aléatoires et des caractères isolés (les caractères du flag) comme colonnes.
Il faut utiliser `cut` pour extraire les caractères du flag, puis les envoyer vers `tr -d "\n"` (comme dans le niveau précédent !) pour les réunir sur une seule ligne.
La solution ressemblera à `/challenge/run | cut ??? | tr ???`, où les `???` restent à compléter.
