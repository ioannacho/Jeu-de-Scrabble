# Jeu-de-Scrabble 

## Description
Ce projet est un jeu interactif où l'utilisateur doit trouver des mots à partir de lettres mélangées. Le jeu se déroule en plusieurs manches de différentes difficultés : facile, moyen et difficile. Pour chaque manche, l'utilisateur doit deviner trois mots à partir des lettres mélangées. Si un mot est trouvé, il gagne un point.

## Fonctionnement
Le jeu propose trois niveaux de difficulté : facile, moyen et difficile. En fonction du niveau choisi, une liste de mots est fournie, et l'utilisateur doit trouver trois mots différents. Après avoir mélangé toutes les lettres de ces mots, l'utilisateur doit les deviner en entrant des mots dans un certain nombre de tentatives.

### Manches du jeu :
- **Facile** : Une liste de mots simples.
- **Moyen** : Une liste de mots avec un peu plus de difficulté.
- **Difficile** : Une liste de mots longs et complexes.

## Fonctionnalités principales :
1. **Génération de mots en fonction du niveau de difficulté** : Le jeu adapte la liste de mots selon la difficulté sélectionnée.
2. **Mélange des lettres** : Les lettres des mots choisis sont mélangées pour créer un défi.
3. **Suppression des doublons** : Les lettres doublon sont supprimées pour rendre le défi encore plus complexe.
4. **Essais pour deviner les mots** : L'utilisateur a un nombre limité de tentatives pour deviner les mots. Chaque mot trouvé rapporte un point.
5. **Affichage des mots à trouver** : À la fin de chaque manche, les mots à trouver sont affichés.

## Comment jouer :
1. Lancez le jeu en exécutant le script Python.
2. Choisissez un niveau de difficulté (facile, moyen, difficile).
3. Essayez de deviner les mots mélangés en entrant votre réponse.
4. Si vous trouvez le mot, vous marquez un point et le mot est ajouté à la liste des mots trouvés.
5. Le jeu se termine après trois manches et vous pouvez voir votre score total.
