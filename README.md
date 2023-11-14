Projet : Arbre quaternaire

Un quadtree ou arbre quaternaire (arbre Q) est une structure de données de type arbre dans laquelle chaque nœud a quatre fils. Les quadtrees sont le plus souvent utilisés pour partitionner un espace bidimensionnel en le subdivisant récursivement en quatre nœuds.




Il existe plusieurs types de quadtree. Dans notre cas il s'agit d'un quadtree "region". Le quadtree «région» représente une partition de l'espace en deux dimensions en décomposant la région en quatre quadrants égaux, puis chaque quadrant en quatre sous-quadrants, et ainsi de suite, avec chaque «nœud terminal» comprenant des données correspondant à une sous-région spécifique. Chaque nœud de l'arbre a exactement : soit quatre enfants, soit aucun (cas d'un nœud terminal). Chaque Noeud comportant quatre éléments. Il s'agit d'une technique connue pour l'encodage d'images. Pour simplifier, les images sont carrées, de couleur noir et blanc et de côté 2^n.




