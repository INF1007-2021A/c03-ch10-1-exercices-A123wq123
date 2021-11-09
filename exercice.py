#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
import math
import random



# TODO: Définissez vos fonctions ici (il en manque quelques unes)

#def linear_values() -> np.ndarray:
    #return np.array([np.random.uniform(-1.3, 2.5, 64)])
    #or do return np.linspace(min, max, reps)


#def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    #for couple_x_y in cartesian_coordinates:

    #return np.array([])
    #could be interesting to look into import cmath pour use the polar function


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0
    #this uses la fonction armin et abs de numpy so check net pour réponse.


def fonction_du_graphique(x):
    y = x**2 * np.sin(1/(x**2)) + x
    return y


def creer_graphique(debut_interval, fin_interval, nb_points):

    x = []
    y = []
    abscisse = debut_interval
    pas = (fin_interval - debut_interval) / nb_points
    for k in range(0, nb_points + 1):
        x.append(abscisse)
        y.append(fonction_du_graphique(abscisse))
        abscisse += pas
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
    plt.close()


def estimer_pi_monte_carlo(nb_de_points):
    points_totaux = 0
    points_dans_cercle = 0


    while True :
        point_aleatoire = (random.uniform(-1, 1), random.uniform(-1, 1))

        points_totaux += 1

        if (point_aleatoire[0]**2 + point_aleatoire[1]**2) <= 1:
            points_dans_cercle += 1

        if points_totaux == nb_de_points:
            return (points_dans_cercle*4/points_totaux)





if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(linear_values())
    creer_graphique(-1, 1, 250)


    pass
