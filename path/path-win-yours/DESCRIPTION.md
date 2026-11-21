Rappelons notre exemple du niveau précédent :

```console
hacker@dojo:~$ ls /home/hacker/scripts
goodscript	badscript	okayscript
hacker@dojo:~$ PATH=/home/hacker/scripts
hacker@dojo:~$ goodscript
YEAH! This is the best script!
hacker@dojo:~$
```

Ce que l'on voit ici, bien sûr, c'est `hacker` qui rend son shell plus utile en y apportant ses propres commandes.
Avec le temps, on finit par accumuler ses propres outils, bien pensés.
Commençons par `win` !

Auparavant, la commande `win` que `/challenge/run` exécutait était stockée dans `/challenge/more_commands`.
Cette fois, `win` n'existe pas !
Rappelons-nous la dernière étape de [Chaîner les commandes](https://pwn.college/linux-luminarium-fr/chaining) : il faut créer un script shell appelé `win`, ajouter son emplacement à `PATH`, et permettre à `/challenge/run` de le trouver !

----
**Indice :**
`/challenge/run` s'exécute en tant que `root` et appelle `win`. Ainsi, `win` peut simplement afficher le fichier du flag avec `cat`.
Là encore, la commande `win` est la _seule_ chose dont `/challenge/run` a besoin : on peut donc remplacer `PATH` par ce seul répertoire.
Mais attention : dans ce cas, votre commande `win` ne trouvera plus `cat`.

Il existe trois façons d'éviter ce problème :

1. Trouver où se trouve le programme `cat` dans le système de fichiers. Il _doit_ se trouver dans un répertoire de `PATH`. Affichez donc la variable (voir [Variables du shell](https://pwn.college/linux-luminarium-fr/variables) pour savoir comment faire), parcourez ses répertoires (rappelez-vous que les entrées sont séparées par `:`), repérez celui qui contient `cat`, et appelez `cat` par son chemin absolu.
2. Définir un `PATH` qui contient les anciens répertoires _plus_ une nouvelle entrée pour l'endroit où vous créez `win`.
3. Utiliser `read` (voir encore [Variables du shell](https://pwn.college/linux-luminarium-fr/variables)) pour lire `/flag`. Comme `read` est une primitive de `bash`, elle n'est pas affectée par les manipulations de `PATH`.

Il ne reste plus qu'à lancer `win` !
