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
    """Disjoint Set Forests: Representation of disjoint sets.

    Disjoint sets of any hashable type represented as disjoint set forest.
    If any size>1 passed to initializer, then
    initialized to disjoint sets of integers in the range [0..size-1].
    This implementation uses both the union by rank heuristic, as well as
    path compression.
    """


    def __init__(self, size=0) :
        """Initializes disjoint set forest.

        If size is 0, initialized to empty forest.  Use make_set to add singleton sets to forest.
        Elements can be any hashable type.

        If size >= 1, initializes disjoint sets of the integers in interval [0..size-1].
        Each integer from 0 to size - 1 is initially in a set by itself.

        Keyword arguments:
        size -- number of elements in disjoint set forest.  If size>0, the elements are integers from 0 to size-1.
                If size = 0, it is an empty forest to which you can add any hashable type.
        """

        self._nodes = {}
        for i in range(size) :
            self.make_set(i)


    def make_set(self,x) :
        """Creates a set containing only element x, of any hashable type, adding set to forest.

        
        Keyword arguments:
        x -- an element of any hashable type
        """
        
        class Node :
            pass
        n = Node()
        n.data = x
        n.p = n
        n.rank = 0
        self._nodes[x] = n
        

    def union(self,x,y) :
        """Union by rank.

        Computes the union of the sets containing x and y.

        Keyword arguments:
        x -- an element
        y -- an element
        """

        self._link(self._find_set(self._nodes[x]), self._find_set(self._nodes[y]))


    def find_set(self,x) :
        """Finds the set for a given element, and performs path compression.

        Finds the set for a given element, returning the data stored in the root node of its
        tree in the forest.  The find also performs path compression, resetting the parents
        of all nodes along path to root to point directly to root.  Path compression does not
        reset ranks, thus ranks are upper bounds only.

        Keyword arguments:
        x -- the element whose set we want to find
        """
        
        return self._find_set(self._nodes[x]).data
        


    def _find_set(self,nx) :
        """Finds the set for a given element, and performs path compression.

        Finds the set for a given element, returning the root node of its
        tree in the forest.  The find also performs path compression, resetting the parents
        of all nodes along path to root to point directly to root.  Path compression does not
        reset ranks, thus ranks are upper bounds only.

        Keyword arguments:
        nx -- the node of the element whose set we want to find
        """

        if nx != nx.p :
            nx.p = self._find_set(nx.p)
        return nx.p
        

        
    def _link(self,nx,ny) :
        if nx.rank > ny.rank :
            ny.p = nx
        else :
            nx.p = ny
            if nx.rank == ny.rank :
                ny.rank  = ny.rank  + 1



    warnings.simplefilter("module")
    def findSet(self,x) :
        warnings.warn("findSet is replaced with find_set", DeprecationWarning)
        
        return self.find_set(x)
