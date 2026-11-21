Dans les niveaux précédents, on a pu remarquer que l'utilisateur `hacker` appartient au groupe `hacker`, et que `zardus` appartient au groupe `zardus`.
Il existe une convention sous Linux, selon laquelle chaque utilisateur a son propre groupe, mais ce n'est pas une obligation.
Par exemple, de nombreux laboratoires informatiques placent tous leurs utilisateurs dans un seul groupe partagé, `users`.

Le point est le suivant : on a utilisé le groupe `hacker` jusqu'ici, mais dans ce niveau, cela ne fonctionnera pas.
La commande `chgrp` reste autorisée, mais le nom du groupe de l'utilisateur a été rendu aléatoire.
Il faut donc utiliser la commande `id` pour découvrir ce nom, puis `chgrp` pour gagner !
