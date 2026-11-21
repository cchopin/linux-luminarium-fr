Il arrive qu'on ait besoin de comparer la sortie de deux commandes plutôt que deux fichiers.
On pourrait penser à enregistrer chaque sortie dans un fichier d'abord :

```console
hacker@dojo:~$ command1 > file1
hacker@dojo:~$ command2 > file2
hacker@dojo:~$ diff file1 file2
```

Il existe pourtant une manière plus élégante ! Linux suit la philosophie selon laquelle [« tout est un fichier »](https://en.wikipedia.org/wiki/Everything_is_a_file).
Autrement dit, le système s'efforce de donner un accès de type fichier à la plupart des ressources, y compris l'entrée et la sortie des programmes en cours d'exécution !
Le shell suit cette philosophie : par exemple, on peut utiliser n'importe quel utilitaire qui prend des fichiers en argument, et le relier à la sortie de programmes, comme on l'a appris dans les niveaux précédents.

On peut même aller plus loin, et relier l'entrée et la sortie de programmes aux _arguments_ de commandes.
Cela se fait avec la [substitution de processus](https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html) (Process Substitution).
Pour lire la sortie d'une commande (substitution de processus en entrée), on écrit `<(command)`.
Lorsqu'on écrit `<(command)`, bash exécute la commande et relie sa sortie à un fichier temporaire qu'il crée.
Ce n'est pas un _vrai_ fichier, bien sûr : c'est ce qu'on appelle un _tube nommé_ (named pipe), car il possède un nom de fichier :

```console
hacker@dojo:~$ echo <(echo hi)
/dev/fd/63
hacker@dojo:~$
```

D'où vient `/dev/fd/63` ?
`bash` a remplacé `<(echo hi)` par le chemin du tube nommé relié à la sortie de la commande !
Pendant que la commande tourne, lire ce fichier revient à lire la sortie standard de la commande.
On procède généralement ainsi avec des commandes qui prennent des fichiers en argument :

```console
hacker@dojo:~$ cat <(echo hi)
hi
hacker@dojo:~$
```

On peut bien sûr le faire plusieurs fois :

```console
hacker@dojo:~$ echo <(echo pwn) <(echo college)
/dev/fd/63 /dev/fd/64
hacker@dojo:~$ cat <(echo pwn) <(echo college)
pwn
college
hacker@dojo:~$
```

Passons au défi !
Rappelons-nous ce qu'on a appris avec le défi `diff` de [Comprendre les commandes](https://pwn.college/linux-luminarium-fr/commands).
Dans ce défi, on comparait deux fichiers.
Ici, on compare deux sorties de commandes : `/challenge/print_decoys`, qui affiche une série de faux flags, et `/challenge/print_decoys_and_flag`, qui affiche les mêmes faux flags plus le vrai flag.

Utiliser la substitution de processus avec `diff` pour comparer les sorties de ces deux programmes et trouver le flag !
