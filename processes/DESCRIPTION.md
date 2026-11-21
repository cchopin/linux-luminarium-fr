Les ordinateurs exécutent des logiciels pour accomplir des tâches.
Dans l'informatique moderne, ces logiciels se répartissent en deux catégories : les _noyaux de système d'exploitation_ (dont on parlera [bien plus tard](https://pwn.college/system-security)) et les _processus_, dont il est question ici.
Au démarrage de Linux, un processus _init_ (abréviation d'initialisation) est lancé. Il lance à son tour d'autres processus, qui en lancent d'autres, jusqu'à ce qu'on se retrouve devant son shell en ligne de commande, lui-même un processus !
Le shell, bien sûr, lance des processus en réponse aux commandes qu'on saisit.

Dans ce module, on apprend à observer et à piloter des processus de plusieurs façons intéressantes !
