Si l'on utilise Linux (ou un ordinateur) assez longtemps pour un travail sérieux, on finit par rencontrer une situation de ce genre : on veut que deux programmes accèdent aux mêmes données, mais chacun attend ces données à un emplacement différent.
Linux propose une solution à ce dilemme : les _liens_.

Il existe deux sortes de liens : les liens _durs_ et les liens _souples_ (aussi appelés _symboliques_).
Une analogie permet de les distinguer :

- Un lien **dur**, c'est habiter un appartement sous plusieurs adresses qui mènent toutes au même endroit (par exemple `Apt 2` et `Unit 2`).
- Un lien **souple**, c'est déménager et faire réexpédier automatiquement son courrier de l'ancien logement vers le nouveau.

Dans un système de fichiers, un fichier correspond, conceptuellement, à une adresse à laquelle se trouve le contenu du fichier.
Un lien dur est une autre adresse qui désigne ces mêmes données : accéder au lien dur ou au fichier d'origine donne exactement les mêmes données, immédiatement.
Un lien souple (symbolique), en revanche, contient le nom du fichier d'origine.
Lorsqu'on accède au lien souple, Linux reconnaît qu'il s'agit d'un lien, lit le nom du fichier d'origine, puis accède (en général) automatiquement à ce fichier.
Dans la plupart des cas, les deux situations donnent accès aux données d'origine, mais les mécanismes sont différents.

Les liens durs semblent plus simples à la plupart des gens (d'ailleurs, je les ai expliqués en une phrase ci-dessus, contre deux pour les liens souples), mais ils ont divers inconvénients et pièges d'implémentation qui font des liens souples, et de loin, l'alternative la plus utilisée.

Dans ce défi, on apprend à utiliser les liens symboliques (aussi appelés _symlinks_).
Les liens symboliques se créent avec la commande `ln` selon la syntaxe `ln -s TARGET LINK_NAME`.
`TARGET` est le chemin vers lequel pointe le lien, et `LINK_NAME` est le nouveau chemin que l'on crée.
Par exemple :

```console
hacker@dojo:~$ cat /tmp/myfile
This is my file!
hacker@dojo:~$ ln -s /tmp/myfile /home/hacker/ourfile
hacker@dojo:~$ cat ~/ourfile
This is my file!
hacker@dojo:~$
```

On voit que l'accès au lien symbolique donne le contenu du fichier d'origine !
Dans cet exemple, `/tmp/myfile` est la cible, et `/home/hacker/ourfile` est le nom du lien.

Un lien symbolique peut être reconnu de plusieurs façons.
Par exemple, la commande `file`, qui prend un nom de fichier et indique son type, reconnaît les liens symboliques :

```console
hacker@dojo:~$ file /tmp/myfile
/tmp/myfile: ASCII text
hacker@dojo:~$ file ~/ourfile
/home/hacker/ourfile: symbolic link to /tmp/myfile
hacker@dojo:~$
```

À nous de jouer !
Dans ce niveau, le flag se trouve, comme toujours, dans `/flag`, mais `/challenge/catflag` affiche à la place le contenu de `/home/hacker/not-the-flag`.
Le chemin `/home/hacker/not-the-flag` est le nom du lien dans ce défi.
Il faut choisir la cible qui fera croire à `/challenge/catflag` qu'il doit afficher le flag !

----
**ATTENTION :** si une expérience précédente a laissé un fichier à `/home/hacker/not-the-flag`, le supprimer d'abord, pour que `ln` puisse y créer le lien symbolique.
