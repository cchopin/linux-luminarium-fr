Voyons les effets de l'effacement de tout votre système de fichiers.
Vous êtes maintenant un `rm` expérimenté, mais auparavant, `/challenge/check` affichait le flag quand vous débarrassiez le système de fichiers de ses encombrants.
Et s'il ne l'avait pas fait ? Sans `cat`, comment liriez-vous ce `/flag` ?

Rappelez-vous, dans le module [Déchiffrer la documentation](https://pwn.college/linux-luminarium-fr/man), que certaines commandes du shell sont des _primitives_ (builtins).
Si `ls`, `cat` et consorts n'en sont pas, `read` (qui, comme vous vous en souvenez du module [Variables du shell](https://pwn.college/linux-luminarium-fr/variables), peut lire des fichiers) en est une.
Cela signifie que, même si vous effacez tout votre système de fichiers, tant qu'une instance de bash est déjà lancée, vous pouvez lire des fichiers !

Ce défi vous oblige à essayer.
Il est presque identique au précédent, mais vous devez lire le flag vous-même après avoir détruit le système.
Une fois que vous aurez tout supprimé avec `rm`, le `/challenge/check` que vous avez lancé auparavant restaurera le fichier `/flag` et le rendra lisible.
Vous pourrez alors le lire avec `read` !
