Et si l'on veut conserver le fichier d'origine ? On peut le faire avec la commande `cp`.
Son usage est le même que celui de `mv`, mais elle conserve le fichier source.
La commande est `cp SOURCE DESTINATION` : le premier argument est le fichier existant, et le second indique où créer la copie.

Ce défi demande de copier le fichier `/flag` vers `/tmp/hack-the-planet`. À faire !
Une fois cela fait, lancer `/challenge/check`, qui vérifie le travail et donne le flag.

----
**NOTE:**
Lorsque la destination de `cp` est un répertoire, `cp` place la copie à l'intérieur, sous le nom du fichier source.
Dans ce défi, `/tmp/hack-the-planet` doit désigner le fichier copié lui-même, et non un répertoire existant.
