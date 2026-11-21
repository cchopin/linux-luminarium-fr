On a découvert les codes de retour dans le module [Processus](https://pwn.college/linux-luminarium-fr/processes/).
Utilisons-les maintenant pour enchaîner des commandes !

L'opérateur `&&` permet d'exécuter une seconde commande seulement si la première réussit (selon la convention Linux, cela signifie qu'elle s'est terminée avec le code 0).
On parle d'opérateur « ET » parce que les deux conditions doivent être vraies : la première commande doit réussir, ET alors la seconde s'exécute.
C'est très utile pour les enchaînements complexes, où certaines actions dépendent du succès d'autres actions.

Voici la syntaxe :
```console
hacker@dojo:~$ command1 && command2
```

Cela signifie : « Exécuter command1, et SI elle réussit, exécuter command2. »

Quelques exemples :

```console
hacker@dojo:~$ touch /home/hacker/file && echo "this will run"
success
this will run
hacker@dojo:~$ touch /file && echo "this will NOT run"
touch: cannot touch '/file': Permission denied
hacker@dojo:~$
```

Le second appel à `touch` échoue parce que l'utilisateur hacker n'a pas le droit d'écriture sur `/file` : le `echo` ne s'exécute donc pas.

Dans ce défi, il faut enchaîner les programmes `/challenge/first-success` et `/challenge/second` avec l'opérateur `&&`.
Il est conseillé d'essayer d'abord chaque commande séparément, pour voir ce qui se passe (on n'obtient *pas* le flag).
Mais si on les enchaîne avec `&&`, le flag apparaît !
