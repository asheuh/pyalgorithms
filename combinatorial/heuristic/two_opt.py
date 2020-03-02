"""
Imports
"""
from pyalgorithms.combinatorial.read_csv import read_file


class TwoOptimal:
    """
    2-opt algorithm to give an approximate solution to the
    travelling salesman problem
    utilizes local search optimization
        - A   B -             - A - B -
            X         ==>     
        - C   D -             - C - D -
    """
    best_route = {}

    def __init__(self, matrix):
        self.coords = matrix

    def distance(self, i: int, j: int) -> float:
        """
        calculates the distance between point i and j
        -----------

        Parameters
        ----------
        i, j; int
            i represents the starting point
            j is the next point to to move

        Return
        -------
        out; float
            out is the total distance between the optimized points
        """
        dist = self.coords[i][j]
        if dist == '':
            dist = self.coords[j][i]
        return float(dist)

    def cost(self, vertices: list) -> tuple:
        """
        calculates the cost between points; in other words
        how optimal is the route

        Paramaters
        ----------
        vertices; list
            vertices is the path that you need to find it's cost

        Returns
        -------
        out; tuple
            cost
            time_list; this is a list of time interval between eash optimized route
        """
        cost = self.distance(vertices[-1], vertices[0])
        n = len(vertices)

        for i in range(n - 1):
            gain = self.distance(vertices[i], vertices[i + 1])
            cost += gain
        return cost

    def insert(self, path, cost_time):
        cost, time_list = cost_time
        self.best_route['Best Path'] = {'cost': cost, 'path': path}

    def swap(self, path: list, i: int, j: int) -> list:
        """
        1. take route[0] to route[i-1] and add them in order to new_route
        2. take route[i] to route[k] and add them in reverse order to new_route
        3. take route[k+1] to end and add them in order to new_route
        return new_route;
        
        this performs the swap to create an optimized route

        example route: A ==> B ==> C ==> D ==> E ==> F ==> G ==> H ==> A  
        example i = 4, example k = 7  
        new_route:  
        1. (A ==> B ==> C)  
        2. A ==> B ==> C ==> (G ==> F ==> E ==> D)  
        3. A ==> B ==> C ==> G ==> F ==> E ==> D (==> H ==> A)
        """
        new_route = path[:]  # assign an intial value or path
        new_route = [*path[:i], *path[i:j + 1][::-1],
                     *path[j + 1:]]  # list concatenation

        return new_route

    def find_best_path(self, current_tour: list) -> list:
        """
        This is the heuristic algorithm (2-opt); it gradually improve an, 
        initially given, feasible answer (local search) until it reaches a 
        local optimum and no more improvements can be made.
        
        the algo tries to achieve a time complexity of O(n**2)
        """
        change = -1
        tour = current_tour
        length = len(tour)

        while change < 0:
            a, b, change = 0, 0, 0
            for n in range(length - 3):
                for m in range(n + 2, length - 1):
                    i, j = tour[n], tour[m]
                    k, l = tour[n + 1], tour[m + 1]

                    # calculate gain
                    gain = self.distance(i, j) + self.distance(k, l)
                    gain -= self.distance(i, k) + self.distance(j, l)

                    if gain < change:
                        change = gain
                        a, b = (n, m)
            if change < 0:
                tour = self.swap(tour, a + 1, b)  # swap the points
        self.insert(tour, self.cost(
            tour))  # save the optimized route in a dictionary data structure


if __name__ == "__main__":
    MATRIX = read_file('../data/distance_data.csv')
    TOUR = [i for i in range(len(MATRIX))]
    T = TwoOptimal(MATRIX)
    T.find_best_path(TOUR)
