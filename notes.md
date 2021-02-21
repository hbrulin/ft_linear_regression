
#install
brew install python
pip3 install pandas
pip3 install matplotlib

have a malefile or something

#Linear function : 
- graph is a straight line
Linear function with one variable = f(x) = ax + b
En l'espèce pour le programme de prédiction : 
prixestimé(kilométrage) = theta0 + (theta1 * kilometrage)
Avant de lancer le programme d'entraînement, theta0 et theta1 auront pour valeur 0. 

Le programme d'entraînement : lit le jeu de données et fait une régression linéaire sur ces données. 
Sauvegarde la valeur de theta0 et theta1 pour le premier programme. 


Sigma : symbolise une addition de termes consécutifs.
Indice de sommation sous sigma -> i= 0 signifie que l'indice i débute avec la valeur 1.
L'indice de sommation i est incrément de 1 à chauqe itération, et s'arrpete quand i = m-1 (variable au dessus du sigma).

Fraction unitaire : Une fraction unitaire est l'inverse d'un entier positif.
Exemple : l'inverse de trois est 1/3 = 0.333, puisque 1/3 * 3 = 1.


Traduction de la formule du programme d'apprentissage : 
1/m SIGMA = inverse de m.

theta0 = ratio * inverse de res
while (i < m -1) {
	res = prix estimé * (km[i] - prix[i]);
	i++;
}
Prix estimé étant calculé comme dans le programme 1.


m est la taille du jeu de données.

Fonction de perte : 
Beaucoup d’algorithmes de Machine Learning obtiennent de bonnes performances grâce à leur entraînement. Cependant, une grande majorité des entraînements repose sur l’optimisation d’une fonction de perte. Plus sa valeur est petite, meilleurs sont les résultats de l’algorithme. 
On a une fonction de perte, dont on va trouver le minimum grâce à l'algorithme de descente de gradient. 


Algorithme du gradient : 
Algorithme permettant de trouver le minimum d'une fonction.
En data science, utilisé quand on veut trouver l'estimateur du maximum de vraisemblance.
Trouve un minimum, c'st la même chose que trouve un maximum : il suffit de changer de signe. 
L’objectif du gradient descent est de modifier les paramètres d’une fonction donnée jusqu’a ce que son gradient soit nul.
On commence avec des valeurs initiales, aléatoires, puis calcul la fonction de mise à jour avec ces valeurs. On répète l'opération jusqu'à trouver les valeurs qui minimisent la fonction de coût. 


https://mrmint.fr/gradient-descent-algorithm

La régression linéraire : prend en entrée une variable x et essaie de trouver une fonction de prédiction h(x)
-> h(x) = theta0 + (theta1 *x)
-> getPrice(kilométrage) = theta0 + (theta1 * kilometrage)

Theta0 et theta1 sont les coefficients de la droite.
On a des points sur un graph : une droite représente la meilleure approximation par rapport à ces points. Cette approximation est rendue possible car on peut calculer les paramètre prédictifs theta0 et theta1 qui définissent notre droite.

Comment calculer les valeurs de theta0 et theta1?
La droite tente d'approcher le plus de points possibles, en réduisant l'écart avec ces derniers --> elle minimise au maximum l'erreur globale. 

Le but : trouver un couple theta0/theta1 optimal tel que h(x) soit le plus proche possible de la valeur qu'on essaie de prédire : valeur y. 

On définit l'erreur unitaire entre une valeur observée yi et une valeur prédite h(xi) comme suit : (h(xi) - yi)2.
Trouver le meilleur couple theta0 et theta1 revient à minimiser le coût global des erreurs unitaires.
Ce coût global se défini comme suit : 
  m
  E  (h(xi) - yi)2
 i=0
m étant la taille du training set.

La fonction de coût est définie comme suit : 
							 m
J(theta0, theta1) = 1/2m     E    (h(xi) - yi)2
							i=0

Si on remplace h(x) (la fonction de base, getPrice) par sa valeur définie plus haut, on obtient : 
							 m
J(theta0, theta1) = 1/2m     E    ((theta0 + (theta1 * xi)) - yi)2
							i=0
C'est la fonction de coût (qui calcul le minimum en terme d'erreurs).


Pour minimiser cette fonction de coût, on utilise l'algorithme de descente du gradient. Algorithme itératif qui va changer, à chaque itération, les valeurs de theta0 et theta1 jusqu'à trouver le meilleur couple possible:

- on initialise aléatoire les valeurs de theta0 et theta1.
- à chaque itération, on fait un nouveau pas qui de la taille fixée par le learning rate : alpha.


#panda
https://www.datacamp.com/community/tutorials/pandas-read-csv