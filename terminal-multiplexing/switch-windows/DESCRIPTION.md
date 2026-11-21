Jusqu'ici, `screen` ressemble à un drôle de terminal dans un terminal.
Mais il peut faire bien plus !

Au sein d'une même session screen, on peut avoir plusieurs fenêtres, comme un navigateur a plusieurs onglets.
C'est très pratique pour organiser différentes tâches !

Ces fenêtres se gèrent avec différents raccourcis clavier, tous commençant par `Ctrl-A` :

- `Ctrl-A c` : créer une nouvelle fenêtre
- `Ctrl-A n` : fenêtre suivante
- `Ctrl-A p` : fenêtre précédente
- `Ctrl-A 0` à `Ctrl-A 9` : aller directement à la fenêtre 0 à 9
- `Ctrl-A "` : afficher un menu de sélection de toutes les fenêtres

Pour ce défi, une session screen a été préparée avec deux fenêtres :

- La fenêtre 0 contient… il faudra y aller pour le savoir !
- La fenêtre 1 contient un message de bienvenue

Se rattacher à la session avec `screen -r`, puis utiliser l'une des combinaisons ci-dessus pour passer à la fenêtre 1.
Il ne reste plus qu'à récupérer le flag !
