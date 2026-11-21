La façon la plus simple d'enchaîner des commandes est d'utiliser `;`.
Dans la plupart des contextes, `;` sépare les commandes comme la touche Entrée sépare les lignes.
Ainsi, ceci :

```console
hacker@dojo:~$ echo COLLEGE > pwn
hacker@dojo:~$ cat pwn
COLLEGE
hacker@dojo:~$
```

revient à peu près à ceci :

```console
hacker@dojo:~$ echo COLLEGE > pwn; cat pwn
COLLEGE
hacker@dojo:~$
```

En gros, quand on appuie sur Entrée, le shell exécute la commande tapée puis, une fois celle-ci terminée, affiche à nouveau l'invite pour une autre commande.
Le point-virgule fonctionne de la même façon, sans l'invite intermédiaire : on tape les deux commandes avant que quoi que ce soit ne soit exécuté.

À essayer maintenant ! Dans ce niveau, il faut exécuter `/challenge/pwn`, puis `/challenge/college`, en les enchaînant avec un point-virgule.
