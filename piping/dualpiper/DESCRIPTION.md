Il est maintenant temps d'assembler ce qu'on a appris.
Il faut maîtriser la tâche ultime des tubes : envoyer la sortie standard vers un programme, et l'erreur standard vers un autre.

La difficulté tient à ce que l'opérateur `|` relie la _sortie standard_ de la commande de gauche à l'_entrée standard_ de la commande de droite.
On a bien utilisé `2>&1` pour rediriger l'erreur standard vers la sortie standard, et la faire passer dans le tube, mais cela mélange alors erreur standard et sortie standard.
Comment les garder séparées ?

Il faut combiner ce qu'on sait de `>()`, de `2>` et de `|`.
La manière d'y parvenir est laissée au lecteur.

Dans ce défi, on dispose de :

- `/challenge/hack` : ce programme produit des données sur la _sortie standard_ et sur l'_erreur standard_
- `/challenge/the` : il faut rediriger l'_erreur standard_ de `hack` vers ce programme
- `/challenge/planet` : il faut rediriger la _sortie standard_ de `hack` vers ce programme

Il reste à récupérer le flag !

----
**Bonus :** pour un peu plus de difficulté, trouver une solution qui n'utilise pas `|`.
