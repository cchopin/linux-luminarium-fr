Ce niveau présente la commande `man`.
`man` est l'abréviation de `manual` (manuel) : elle affiche, lorsqu'il existe, le manuel de la commande donnée en argument.
Par exemple, prenons la commande `yes` (oui, c'est une vraie commande) :

```console
hacker@dojo:~$ man yes
```

Cela affiche la page de manuel de `yes`, qui ressemble à ceci :

```text
YES(1)                           User Commands                          YES(1)

NAME
       yes - output a string repeatedly until killed

SYNOPSIS
       yes [STRING]...
       yes OPTION

DESCRIPTION
       Repeatedly output a line with all specified STRING(s), or 'y'.

       --help display this help and exit

       --version
              output version information and exit

AUTHOR
       Written by David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report any translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright  ©  2020  Free Software Foundation, Inc.  License GPLv3+: GNU
       GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free  to  change  and  redistribute  it.
       There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation <https://www.gnu.org/software/coreutils/yes>
       or available locally via: info '(coreutils) yes invocation'

GNU coreutils 8.32               February 2022                          YES(1)
```

Les sections importantes sont :

```text
NAME(1)                           CATEGORY                          NAME(1)

NAME
	This gives the name (and short description) of the command or
	concept discussed by the page.

SYNOPSIS
	This gives a short usage synopsis. These synopses have a standard
	format. Typically, each line is a different valid invocation of the
	command, and the lines can be read as:

	COMMAND [OPTIONAL_ARGUMENT] SINGLE_MANDATORY_ARGUMENT
	COMMAND [OPTIONAL_ARGUMENT] MULTIPLE_ARGUMENTS...

DESCRIPTION
	Details of the command or concept, with detailed descriptions
	of the various options.

SEE ALSO
	Other man pages or online resources that might be useful.

COLLECTION                        DATE                          NAME(1)
```

On peut faire défiler la page de manuel avec les flèches, et avec PgUp/PgDn.
Une fois la lecture terminée, la touche `q` permet de quitter.

Les pages de manuel sont stockées dans une base centralisée.
Si la curiosité nous pousse, cette base se trouve dans le répertoire `/usr/share/man`, mais on n'a jamais besoin d'y accéder directement : on l'interroge avec la commande `man`.
Les arguments de `man` ne sont pas des chemins de fichiers, mais les noms des entrées elles-mêmes (on exécute `man yes` pour consulter la page de `yes`, et non `man /usr/bin/yes`, qui est pourtant le chemin réel du programme, mais produirait un affichage illisible).

Le défi de ce niveau possède une option secrète qui, utilisée, fait afficher le flag par le programme.
Il faut découvrir cette option dans la page de manuel de `challenge` !
