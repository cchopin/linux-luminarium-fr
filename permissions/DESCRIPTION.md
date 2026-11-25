Ce module initie aux permissions Linux, l'une des notions les plus importantes pour la suite, puisqu'elles régissent l'accès aux fichiers pour les différents utilisateurs.

Sous Linux, les fichiers ont des permissions, aussi appelées modes de fichier.
On peut consulter les permissions d'un fichier ou d'un répertoire avec `ls -l`.
Créons quelques fichiers et observons leurs permissions :

```console
hacker@dojo:~$ mkdir pwn_directory
hacker@dojo:~$ touch college_file
hacker@dojo:~$ ls -l
total 4
-rw-r--r-- 1 hacker hacker    0 May 22 13:42 college_file
drwxr-xr-x 2 hacker hacker 4096 May 22 13:42 pwn_directory
hacker@dojo:~$
```

Cette sortie contient beaucoup d'informations, et on en découvrira une grande partie dans ce module !
Pour l'instant, voici une lecture globale de cette sortie :

#### Le type de fichier

Le premier caractère de chaque ligne indique le type de fichier.
Pour `pwn_directory`, le `d` indique un répertoire, et pour `college_file`, le `-` indique un fichier ordinaire.
D'autres types existent, et on en rencontrera certains plus tard dans le parcours pwn.college.

#### Les permissions

Les neuf caractères suivants sont les permissions d'accès réelles du fichier ou du répertoire. Ils sont répartis en trois groupes de trois caractères : les permissions du propriétaire du fichier (le « propriétaire »), celles du groupe propriétaire (le « groupe ») et celles de tous les autres accès (par exemple, les autres utilisateurs et les autres groupes).
Nous les détaillerons plus loin dans le module.

#### Les informations de propriété

Deux colonnes indiquent l'utilisateur propriétaire du fichier (ici, l'utilisateur `hacker`), puis le groupe propriétaire (ici, aussi le groupe `hacker`).
On va s'exercer sur ces informations.

----

Dans ce module, on s'entraîne à percevoir les permissions.
C'est parti !

## Fiche de cours (ajout, hors traduction)

*Cette fiche n'est pas une traduction. Elle s'appuie sur les quatre diapositives « Access Control » d'Adam Doupé (Arizona State University), en anglais, dont les liens figurent dans les ressources du module. Elle reprend les notions dans l'ordre où les défis en ont besoin, sans donner de solution.*

### 1. Autorisation et contrôle d'accès

La première diapositive distingue deux notions. L'**autorisation** définit ce qu'on a le droit de faire sur un système : c'est une politique. Le **contrôle d'accès** est le mécanisme qui applique cette politique. Il ne faut pas confondre l'autorisation avec l'**authentification**, qui consiste à vérifier qui l'on est.

Le contrôle d'accès repose sur trois éléments :

- les **sujets** : les entités qui agissent, comme les processus ou les utilisateurs ;
- les **objets** : les ressources sur lesquelles on agit, comme les fichiers ;
- les **droits** : ce que le sujet peut faire sur l'objet, comme lire, écrire ou exécuter.

### 2. La matrice de contrôle d'accès

On peut représenter ces droits dans une **matrice** : chaque ligne est un sujet, chaque colonne est un objet, et chaque case contient les droits du sujet sur l'objet. Dans le modèle simplifié d'UNIX, les sujets sont les processus, les objets sont les fichiers, et les droits sont la lecture (`r`), l'écriture (`w`), l'exécution (`x`), l'ajout (`a`) et la propriété (`o`).

La matrice est souvent très creuse : la plupart des cases sont vides. Il faut donc la stocker autrement.

### 3. Deux façons de stocker la matrice

- Les **listes de contrôle d'accès** (ACL) stockent chaque colonne avec l'objet : pour un fichier donné, on sait qui peut faire quoi.
- Les **listes de capacités** stockent chaque ligne avec le sujet : pour un utilisateur donné, on sait sur quoi il peut agir.

Les ACL facilitent la révision des accès aux objets et la révocation des droits sur un objet. Les capacités facilitent le principe du moindre privilège pour des sujets temporaires et les révisions d'accès par sujet. Pour accorder un droit avec des capacités, il faut que celles-ci soient infalsifiables et que leur transmission soit contrôlée.

### 4. Les permissions POSIX

Sous Linux, chaque fichier dispose de **douze bits** de permission, regroupés en quatre ensembles de trois bits :

- le premier ensemble contient les bits **SUID**, **SGID** et **sticky** ;
- les trois ensembles suivants concernent respectivement le propriétaire, le groupe propriétaire, et tous les autres utilisateurs. Chacun contient les bits de lecture, d'écriture et d'exécution.

Le bit **SUID** fait s'exécuter le programme avec les droits de son propriétaire. Le bit **sticky**, sur un répertoire, permet à chacun d'y créer des fichiers, mais seul le propriétaire d'un fichier (ou du répertoire) peut le supprimer ou le renommer. Dans `ls -l`, la lettre `s` à la place du `x` signifie que le bit d'exécution et le bit SUID sont positionnés, et `S` signifie que le SUID est positionné sans l'exécution. Pour le bit sticky, `t` indique qu'il est positionné et que l'autre utilisateur peut exécuter, et `T` qu'il est positionné sans cette possibilité.
