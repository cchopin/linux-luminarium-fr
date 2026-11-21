Un des buts du transfert de données par tubes est de les _modifier_.
De nombreuses commandes Linux permettent de modifier les données de façons très intéressantes.
L'une d'elles est `tr`, qui _tr_aduit les caractères reçus sur l'entrée standard et les affiche sur la sortie standard.

Dans son usage le plus simple, `tr` remplace le caractère donné en premier argument par le caractère donné en second argument :

```console
hacker@dojo:~$ echo OWN | tr O P
PWN
hacker@dojo:~$
```

Il peut aussi traiter plusieurs caractères : chaque caractère de la première chaîne est remplacé par le caractère situé à la même position dans la seconde.

```console
hacker@dojo:~$ echo PWM.COLLAGE | tr MA NE
PWN.COLLEGE
hacker@dojo:~$
```

Essayons maintenant !
Dans ce niveau, `/challenge/run` affiche le flag, mais en inversant la casse de tous les caractères (par exemple `A` devient `a` et inversement).
Peut-on annuler cette transformation avec `tr` et obtenir le flag ?
