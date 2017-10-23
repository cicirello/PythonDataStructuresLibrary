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

import sys
sys.path.append('../lib')

import unittest
from pq import PQ
from pq import MaxPQ
from random import randrange

class TestPQMethods(unittest.TestCase) :

    def test_empty(self) :
        q = PQ()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_one_element(self) :
        q = PQ()
        q.add("a", 5)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertEqual(q.get_priority("a"), 5)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.change_priority("a", 3))
        self.assertEqual(q.get_priority("a"), 3)
        self.assertTrue(q.change_priority("a", 10))
        self.assertEqual(q.get_priority("a"), 10)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertEqual(q.extract_min(), "a")
        self.assertFalse(q.contains("a"))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_two_elements_added_in_order(self) :
        q = PQ()
        q.add("a", 5)
        q.add("b", 15)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertEqual(q.get_priority("a"), 5)
        self.assertEqual(q.get_priority("b"), 15)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.change_priority("a", 3))
        self.assertEqual(q.get_priority("a"), 3)
        self.assertTrue(q.change_priority("a", 10))
        self.assertEqual(q.get_priority("a"), 10)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.change_priority("a", 20))
        self.assertEqual(q.get_priority("a"), 20)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.change_priority("a", 11))
        self.assertEqual(q.get_priority("a"), 11)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))

        self.assertEqual(q.extract_min(), "a")
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertFalse(q.contains("a"))
        self.assertTrue(q.contains("b"))

        self.assertEqual(q.extract_min(), "b")
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.contains("a"))
        self.assertFalse(q.contains("b"))

    def test_two_elements_added_out_of_order(self) :
        q = PQ()
        q.add("b", 15)
        q.add("a", 5)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertEqual(q.get_priority("a"), 5)
        self.assertEqual(q.get_priority("b"), 15)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.change_priority("a", 3))
        self.assertEqual(q.get_priority("a"), 3)
        self.assertTrue(q.change_priority("a", 10))
        self.assertEqual(q.get_priority("a"), 10)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.change_priority("a", 20))
        self.assertEqual(q.get_priority("a"), 20)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.change_priority("a", 11))
        self.assertEqual(q.get_priority("a"), 11)
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))

        self.assertEqual(q.extract_min(), "a")
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertFalse(q.contains("a"))
        self.assertTrue(q.contains("b"))

        self.assertEqual(q.extract_min(), "b")
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.contains("a"))
        self.assertFalse(q.contains("b"))

    def test_three_elements_added_in_order(self) :
        q = PQ()
        q.add("a", 5)
        q.add("b", 15)
        q.add("c", 25)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertEqual(q.get_priority("a"), 5)
        self.assertEqual(q.get_priority("b"), 15)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 3))
        self.assertEqual(q.get_priority("a"), 3)
        self.assertTrue(q.change_priority("a", 10))
        self.assertEqual(q.get_priority("a"), 10)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 20))
        self.assertEqual(q.get_priority("a"), 20)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 11))
        self.assertEqual(q.get_priority("a"), 11)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 30))
        self.assertEqual(q.get_priority("a"), 30)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 9))
        self.assertEqual(q.get_priority("a"), 9)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))

        self.assertEqual(q.extract_min(), "a")
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertFalse(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))

        self.assertEqual(q.extract_min(), "b")
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "c")
        self.assertFalse(q.contains("a"))
        self.assertFalse(q.contains("b"))
        self.assertTrue(q.contains("c"))

        self.assertEqual(q.extract_min(), "c")
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.contains("a"))
        self.assertFalse(q.contains("b"))
        self.assertFalse(q.contains("c"))

    def test_three_elements_added_out_of_order(self) :
        q = PQ()
        q.add("c", 25)
        q.add("b", 15)
        q.add("a", 5)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertEqual(q.get_priority("a"), 5)
        self.assertEqual(q.get_priority("b"), 15)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 3))
        self.assertEqual(q.get_priority("a"), 3)
        self.assertTrue(q.change_priority("a", 10))
        self.assertEqual(q.get_priority("a"), 10)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 20))
        self.assertEqual(q.get_priority("a"), 20)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 11))
        self.assertEqual(q.get_priority("a"), 11)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 30))
        self.assertEqual(q.get_priority("a"), 30)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))
        self.assertTrue(q.change_priority("a", 9))
        self.assertEqual(q.get_priority("a"), 9)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))

        self.assertEqual(q.extract_min(), "a")
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "b")
        self.assertFalse(q.contains("a"))
        self.assertTrue(q.contains("b"))
        self.assertTrue(q.contains("c"))

        self.assertEqual(q.extract_min(), "b")
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_min(), "c")
        self.assertFalse(q.contains("a"))
        self.assertFalse(q.contains("b"))
        self.assertTrue(q.contains("c"))

        self.assertEqual(q.extract_min(), "c")
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.contains("a"))
        self.assertFalse(q.contains("b"))
        self.assertFalse(q.contains("c"))

    def test_many_elements_added_in_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]

        q = PQ()
        for i in range(len(els)) :
            q.add(els[i], priorities[i])
            self.assertEqual(q.size(), i+1)
            self.assertTrue(q.contains(els[i]))
        for i in range(len(els)) :
            self.assertEqual(q.peek_min(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_min(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_init_elements_in_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]
        pairs = [ (els[i], priorities[i]) for i in range(len(els))]

        q = PQ(pairs)
        self.assertEqual(q.size(), len(els))
        for i in range(len(els)) :
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_min(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_min(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_init_elements_out_of_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]
        pairs = [ (els[i], priorities[i]) for i in range(-1,-len(els)-1,-1)]

        q = PQ(pairs)
        self.assertEqual(q.size(), len(els))
        for i in range(len(els)) :
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_min(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_min(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_init_elements_random_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]
        pairs = [ (els[i], priorities[i]) for i in range(len(els))]

        for r in range(len(pairs),0,-1) :
            j = randrange(r)
            i = r-1
            if i != j :
                pairs[i],pairs[j] = pairs[j],pairs[i]
            
        q = PQ(pairs)
        self.assertEqual(q.size(), len(els))
        for i in range(len(els)) :
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_min(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_min(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_elements_added_out_of_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]

        q = PQ()
        for i in range(-1,-len(els)-1,-1) :
            q.add(els[i], priorities[i])
            self.assertEqual(q.size(), -i)
            self.assertTrue(q.contains(els[i]))
        for i in range(len(els)) :
            self.assertEqual(q.peek_min(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_min(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_elements_random_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]

        for r in range(len(els),0,-1) :
            j = randrange(r)
            i = r-1
            if i != j :
                els[i],els[j] = els[j],els[i]
                priorities[i],priorities[j] = priorities[j],priorities[i]

        q = PQ()
        for i in range(len(els)) :
            q.add(els[i], priorities[i])
            self.assertEqual(q.size(), i+1)
            self.assertTrue(q.contains(els[i]))
        els.sort()
        priorities.sort()
        for i in range(len(els)) :
            self.assertEqual(q.peek_min(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_min(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_elements_change_priority(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]

        q = PQ()
        for i in range(len(els)) :
            q.add(els[i], priorities[i])
        for p in range(7,58,5) :
            self.assertTrue(q.change_priority("a", p))
            self.assertEqual(q.get_priority("a"), p)
            if p > 10 :
                self.assertEqual(q.peek_min(), "b")
            else :
                self.assertEqual(q.peek_min(), "a")
        for p in range(56,0,-5) :
            self.assertTrue(q.change_priority("a", p))
            self.assertEqual(q.get_priority("a"), p)
            if p > 10 :
                self.assertEqual(q.peek_min(), "b")
            else :
                self.assertEqual(q.peek_min(), "a")
        self.assertEqual(q.peek_min(), "a")
        self.assertTrue(q.change_priority("a", 27))
        for i in range(1,5) :
            self.assertEqual(q.extract_min(), els[i])
        self.assertEqual(q.extract_min(), "a")
        for i in range(5,len(els)) :
            self.assertEqual(q.extract_min(), els[i])
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_remove(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*x for x in range(1,11)]

        for cap in range(1,len(els)+1) :
            for removeMe in range(cap) :
                q = PQ()
                for i in range(cap) :
                    q.add(els[i], priorities[i])
                q.remove(els[removeMe])
                self.assertEqual(q.size(), cap-1)
                for i in range(cap) :
                    if i==removeMe :
                        self.assertFalse(q.contains(els[i]))
                    else :
                        self.assertTrue(q.contains(els[i]))
                        self.assertEqual(q.get_priority(els[i]), priorities[i])
                for i in range(cap) :
                    if i!=removeMe :
                        self.assertEqual(q.extract_min(), els[i])


            
class TestMaxPQMethods(unittest.TestCase) :

    def test_empty(self) :
        q = MaxPQ()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_one_element(self) :
        q = MaxPQ()
        q.add("a", 5)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_max(), "a")
        self.assertTrue(q.contains("a"))
        self.assertEqual(q.get_priority("a"), 5)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_max(), "a")
        self.assertTrue(q.contains("a"))
        self.assertTrue(q.change_priority("a", 3))
        self.assertEqual(q.get_priority("a"), 3)
        self.assertTrue(q.change_priority("a", 10))
        self.assertEqual(q.get_priority("a"), 10)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.peek_max(), "a")
        self.assertTrue(q.contains("a"))
        self.assertEqual(q.extract_max(), "a")
        self.assertFalse(q.contains("a"))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_elements_added_in_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]

        q = MaxPQ()
        for i in range(len(els)) :
            q.add(els[i], priorities[i])
            self.assertEqual(q.size(), i+1)
            self.assertTrue(q.contains(els[i]))
        for i in range(len(els)) :
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_max(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_max(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_init_elements_in_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]
        pairs = [ (els[i], priorities[i]) for i in range(len(els))]

        q = MaxPQ(pairs)
        self.assertEqual(q.size(), len(els))
        for i in range(len(els)) :
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_max(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_max(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_init_elements_out_of_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]
        pairs = [ (els[i], priorities[i]) for i in range(-1,-len(els)-1,-1)]

        q = MaxPQ(pairs)
        self.assertEqual(q.size(), len(els))
        for i in range(len(els)) :
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_max(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_max(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_init_elements_random_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]
        pairs = [ (els[i], priorities[i]) for i in range(len(els))]

        for r in range(len(pairs),0,-1) :
            j = randrange(r)
            i = r-1
            if i != j :
                pairs[i],pairs[j] = pairs[j],pairs[i]

        q = MaxPQ(pairs)
        self.assertEqual(q.size(), len(els))
        for i in range(len(els)) :
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_max(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_max(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        

    def test_many_elements_added_out_of_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]

        q = MaxPQ()
        for i in range(-1,-len(els)-1,-1) :
            q.add(els[i], priorities[i])
            self.assertEqual(q.size(), -i)
            self.assertTrue(q.contains(els[i]))
        for i in range(len(els)) :
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        for i in range(len(els)) :
            self.assertEqual(q.peek_max(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_max(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_elements_random_order(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]

        for r in range(len(els),0,-1) :
            j = randrange(r)
            i = r-1
            if i != j :
                els[i],els[j] = els[j],els[i]
                priorities[i],priorities[j] = priorities[j],priorities[i]

        q = MaxPQ()
        for i in range(len(els)) :
            q.add(els[i], priorities[i])
            self.assertEqual(q.size(), i+1)
            self.assertTrue(q.contains(els[i]))
        for i in range(len(els)) :
            self.assertEqual(q.get_priority(els[i]), priorities[i])
        els.sort()
        priorities.sort()
        priorities.reverse()
        for i in range(len(els)) :
            self.assertEqual(q.peek_max(), els[i])
            self.assertEqual(q.size(), len(els)-i)
            self.assertTrue(q.contains(els[i]))
            self.assertEqual(q.extract_max(), els[i])
            self.assertEqual(q.size(), len(els)-i-1)
            self.assertFalse(q.contains(els[i]))
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_many_elements_change_priority(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]

        q = MaxPQ()
        for i in range(len(els)) :
            q.add(els[i], priorities[i])
        for p in range(47,0,-5) :
            self.assertTrue(q.change_priority("a", p))
            self.assertEqual(q.get_priority("a"), p)
            if p < 45 :
                self.assertEqual(q.peek_max(), "b")
            else :
                self.assertEqual(q.peek_max(), "a")
        for p in range(3,55,5) :
            self.assertTrue(q.change_priority("a", p))
            self.assertEqual(q.get_priority("a"), p)
            if p < 45 :
                self.assertEqual(q.peek_max(), "b")
            else :
                self.assertEqual(q.peek_max(), "a")
        self.assertEqual(q.peek_max(), "a")
        self.assertTrue(q.change_priority("a", 27))
        for i in range(1,5) :
            self.assertEqual(q.extract_max(), els[i])
        self.assertEqual(q.extract_max(), "a")
        for i in range(5,len(els)) :
            self.assertEqual(q.extract_max(), els[i])
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_remove(self) :
        els = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        priorities = [ 5*(11-x) for x in range(1,11)]

        for cap in range(1,len(els)+1) :
            for removeMe in range(cap) :
                q = MaxPQ()
                for i in range(cap) :
                    q.add(els[i], priorities[i])
                q.remove(els[removeMe])
                self.assertEqual(q.size(), cap-1)
                for i in range(cap) :
                    if i==removeMe :
                        self.assertFalse(q.contains(els[i]))
                    else :
                        self.assertTrue(q.contains(els[i]))
                        self.assertEqual(q.get_priority(els[i]), priorities[i])
                for i in range(cap) :
                    if i!=removeMe :
                        self.assertEqual(q.extract_max(), els[i])

    @unittest.expectedFailure
    def test_peek_min(self) :
        q = MaxPQ()
        q.add("a",5)
        q.peek_min()

    @unittest.expectedFailure
    def test_extract_min(self) :
        q = MaxPQ()
        q.add("a",5)
        q.extract_min()


if __name__ == '__main__':
    unittest.main()    
