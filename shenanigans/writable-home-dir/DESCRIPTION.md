Zardus est devenu prudent : pourquoi, d'ailleurs, aurait-il un `.bashrc` accessible en écriture ?
Mais un scénario plus courant est celui d'utilisateurs d'un même système qui, pour faciliter la collaboration, rendent leurs répertoires personnels _accessibles en écriture à tous_.
Quel est le problème ?

Le problème tient à une subtilité des droits sur les fichiers et les répertoires Linux : toute personne qui a un accès en écriture à un répertoire peut _déplacer_ et _supprimer_ les fichiers qu'il contient.
Par exemple, supposons que Zardus ait un répertoire accessible en écriture à tous pour collaborer :

```console
zardus@dojo:~$ mkdir /tmp/collab
zardus@dojo:~$ chmod a+w /tmp/collab
zardus@dojo:~$ echo "do pwn.college" > /tmp/collab/todo-list
```

Puis un pirate arrive et fait ceci, _alors qu'il ne possède pas le fichier todo-list_ !

```console
hacker@dojo:~$ ls -l /tmp/collab/todo-list
-rw-r--r-- 1 zardus zardus 15 Jun  6 13:12 /tmp/collab/todo-list
hacker@dojo:~$ rm /tmp/collab/todo-list
rm: remove write-protected regular file '/tmp/collab/todo-list'? y
hacker@dojo:~$ echo "send hacker money" > /tmp/collab/todo-list
hacker@dojo:~$ ls -l /tmp/collab/todo-list
-rw-r--r-- 1 hacker hacker 18 Jun  6 13:12 /tmp/collab/todo-list
hacker@dojo:~$
```

Cela peut sembler contre-intuitif : `hacker` n'a pas d'accès en écriture au fichier `todo-list`, mais le résultat est qu'il peut en modifier le contenu.
Pensez-y ainsi : le lien d'un fichier avec un répertoire se trouve finalement dans le répertoire lui-même, et les utilisateurs qui ont un accès en écriture à ce répertoire peuvent le manipuler.
Bien sûr, cela a des conséquences de sécurité lorsque des répertoires importants sont accessibles en écriture à tous.

Dans ce défi, pour plus de commodité, Zardus a ouvert son répertoire personnel :

```console
zardus@dojo:~$ chmod a+w /home/zardus
```

Vous le savez, ce répertoire contient de nombreux fichiers sensibles, _comme `.bashrc`_ !
Pouvez-vous reproduire l'attaque précédente, avec un accès en écriture à `/home/zardus` plutôt qu'à `/home/zardus/.bashrc` ?
