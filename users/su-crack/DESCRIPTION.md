Quand on saisit un mot de passe pour `su`, celui-ci est comparé au mot de passe enregistré pour cet utilisateur.
Ces mots de passe étaient autrefois stockés dans `/etc/passwd`. Comme ce fichier est lisible par tous, ce n'est pas une bonne idée : les mots de passe ont donc été déplacés dans `/etc/shadow`.
Voici l'exemple de `/etc/shadow` du niveau précédent :

```console
root:$6$s74oZg/4.RnUvwo2$hRmCHZ9rxX56BbjnXcxa0MdOsW2moiW8qcAl/Aoc7NEuXl2DmJXPi3gLp7hmyloQvRhjXJ.wjqJ7PprVKLDtg/:19921:0:99999:7:::
daemon:*:19873:0:99999:7:::
bin:*:19873:0:99999:7:::
sys:*:19873:0:99999:7:::
sync:*:19873:0:99999:7:::
games:*:19873:0:99999:7:::
man:*:19873:0:99999:7:::
lp:*:19873:0:99999:7:::
mail:*:19873:0:99999:7:::
news:*:19873:0:99999:7:::
uucp:*:19873:0:99999:7:::
proxy:*:19873:0:99999:7:::
www-data:*:19873:0:99999:7:::
backup:*:19873:0:99999:7:::
list:*:19873:0:99999:7:::
irc:*:19873:0:99999:7:::
gnats:*:19873:0:99999:7:::
nobody:*:19873:0:99999:7:::
_apt:*:19873:0:99999:7:::
systemd-timesync:*:19901:0:99999:7:::
systemd-network:*:19901:0:99999:7:::
systemd-resolve:*:19901:0:99999:7:::
mysql:!:19901:0:99999:7:::
messagebus:*:19901:0:99999:7:::
sshd:*:19901:0:99999:7:::
hacker::19916:0:99999:7:::
zardus:$6$bEFkpM0w/6J0n979$47ksu/JE5QK6hSeB7mmuvJyY05wVypMhMMnEPTIddNUb5R9KXgNTYRTm75VOu1oRLGLbAql3ylkVa5ExuPov1.:19921:0:99999:7:::
```

Séparés par des `:`, le premier champ de chaque ligne est le nom d'utilisateur, et le second est le mot de passe.
Une valeur `*` ou `!` signifie que la connexion par mot de passe est désactivée pour ce compte. Un champ vide signifie qu'il n'y a pas de mot de passe, une erreur de configuration pas si rare, qui permet parfois d'utiliser `su` sans mot de passe. La longue chaîne, comme celle de `zardus`, `$6$bEFkpM0w/6J0n979$47ksu/JE5QK6hSeB7mmuvJyY05wVypMhMMnEPTIddNUb5R9KXgNTYRTm75VOu1oRLGLbAql3ylkVa5ExuPov1.`, est le résultat du chiffrement à sens unique (hachage) du mot de passe de `zardus` du niveau précédent, c'est-à-dire `dont-hack-me`.
D'autres champs de ce fichier ont d'autres significations, que l'on peut découvrir [ici](https://www.cyberciti.biz/faq/understanding-etcshadow-file/).

Quand on saisit un mot de passe dans `su`, celui-ci est haché, puis le résultat est comparé à la valeur enregistrée.
Si les deux correspondent, `su` donne accès à l'utilisateur !

Mais que faire si l'on ne connaît pas le mot de passe ?
Si l'on possède la valeur hachée, on peut la *casser* ! Or `/etc/shadow` n'est lisible, par défaut, que par `root`, mais des fuites arrivent !
Par exemple, des sauvegardes sont souvent stockées sans chiffrement et insuffisamment protégées sur des serveurs de fichiers, ce qui a déjà provoqué d'innombrables fuites de données.

Si un pirate met la main sur un `/etc/shadow` qui a fuité, il peut commencer à casser les mots de passe et à semer le chaos.
Le craquage peut se faire avec le célèbre [John the Ripper](https://www.openwall.com/john/), comme suit :

```console
hacker@dojo:~$ john ./my-leaked-shadow-file
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Will run 32 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password1337      (zardus)
1g 0:00:00:22 3/3 0.04528g/s 10509p/s 10509c/s 10509C/s lykys..lank
Use the "--show" option to display all of the cracked passwords reliably
Session completed
hacker@dojo:~$
```

Ici, John the Ripper a cassé le hachage du mot de passe fuité de `zardus` et retrouvé sa vraie valeur, `password1337`.
Pauvre `zardus` !

Ce niveau reproduit cette situation : une fuite de `/etc/shadow` est fournie dans `/challenge/shadow-leak`.
Il faut le casser (cela peut prendre quelques minutes), basculer vers `zardus` avec `su`, puis exécuter `/challenge/run` pour obtenir le flag !
