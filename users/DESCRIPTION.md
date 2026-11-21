Croit-on que `hacker` est le seul fantôme de la machine ?
Un système Linux typique compte en réalité de très nombreux utilisateurs !
La liste complète des utilisateurs d'un système Linux est définie dans le fichier `/etc/passwd`. Son nom vient de l'histoire : il ne contient plus de mots de passe.
Voici un exemple, tiré du conteneur du dojo :

```console
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
mysql:x:104:105:MySQL Server,,,:/nonexistent:/bin/false
messagebus:x:105:106::/nonexistent:/usr/sbin/nologin
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
hacker:x:1000:1000::/home/hacker:/bin/bash
```

Beaucoup d'utilisateurs, et beaucoup d'informations !
Chaque ligne contient, séparés par des `:`, le nom d'utilisateur, un `x` qui tient la place de l'ancien mot de passe (on verra plus loin où il se trouve réellement), l'identifiant numérique de l'utilisateur, l'identifiant numérique de son groupe par défaut, des informations détaillées, le répertoire personnel et le shell par défaut.

L'utilisateur `hacker`, tout en bas, est celui qu'on utilise dans ce dojo.
La plupart des autres utilisateurs sont là pour des raisons historiques, sont des comptes de service pour des logiciels installés, ou sont des comptes « utilitaires ». Par exemple, l'utilisateur `nobody` permet de faire tourner certains programmes sans aucun privilège particulier.

Un utilisateur important est `root` : l'administrateur du système. Il a des implications de sécurité évidentes : un utilisateur `hacker` qui parviendrait, grâce à une fonctionnalité de Linux, à devenir `root` pourrait causer de graves dégâts sur le système.
Les attaquants qui s'introduisent dans un système cherchent très souvent à obtenir les droits de `root`. Il faut donc protéger `root` à tout prix !

Dans ce module, on explore différentes façons de changer d'utilisateur : celles qui servent à administrer le système, et quelques détournements amusants.
