Comme pour la sortie standard, on peut aussi rediriger le canal d'erreur des commandes.
Ici, on découvre les *numéros de descripteurs de fichier* (File Descriptor numbers).
Un descripteur de fichier (FD) est un numéro qui _désigne_ un canal de communication sous Linux.
On les utilise déjà depuis le début, sans s'en rendre compte.
Trois sont familiers :

- FD 0 : entrée standard
- FD 1 : sortie standard
- FD 2 : erreur standard

Lorsqu'on redirige une communication de processus, on le fait par numéro de descripteur, même si certains numéros sont implicites.
Par exemple, un `>` sans numéro équivaut à `1>`, qui redirige le FD 1 (sortie standard).
Les deux commandes suivantes sont donc équivalentes :

```console
hacker@dojo:~$ echo hi > asdf
hacker@dojo:~$ echo hi 1> asdf
```

Rediriger les erreurs est assez simple à partir de là.
Si une commande peut produire des données sur l'erreur standard (comme `/challenge/run`), on peut écrire :

```console
hacker@dojo:~$ /challenge/run 2> errors.log
```

Cela redirige l'erreur standard (FD 2) vers le fichier `errors.log`.
On peut aussi rediriger plusieurs descripteurs en même temps.
Par exemple :

```console
hacker@dojo:~$ some_command > output.log 2> errors.log
```

Cette commande envoie la sortie vers `output.log` et les erreurs vers `errors.log`.

Passons à la pratique !
Dans ce défi, il faut rediriger la sortie de `/challenge/run`, comme précédemment, vers `myflag`, et les « erreurs » (ici, les instructions) vers `instructions`.
Rien ne s'affiche dans le terminal, puisque tout a été redirigé !
Les instructions et les retours se trouvent dans `instructions`, et le flag dans `myflag`, une fois le défi réussi.

----
**Attention :** si une expérience précédente a laissé un fichier, un répertoire ou un lien symbolique nommé `myflag` ou `instructions` dans le répertoire courant, il faut d'abord le supprimer, pour que le shell puisse y créer des fichiers normaux accessibles en écriture.
