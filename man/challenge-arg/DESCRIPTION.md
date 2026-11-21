Le besoin le plus courant de documentation est simplement de savoir utiliser tous ces programmes, et en particulier de savoir quels arguments donner sur la ligne de commande.
Ce module approfondit cette idée, qui sert de point d'appui pour savoir utiliser les programmes en général.
Dans la suite du module, on verra diverses façons de demander de l'aide à l'environnement pour les programmes, mais commençons par la lecture de la documentation.

L'utilisation correcte d'un programme dépend en grande partie de la manière dont on lui spécifie ses arguments.
Rappelons l'option `-a` de `ls -a` dans le défi `hidden files` du module [Commandes de base](https://pwn.college/linux-luminarium-fr/commands) : ce `-a` est un _argument_ qui indique à `ls` de lister les fichiers cachés en plus des autres.
Comme on _voulait_ lister les fichiers cachés, invoquer `ls` avec l'argument `-a` était la bonne façon de l'utiliser dans cette situation.

Le programme de ce défi est `/challenge/challenge`. Il faut l'invoquer correctement pour qu'il donne le flag.
Imaginons que voici sa documentation :

> Welcome to the documentation for `/challenge/challenge`! To properly run this program, you will need to pass it the argument of `--giveflag`. Good luck!

Muni de cette information, il faut obtenir le flag !
