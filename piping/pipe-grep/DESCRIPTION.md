On peut « court-circuiter l'intermédiaire » et éviter d'enregistrer les résultats dans un fichier, comme dans le niveau précédent.
Pour cela, on utilise l'opérateur `|` (le tube, ou _pipe_).
La sortie standard de la commande située à gauche du tube est reliée (on dit _envoyée dans_) à l'entrée standard de la commande située à droite.
Par exemple :

```
hacker@dojo:~$ echo no-no | grep yes
hacker@dojo:~$ echo yes-yes | grep yes
yes-yes
hacker@dojo:~$ echo yes-yes | grep no
hacker@dojo:~$ echo no-no | grep no
no-no
```

Essayons maintenant par soi-même ! `/challenge/run` affiche cent mille lignes de texte, dont le flag.
Chercher le flag avec `grep` !
