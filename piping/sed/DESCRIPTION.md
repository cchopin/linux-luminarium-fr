`grep` n'est pas le seul moyen de chercher des motifs. Il arrive que les données utiles et les données parasites soient mêlées dans la même ligne,
et qu'il faille retirer les parasites. Pour cela, on dispose de `sed`. `sed` permet de remplacer facilement un motif
dans un texte par un autre mot. La syntaxe de recherche et de remplacement est simple :

```
sed "s/oldword/newword/g"
```

`s/` - substitution  
`oldword` - le mot à remplacer  
`newword` - le remplacement de `oldword`  
`/g` - global (recherche toutes les occurrences du motif)  

Dans ce défi, `/challenge/run` affiche le flag, mais avec la chaîne « FAKEFLAG » entre chaque caractère.
Il faut retirer les données parasites du flag. Bonne chance !
