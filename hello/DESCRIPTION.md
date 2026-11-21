Ce module présente les bases de l'interaction avec la ligne de commande !
La _ligne de commande_ permet d'exécuter des _commandes_.
Lorsqu'on ouvre un terminal, il lance un « shell » en ligne de commande, qui ressemble à ceci :

```console
hacker@dojo:~$
```

Cette invite s'appelle le « prompt » : elle attend qu'on saisisse une commande.
Voyons ce qui se passe ici :

- Le `hacker` du prompt est le _nom d'utilisateur_ de l'utilisateur courant.
  Dans l'environnement du dojo de pwn.college, il s'appelle « hacker ».
- Dans l'exemple ci-dessus, la partie `dojo` du prompt est le _nom d'hôte_ de la machine sur laquelle tourne le shell (cette précision peut servir à un administrateur système qui gère chaque jour de nombreuses machines, par exemple).
  Ici, le nom d'hôte est `dojo`, mais dans pwn.college, il est dérivé du nom du défi en cours.
- Nous verrons plus tard ce que signifie `~` :-)
- Le `$` à la fin du prompt indique que `hacker` n'est pas un utilisateur administrateur.
  Bien plus tard dans pwn.college, lorsqu'on apprend à utiliser des exploits pour devenir administrateur, le prompt affiche `#` au lieu de `$` : on sait alors qu'on a gagné !

Bref, l'invite attend la commande suivante.
Passer au premier défi pour apprendre à exécuter réellement des commandes !
