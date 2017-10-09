## Python Data Structures Library
##
## Copyright (C) 2017 Vincent A. Cicirello.
## http://www.cicirello.org/
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.


class PQ :
    """A Priority Queue (PQ) implemented with a binary heap.

    A binary min heap is used to implement a PQ.  A python dictionary, i.e., associative array,
    is used to enable changing priorities in O(lg N) time.

    Assuming a PQ with N elements, the runtimes of the operations are as follows.

    The following operations run in O(lg N) time: add, extractMin, changePriority

    The following operations run in O(1) time: peekMin, contains, getPriorityValue, size, isEmpty
    """

    def __init__(self) :
        """Initialize an empty PQ."""
        
        self._heap = []
        self._index = {}


    def size(self) :
        """Size of the PQ."""
        
        return len(self._heap)
    

    def isEmpty(self) :
        """Returns True if PQ is empty and False otherwise."""
        
        return len(self._heap) == 0


    
    def add(self, element, value) :
        """Adds an element to the PQ with a specified priority.

        Adds the element to the PQ provided PQ doesn't already contain it.
        Does nothing if the PQ already contains the element.

        Returns True if element added and False if already present.

        Keyword arguments:
        element -- The element to add.
        value -- The priority of the element.
        """

        if element in self._index :
            return False
        position = len(self._heap)
        self._heap.append((element, value))
        self._percolateUp(position)
        return True

    

    def peekMin(self) :
        """Returns, but does not remove, the element with the minimum priority value."""
        
        return self._heap[0][0]

    

    def extractMin(self) :
        """Removes and returns the element with minimum priority value."""
        
        minElement = self._heap[0][0]
        oldLast = self._heap.pop()
        if len(self._heap) > 0 :
            self._heap[0] = oldLast
            self._percolateDown(0)
        del self._index[minElement]
        return minElement
    


    def contains(self, element) :
        """Returns True if element is in the PQ and False otherwise.

        Keyword arguments:
        element -- The element
        """
        
        return element in self._index
    


    def getPriorityValue(self, element) :
        """Gets the current priority of the specified element.

        Keyword arguments:
        element -- The element
        """
        
        return self._heap[self._index[element]][1]
    


    def changePriorityValue(self, element, value) :
        """Changes the priority of an element in the PQ.

        Changes the priority of an element that is in the PQ.
        Does nothing if the PQ doesn't contains the element.

        Returns True if element is present in the PQ and False otherwise.

        Keyword arguments:
        element -- The element to add.
        value -- The new priority for the element.
        """
        
        if not self.contains(element) :
            return False
        position = self._index[element]
        if self._heap[position][1] > value :
            self._heap[position] = (element, value)
            self._percolateUp(position)
        elif self._heap[position][1] < value :
            self._heap[position] = (element, value)
            self._percolateDown(position)
        return True
        
   

    def _left(i) :
        return 2*i+1

    def _right(i) :
        return 2*i+2

    def _parent(i) :
        return (i-1)//2
        

    def _percolateUp(self, position) :
        element, value = self._heap[position]
        p = PQ._parent(position)
        while p >= 0 and self._heap[p][1] > self._heap[position][1] :
            self._heap[position] = self._heap[p]
            self._index[self._heap[position][0]] = position
            self._heap[p] = (element, value)
            position = p
            p = PQ._parent(position)
        self._index[element] = position

    def _percolateDown(self, position) :
        minChildPos = PQ._left(position)
        current = self._heap[position]
        while minChildPos < len(self._heap) :
            if minChildPos + 1 < len(self._heap) and self._heap[minChildPos + 1][1] < self._heap[minChildPos][1] :
                minChildPos = minChildPos + 1
            if self._heap[minChildPos][1] < current[1] :
                self._heap[position] = self._heap[minChildPos]
                self._index[self._heap[position][0]] = position
                position = minChildPos
                minChildPos = PQ._left(position)
            else :        
                 break
        self._heap[position] = current
        self._index[self._heap[position][0]] = position


