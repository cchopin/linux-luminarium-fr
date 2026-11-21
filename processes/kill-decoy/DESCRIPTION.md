Il arrive que des processus qui se comportent mal gênent le travail.
Ces processus doivent parfois être supprimés...

Dans ce défi, un processus leurre monopolise une ressource essentielle : un tube nommé (FIFO) situé à `/tmp/flag_fifo`, dans lequel `/challenge/run` veut écrire le flag (comme dans le défi FIFO de [Pratiquer les tubes et les redirections](https://pwn.college/linux-luminarium-fr/piping)).
Il faut `kill` ce processus.

La marche générale est la suivante :

1. Vérifier les processus en cours.
2. Repérer `/challenge/decoy` dans la liste et trouver son identifiant de processus.
3. Le `kill`.
4. Lancer `/challenge/run` pour obtenir le flag, sans être submergé par les leurres (il n'est pas nécessaire de rediriger sa sortie : il écrit seul dans le FIFO).

Bonne chance !

----
**Note :**
Quelques faux flags peuvent encore apparaître après la suppression du processus leurre.
Cela tient au fait que les tubes Linux sont _tamponnés_ : conceptuellement, ils ont une sorte de longueur à travers laquelle circulent les données, et l'on peut supprimer le leurre alors que des données sont encore dans le tube.
Ces données, déjà entrées dans le tube, arrivent jusqu'à l'autre extrémité (le `cat`).
Si l'on attend une seconde, les leurres cessent d'apparaître, et l'on peut alors lancer `/challenge/run` et gagner !
