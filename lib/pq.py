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


class PQ :
    """A Priority Queue (PQ) implemented with a binary heap.

    A binary min heap is used to implement a PQ.  A python dictionary, i.e., associative array,
    is used to enable changing priorities, as well as removal of any element, in O(lg N) time.

    Elements must be of a hashable type (due to use of Python dictionary).  However, be careful
    when mutating state of an element that is already in the PQ, and don't change any element property
    that is used in generating the hash or else you will break the PQ.

    Assuming a PQ with N elements, the runtimes of the operations are as follows.

    The following operations run in O(lg N) time: add, extract_min, change_priority, remove

    The following operations run in O(1) time: peek_min, contains, get_priority, size, is_empty
    """

    def __init__(self) :
        """Initialize an empty PQ."""
        
        self._heap = []
        self._index = {}


    def size(self) :
        """Size of the PQ."""
        
        return len(self._heap)
    

    def is_empty(self) :
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
        self._percolate_up(position)
        return True

    

    def peek_min(self) :
        """Returns, but does not remove, the element with the minimum priority value."""
        
        return self._heap[0][0]

    

    def extract_min(self) :
        """Removes and returns the element with minimum priority value."""
        
        minElement = self._heap[0][0]
        oldLast = self._heap.pop()
        if len(self._heap) > 0 :
            self._heap[0] = oldLast
            self._percolate_down(0)
        del self._index[minElement]
        return minElement
    


    def contains(self, element) :
        """Returns True if element is in the PQ and False otherwise.

        Keyword arguments:
        element -- The element
        """
        
        return element in self._index
    


    def get_priority(self, element) :
        """Gets the current priority of the specified element.

        Keyword arguments:
        element -- The element
        """
        
        return self._heap[self._index[element]][1]
    


    def change_priority(self, element, value) :
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
            self._percolate_up(position)
        elif self._heap[position][1] < value :
            self._heap[position] = (element, value)
            self._percolate_down(position)
        return True


    def remove(self, element) :
        """Removes a specified element from the PQ.

        Removes a specified element from the PQ, if it is present.
        Returns True if element removed, and False if not present in PQ.

        Keyword arguments:
        element -- The element to remove.
        """

        if not self.contains(element) :
            return False
        position = self._index[element]
        del self._index[element]
        if len(self._heap) == 1 :
            self._heap.pop()
        elif position == len(self._heap)-1 :
            self._heap.pop()
        else :
            self._heap[position] = self._heap.pop()
            self._index[self._heap[position][0]] = position
            if position > 0 and self._heap[position][1] < self._heap[PQ._parent(position)][1] :
                self._percolate_up(position)
            else :
                self._percolate_down(position)
        return True
        
   

    def _left(i) :
        return 2*i+1

    def _right(i) :
        return 2*i+2

    def _parent(i) :
        return (i-1)//2

    def _ancestor(i,a) :
        # a=0 is itself, a=1 is parent, a=2 is grandparent, etc
        po2 = 1 << a
        return (i-po2+1)//po2

    def _tree_level(i) :
        return (i+1).bit_length()-1

    def _percolate_up(self, position) :
        element, value = self._heap[position]
        p = PQ._parent(position)
        while p >= 0 and self._heap[p][1] > self._heap[position][1] :
            self._heap[position] = self._heap[p]
            self._index[self._heap[position][0]] = position
            self._heap[p] = (element, value)
            position = p
            p = PQ._parent(position)
        self._index[element] = position

    def _percolate_down(self, position) :
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



    warnings.simplefilter("module")
    def changePriorityValue(self, element, value) :
        """Deprecated"""
        
        warnings.warn("changePriorityValue is replaced with change_priority", DeprecationWarning)

        return self.change_priority(element, value)

    def getPriorityValue(self, element) :
        """Deprecated"""

        warnings.warn("getPriorityValue is replaced with get_priority", DeprecationWarning)
        return self.get_priority(element)

    def extractMin(self) :
        """Deprecated"""

        warnings.warn("extractMin is replaced with extract_min", DeprecationWarning)
        return self.extract_min()

    def peekMin(self) :
        """Deprecated"""
        
        warnings.warn("peekMin is replaced with peek_min", DeprecationWarning)
        return self.peek_min()

    def isEmpty(self) :
        """Deprecated"""

        warnings.warn("isEmpty is replaced with is_empty", DeprecationWarning)
        return self.is_empty()


class MaxPQ(PQ) :
    """A Priority Queue (PQ), with elements extracted max first, implemented with a binary heap.

    A binary max heap is used to implement MaxPQ.  A python dictionary, i.e., associative array,
    is used to enable changing priorities, as well as removal of any element, in O(lg N) time.

    Elements must be of a hashable type (due to use of Python dictionary).  However, be careful
    when mutating state of an element that is already in the PQ, and don't change any element property
    that is used in generating the hash or else you will break the PQ.

    Assuming a PQ with N elements, the runtimes of the operations are as follows.

    The following operations run in O(lg N) time: add, extract_max, change_priority, remove

    The following operations run in O(1) time: peek_max, contains, get_priority, size, is_empty
    """

    def add(self, element, value) :
        return super().add(element, -value)

    def peek_min(self) :
        """peek_min is not supported in a MaxPQ."""
        
        raise NotImplementedError("peek_min is not supported in a MaxPQ.")

    def extract_min(self) :
        """extract_min is not supported in a MaxPQ."""
        
        raise NotImplementedError("extract_min is not supported in a MaxPQ.")

    def peek_max(self) :
        """Returns, but does not remove, the element with the maximum priority value."""
        
        return super().peek_min()

    def extract_max(self) :
        """Removes and returns the element with maximum priority value."""
        
        return super().extract_min()

    def get_priority(self, element) :
        return -super().get_priority(element)

    def change_priority(self, element, value) :
        return super().change_priority(element, -value)
    
