Au démarrage, le shell cherche un fichier `.bashrc` dans votre répertoire personnel et l'exécute comme _script de démarrage_.
On peut personnaliser son `/home/hacker/.bashrc` avec des éléments utiles : définir des variables d'environnement, ajuster la configuration du shell, et ainsi de suite.

On peut _aussi_ s'en servir pour faire le mal !
Le `.bashrc` d'une victime inconsciente est une cible classique pour les bêtises.
Imaginez qu'on se glisse sur l'ordinateur d'un ami et qu'on ajoute `echo "Hackers were here!"` à la fin de son `.bashrc`.
C'est amusant, mais la même capacité peut servir à des fins bien plus malveillantes.
Les logiciels malveillants visent souvent les scripts de démarrage comme `.bashrc`, pour se maintenir durablement !

Dans ce défi, faisons comme si l'on s'était introduit sur l'ordinateur d'un utilisateur victime !
Cet utilisateur s'appelle `zardus`, et son répertoire personnel est `/home/zardus`.
Vous, en tant qu'utilisateur `hacker`, avez un accès en écriture à son `.bashrc`, et `zardus` peut lire `/flag`.
La victime est simulée par le script `/challenge/victim`, que vous pouvez lancer à tout moment pour observer la connexion de la victime à l'ordinateur.
Pouvez-vous obtenir le flag ?

----
**INDICE :**
Comme les scripts étudiés dans [Chaîner les commandes](https://pwn.college/linux-luminarium-fr/chaining), le `.bashrc` est simplement un script shell.
Ajouter une ligne contenant une commande (par exemple `echo Hello Hackers`) fera exécuter cette commande : il suffit donc de trouver la commande qui donnera le flag !

**NOTE :**
Le `/home/zardus/.bashrc` de la victime contient déjà beaucoup de choses : le démarrage du shell est une affaire complexe.
Ne vous inquiétez pas, ajoutez simplement votre charge utile à la fin et espérez le meilleur !

**INDICE :**
Vous devez examiner ce qui se passe du côté de `zardus` pour déboguer votre solution ?
En mode privilégié, la commande `sudo su --login zardus` ouvre une session de Zardus !
