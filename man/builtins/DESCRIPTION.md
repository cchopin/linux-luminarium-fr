Certaines commandes ne sont pas des programmes avec une page de manuel ni une option d'aide : elles sont intégrées au shell lui-même.
On les appelle des _commandes internes_ (builtins).
On les utilise comme n'importe quelle commande, mais c'est le shell qui les traite directement, au lieu de lancer un autre programme.
On obtient la liste des commandes internes du shell en exécutant la commande interne `help`, comme ceci :

```console
hacker@dojo:~$ help
```

On peut obtenir l'aide sur une commande interne précise en la passant à `help`.
Prenons une commande interne déjà utilisée plus tôt : `cd` !

```console
hacker@dojo:~$ help cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
    Change the shell working directory.
    
    Change the current directory to DIR.  The default DIR is the value of the
    HOME shell variable.
...
```

Voilà des informations utiles !
Dans ce défi, on s'entraîne à utiliser `help` pour consulter l'aide des commandes internes.
La commande `challenge` de ce défi est une commande interne du shell, et non un programme.
Comme précédemment, il faut consulter son aide pour trouver la valeur secrète à lui transmettre !
