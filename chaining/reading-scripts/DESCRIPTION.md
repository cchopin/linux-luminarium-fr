On n'est pas le seul à écrire des scripts shell !
Ils sont très pratiques pour les tâches simples « au niveau du système », et les développeurs comme les administrateurs système y recourent couramment.
En fait, une part étonnante des programmes présents sur une machine Linux typique sont des scripts shell.

Dans ce niveau, on apprend à lire des scripts shell.
`/challenge/run` est un script shell qui demande un mot de passe secret, mais ce mot de passe est écrit en dur dans le script lui-même !
Il faut lire le script (avec `cat`, par exemple), trouver le mot de passe et obtenir le flag !

----
**NOTE :**
Il est tout à fait possible de lire le code des autres défis.
Lire du code est une stratégie essentielle pour apprendre de nouvelles compétences : on voit comment une fonctionnalité a été implémentée, et on peut réutiliser ces techniques dans ses propres scripts.
Attention cependant : certains fichiers de programme sont du code machine, illisible pour un humain. La commande `file` permet de les distinguer, mais presque tous les défis de Linux Luminarium sont des scripts shell et peuvent être affichés sans risque avec `cat`.
