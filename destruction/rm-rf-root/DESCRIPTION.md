Vous voulez effacer l'ardoise et tout recommencer ?
Vous le pouvez !

```console
hacker@dojo:~$ ls /
bin etc blah blah blah
hacker@dojo:~$ rm -rf /
hacker@dojo:~$ ls /
bash: ls: command not found
hacker@dojo:~$
```

Que s'est-il passé ?
Comme vous le savez, `rm` supprime des fichiers.
L'option `-r` (récursif) supprime les répertoires ainsi que tous les fichiers qu'ils contiennent.
L'option `-f` (force) ignore les erreurs rencontrées par la commande `rm`, ainsi que les demandes de confirmation qu'elle pourrait faire.
Combinées et dirigées vers `/`, les conséquences sont catastrophiques : l'effacement complet de votre système.
Sur un système moderne, les choses ne sont pas _aussi_ simples, mais vous le constaterez par vous-même.

Dans ce défi, vous allez faire quelque chose que vous ne ferez peut-être jamais plus : effacer tout le système.
Nous avons légèrement modifié les choses pour protéger votre répertoire personnel (normalement, il serait lui aussi effacé !), mais pour le reste, il ne vous reste devant vous, et entre vous et le flag, que votre volonté d'effacer le disque.
Avant de tout effacer, pensez à lancer `/challenge/check` pour qu'il assiste au feu d'artifice (et vous donne le flag) !

----
**NOTE :**
La commande `rm` prendra du temps.
Il y a beaucoup à supprimer !

**NOTE :**
Pour diverses raisons techniques, vous ne pourrez probablement pas tout supprimer, y compris avec la technique qui protège votre répertoire personnel dans ce niveau.
Ne vous inquiétez pas, vous causerez assez de dégâts comme ça !
