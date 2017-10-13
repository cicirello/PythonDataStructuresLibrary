##  Python Data Structures Library
##
##  Copyright (C) 2017 Vincent A. Cicirello.
##  http://www.cicirello.org/
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import warnings


class DisjointSets :
    """Disjoint Set Forests: Representation of disjoint sets of integers from the range [0..N-1].

    Disjoint sets of integers from the range [0..size-1] are represented as
    a disjoint set forest.  This implementation uses both the union by rank heuristic, as well as
    path compression.
    """


    def __init__(self, size) :
        """Initializes disjoint set forest of the integers in interval [0..size-1].

        Each integer from 0 to size - 1 is initially in a set by itself.

        Keyword arguments:
        size -- number of elements in disjoint set forest.  The elements are integers from 0 to size-1.
        """

        # List of parent nodes, one for each element, in the tree representing
        # a node's set. Root of tree has itself as parent.
        self._p = list(range(size))
        # A node's rank is an upper bound on node height (given chain of parents to root).
        self._rank = [0] * size


    def union(self,x,y) :
        """Union by rank.

        Computes the union of the sets containing x and y.

        Keyword arguments:
        x -- an element, an integer in [0,size)
        y -- an element, an integer in [0,size)
        """
        
        self._link(self.find_set(x), self.find_set(y))


    def find_set(self,x) :
        """Finds the set id for a given element, and performs path compression.

        Finds the set id for a given element, where the set id is the root of its
        tree in the forest.  The find also performs path compression, resetting the parents
        of all nodes along path to root to point directly to root.  Path compression does not
        reset ranks, thus ranks are upper bounds only.

        Keyword arguments:
        x -- the element whose set we want to find
        """
        
        if x != self._p[x] :
            self._p[x] = self.find_set(self._p[x])
        return self._p[x]


        
    def _link(self,x,y) :
        if self._rank[x] > self._rank[y] :
            self._p[y] = x
        else :
            self._p[x] = y
            if self._rank[x] == self._rank[y] :
                self._rank[y] = self._rank[y] + 1


    warnings.simplefilter("module")
    def findSet(self,x) :
        warnings.warn("findSet is replaced with find_set", DeprecationWarning)
        
        return self.find_set(x)
