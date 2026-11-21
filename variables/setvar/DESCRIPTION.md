En plus de lire les valeurs stockées dans des variables, on peut aussi écrire des valeurs dans des variables.
Cela se fait, comme dans beaucoup d'autres langages, avec `=`.
Pour affecter la valeur `1337` à la variable `VAR`, on écrit :

```console
hacker@dojo:~$ VAR=1337
```

Il ne faut pas d'espaces autour du `=` !
Si l'on en met (par exemple `VAR = 1337`), le shell ne reconnaît pas une affectation de variable et tente d'exécuter la commande `VAR`, qui n'existe pas.

Notons aussi que l'on écrit `VAR` et non `$VAR` : le `$` ne sert qu'à _accéder_ aux variables.
En termes de shell, cet ajout du `$` déclenche ce qu'on appelle l'*expansion de variable*, qui est, de manière surprenante, à l'origine de nombreuses vulnérabilités potentielles (si cela intéresse, le dojo Art of the Shell est une bonne suite une fois à l'aise avec la ligne de commande !).

Après avoir défini des variables, on peut y accéder avec les techniques vues précédemment, par exemple :

```console
hacker@dojo:~$ echo $VAR
1337
```

Pour résoudre ce niveau, il faut affecter la valeur `COLLEGE` à la variable `PWN`.
Attention : les noms et les valeurs des variables sont sensibles à la casse !
`PWN` n'est pas la même chose que `pwn`, et `COLLEGE` n'est pas la même chose que `College`.
