Chaque commande du shell, y compris chaque programme et chaque commande interne, se termine avec un _code de retour_ à la fin de son exécution.
Le shell, ou l'utilisateur du shell (c'est-à-dire nous !), peut s'en servir pour vérifier si le processus a réussi ce qu'il devait faire (ce jugement dépend bien sûr de ce que le processus est censé faire).

On accède au code de retour de la dernière commande terminée avec la variable spéciale `?` (ne pas oublier le `$` pour en lire la valeur !) :

```console
hacker@dojo:~$ touch test-file
hacker@dojo:~$ echo $?
0
hacker@dojo:~$ touch /test-file
touch: cannot touch '/test-file': Permission denied
hacker@dojo:~$ echo $?
1
hacker@dojo:~$
```

Comme on le voit, les commandes qui réussissent renvoient en général `0`, et celles qui échouent renvoient une valeur non nulle, le plus souvent `1`, mais parfois un code d'erreur qui identifie un mode d'échec précis.

Dans ce défi, il faut récupérer le code de retour renvoyé par `/challenge/get-code`, puis lancer `/challenge/submit-code` avec ce code d'erreur en argument.
Bonne chance !
