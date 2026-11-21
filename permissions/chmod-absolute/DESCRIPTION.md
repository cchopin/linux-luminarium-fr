En plus d'ajouter et de retirer des permissions, comme dans le niveau précédent, `chmod` peut aussi définir directement l'ensemble des permissions, en remplaçant les anciennes.
Cela se fait avec `=` au lieu de `-` ou `+`.
Par exemple :

- `u=rw` donne les droits de lecture et d'écriture à l'utilisateur, et supprime le droit d'exécution ;
- `o=x` ne donne que le droit d'exécution aux autres, en supprimant la lecture et l'écriture ;
- `a=rwx` donne les droits de lecture, d'écriture et d'exécution à l'utilisateur, au groupe et aux autres !

Mais que faire si l'on veut définir les permissions de l'utilisateur différemment de celles du groupe ?
Par exemple, `rw` pour le propriétaire, mais seulement `r` pour le groupe propriétaire ?
On y parvient en enchaînant plusieurs modes dans `chmod`, séparés par des `,` !

- `chmod u=rw,g=r /challenge/pwn` donne à l'utilisateur les droits de lecture et d'écriture, et au groupe le seul droit de lecture ;
- `chmod a=r,u=rw /challenge/pwn` donne à l'utilisateur les droits de lecture et d'écriture, et au groupe et aux autres le seul droit de lecture.

On peut aussi remettre des permissions à zéro avec `-` :

- `chmod u=rw,g=r,o=- /challenge/pwn` donne à l'utilisateur les droits de lecture et d'écriture, au groupe le seul droit de lecture, et ne laisse aucun droit aux autres.

Il faut garder à l'esprit que le `-` placé après `=` n'a pas le même sens que s'il suivait directement `u`, `g` ou `o` (dans ce cas, il retirerait seulement certains bits, et non tout).

Ce niveau pousse plus loin le précédent, en demandant des modifications plus radicales des permissions, qui nécessitent les `=` et l'enchaînement avec `,`.
Bonne chance !
