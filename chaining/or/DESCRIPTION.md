On vient de voir l'opérateur `&&`, qui exécute la seconde commande seulement si la première réussit.
Voyons maintenant son contraire : l'opérateur `||` permet d'exécuter une seconde commande seulement si la première échoue (se termine avec un code différent de zéro).
On parle d'opérateur « OU » parce que l'une des deux commandes doit réussir, OU sinon la seconde s'exécute.

Voici la syntaxe :
```console
hacker@dojo:~$ command1 || command2
```

Cela signifie : « Exécuter command1, et SI elle échoue, exécuter command2. »

Quelques exemples :
```console
hacker@dojo:~$ touch /file || echo "touch failed, so this runs"
touch: cannot touch '/file': Permission denied
touch failed, so this runs
hacker@dojo:~$ touch /home/hacker/file || echo "this will NOT run"
hacker@dojo:~$
```

L'opérateur `||` est très pratique pour prévoir une commande de repli ou pour gérer les erreurs !

Dans ce défi, il faut enchaîner `/challenge/first-failure` et `/challenge/second` avec l'opérateur `||`.
Il ne reste plus qu'à lancer les commandes !
