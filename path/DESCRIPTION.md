Jusqu'ici, on a lancé des commandes de plusieurs façons :

- par un chemin absolu (par exemple `/challenge/run`) ;
- par un chemin relatif (par exemple `./run`) ;
- par un simple nom de commande (par exemple `ls`).

Les deux premiers cas, le chemin absolu et le chemin relatif, sont simples : le fichier `run` se trouve dans le répertoire `/challenge`, et les deux écritures le désignent, à condition bien sûr que le chemin relatif soit utilisé depuis `/challenge`.
Mais qu'en est-il du dernier cas ?
Où se trouve le programme `ls` ?
Comment le shell sait-il où le chercher ?

Dans ce module, on soulève le voile et on répond à cette question !
Allons-y.
