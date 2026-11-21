On sait rediriger les erreurs vers un fichier, et on sait envoyer une sortie vers un autre programme comme `grep`.
Mais comment chercher directement dans les erreurs ?

L'opérateur `>` redirige un descripteur donné vers un fichier, et l'on a utilisé `2>` pour rediriger le FD 2, c'est-à-dire l'erreur standard.
L'opérateur `|` ne redirige _que la sortie standard_ vers un autre programme, et il n'existe pas de forme `2|` !
Il ne peut envoyer que la sortie standard (descripteur de fichier 1).

Heureusement, là où il y a un shell, il y a un moyen !
Le shell possède l'opérateur `>&`, qui redirige un descripteur de fichier _vers un autre descripteur_.
On peut donc procéder en deux étapes pour chercher dans les erreurs : d'abord rediriger l'erreur standard vers la sortie standard (`2>& 1`), puis envoyer le flux combiné dans un tube (`|`) comme d'habitude !

Essayons !
Comme pour le niveau précédent, ce défi produit une grande quantité de sortie, cette fois sur l'erreur standard.
Chercher dans ce flux avec `grep` pour trouver le flag !
