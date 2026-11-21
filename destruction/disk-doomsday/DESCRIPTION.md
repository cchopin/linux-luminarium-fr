L'espace disponible dans `/home/hacker`, dans ce conteneur, n'est que de **1 gigaoctet**.
Dans ce niveau, vous allez encombrer `/home/hacker` avec tant de déchets qu'on ne peut même plus créer un fichier de 1 mégaoctet.
Quand cela arrive, votre espace de travail devient inutilisable.
Nous nous entraînons à provoquer cette situation dans ce défi, avant de la développer un peu plus tard.

Comment remplir le disque ?
Il existe tellement de moyens.
Ici, nous allons vous apprendre la commande `yes` !

```
hacker@dojo:~$ yes | head
y
y
y
y
y
y
y
y
y
y
hacker@dojo:~$
```

La commande `yes` affiche `y` sans fin.
Son usage typique est d'automatiser les demandes de confirmation (« Êtes-vous sûr de vouloir supprimer ce fichier ? ») grâce aux tubes, mais nous l'utiliserons ici pour produire un fichier énorme rempli de lignes « y ».
Il suffit de rediriger `yes` vers un fichier de votre répertoire personnel, et vous remplirez votre disque en une minute ou deux !

Ce défi vous oblige à remplir le disque, puis à faire le ménage.
La procédure :

1. Remplir votre disque.
2. Lancer `/challenge/check`. Il essaie de créer un fichier temporaire de 1 mégaoctet. Si cela échoue, vous passez la première étape, et le vérificateur vous demande de libérer de l'espace.
3. Supprimer le fichier créé (avec `rm`) pour libérer de la place.
4. Relancer `/challenge/check`. S'il peut maintenant créer le fichier temporaire (c'est-à-dire si vous avez bien nettoyé votre répertoire personnel), vous recevez le flag.

----
**NOTE :**
Pour ce défi, `/home/hacker` est un petit répertoire personnel temporaire.
Vos fichiers existants ne sont pas disponibles ici, et les fichiers que vous enregistrez ici ne persistent pas après la fin du défi.

**Pourquoi deux étapes ?**
Votre répertoire personnel persiste d'un défi à l'autre.
Si nous vous laissions le remplir, votre pwn.college cesserait de fonctionner.
C'est _de loin_ la cause la plus fréquente de problèmes étranges sur pwn.college !

**AU SECOURS, ÇA A CASSÉ !**
Si vous remplissez le disque sans nettoyer ensuite, il faudra vous connecter en `ssh` pour réparer (en supprimant ce fichier).
C'est un peu délicat, mais nous décrivons la marche à suivre dans la partie « Connexion par SSH » du module [Premiers pas](https://pwn.college/welcome/welcome).
