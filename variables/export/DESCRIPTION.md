Par défaut, les variables qu'on définit dans une session de shell sont locales à ce processus shell.
Autrement dit, les autres commandes lancées ne les héritent pas.
On peut le vérifier en lançant simplement un autre processus shell depuis le sien :

```console
hacker@dojo:~$ VAR=1337
hacker@dojo:~$ echo "VAR is: $VAR"
VAR is: 1337
hacker@dojo:~$ sh
$ echo "VAR is: $VAR"
VAR is: 
```

Dans la sortie ci-dessus, l'invite `$` est celle de `sh`, une implémentation minimale de shell, lancée comme _processus fils_ du shell principal.
Et elle ne reçoit pas la variable `VAR` !

C'est logique, bien sûr.
Les variables du shell peuvent contenir des données sensibles ou inattendues, et l'on ne souhaite pas qu'elles fuient vers les autres programmes lancés, sauf si c'est explicitement voulu.
Comment indiquer qu'une variable doit être transmise ?
On l'*exporte*.
Une fois exportées, les variables sont transmises aux *variables d'environnement* des processus fils.
On rencontrera le concept de variable d'environnement dans d'autres défis, mais on en observera déjà les effets ici.
Voici un exemple :

```console
hacker@dojo:~$ VAR=1337
hacker@dojo:~$ export VAR
hacker@dojo:~$ sh
$ echo "VAR is: $VAR"
VAR is: 1337
```

Ici, le shell fils a reçu la valeur de `VAR` et a pu l'afficher !
On peut aussi combiner les deux premières lignes.

```console
hacker@dojo:~$ export VAR=1337
hacker@dojo:~$ sh
$ echo "VAR is: $VAR"
VAR is: 1337
```

Dans ce défi, il faut lancer `/challenge/run` avec la variable `PWN` exportée et valant `COLLEGE`, et la variable `COLLEGE` valant `PWN` mais _non_ exportée (c'est-à-dire non héritée par `/challenge/run`).
Bonne chance !
