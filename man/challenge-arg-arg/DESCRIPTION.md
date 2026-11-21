Si l'utilisation de la plupart des commandes est simple, celle de certaines peut devenir très complexe.
Par exemple, les arguments de commandes comme `sed` et `awk`, que nous n'aborderons pas maintenant, sont de véritables programmes écrits dans un langage de programmation ésotérique !
Entre `cd` et `awk`, il existe des commandes dont les arguments prennent eux-mêmes des arguments...

Cela semble fou, mais on l'a déjà rencontré avec le niveau `find` du module [Commandes de base](https://pwn.college/linux-luminarium-fr/commands).
`find` possède un argument `-name`, et cet argument prend lui-même un argument, le nom à rechercher.
De nombreuses autres commandes fonctionnent de la même manière.

Voici la documentation de `/challenge/challenge` pour ce niveau :

> Welcome to the documentation for `/challenge/challenge`!
> This program prints arbitrary files to the terminal when given the `--printfile` argument.
> The argument to `--printfile` is the path of the file to read.
> For example, `/challenge/challenge --printfile /etc/hostname` will print the container's hostname!

Muni de cette documentation, il faut obtenir le flag !
