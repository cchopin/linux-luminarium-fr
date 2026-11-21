On commence par lire une saisie de l'utilisateur.
Cela se fait avec la commande interne `read`, qui *lit* une saisie et la place dans une variable !

Voici un exemple avec l'option `-p`, qui permet d'indiquer une invite (sans elle, il serait difficile de distinguer la saisie de la sortie dans l'exemple ci-dessous) :

```console
hacker@dojo:~$ read -p "INPUT: " MY_VARIABLE
INPUT: Hello!
hacker@dojo:~$ echo "You entered: $MY_VARIABLE"
You entered: Hello!
```

Gardons à l'esprit que `read` lit les données de l'entrée standard !
Le premier `Hello!`, ci-dessus, a été _saisi_ et non _affiché_.
Rendons cela plus explicite : ici, chaque ligne est annotée selon qu'elle représente une `INPUT` (saisie de l'utilisateur) ou une `OUTPUT` (sortie vers l'utilisateur) :

```console
 INPUT: hacker@dojo:~$ echo $MY_VARIABLE
OUTPUT:
 INPUT: hacker@dojo:~$ read MY_VARIABLE
 INPUT: Hello!
 INPUT: hacker@dojo:~$ echo "You entered: $MY_VARIABLE"
OUTPUT: You entered: Hello!
```

Dans ce défi, il faut utiliser `read` pour affecter la valeur `COLLEGE` à la variable `PWN`.
Bonne chance !
