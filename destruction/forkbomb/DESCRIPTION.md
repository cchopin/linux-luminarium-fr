Comme vous l'avez appris dans le module [Processus et tâches](https://pwn.college/linux-luminarium-fr/processes), chaque fois que vous lancez un programme, le système d'exploitation Linux crée un nouveau processus.
Si l'on crée des processus plus vite que le noyau ne peut les gérer, la table des processus se remplit, et _tout_ se bloque.
Ce nouveau processus (par exemple celui d'une invocation de `ls`) est « bifurqué » (forked) à partir d'un processus parent (par exemple une instance du shell).
D'où le nom de « bombe fork » donné à cette explosion de processus.

Vous disposez des outils nécessaires :

- écrire un petit script (comme dans le module [Chaîner les commandes](https://pwn.college/linux-luminarium-fr/chaining)) ;
- le rendre exécutable (comme dans le module [Perception des droits](https://pwn.college/linux-luminarium-fr/permissions)) ;
- lui faire lancer une copie de lui-même en arrière-plan (comme dans le module [Processus et tâches](https://pwn.college/linux-luminarium-fr/processes)) ;
- puis lancer _une autre_ copie de lui-même en arrière-plan !

Chaque copie en lancera deux autres, et chacune de celles-ci en lancera encore deux, et vous inonderez le système de tant de processus que les nouveaux ne pourront plus démarrer !

Ce défi contient un `/challenge/check` qui tente de déterminer si votre bombe fork fonctionne (c'est-à-dire s'il ne peut plus lancer de nouveaux processus), et vous donne le flag le cas échéant.
Pensez à le lancer (dans un autre terminal) _avant_ votre attaque, sinon vous ne pourrez plus rien lancer !

----
**NOTE :**
Inutile de le dire : votre environnement deviendra inutilisable.
Il suffit de redémarrer le défi (ou d'en lancer un autre) pour retrouver un environnement utilisable !
