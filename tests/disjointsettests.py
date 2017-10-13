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
from disjointsets import DisjointSets

class TestDisjointSets(unittest.TestCase) :

    def test_one(self):
        ds = DisjointSets(1)
        self.assertEqual(ds.find_set(0),0)
        self.assertEqual(ds.find_set(0),0)

    def test_two(self):
        ds = DisjointSets(2)
        self.assertEqual(ds.find_set(0),0)
        self.assertEqual(ds.find_set(0),0)
        self.assertEqual(ds.find_set(1),1)
        self.assertEqual(ds.find_set(1),1)
        ds.union(0,1)
        self.assertEqual(ds.find_set(0),ds.find_set(1))
        self.assertEqual(ds.find_set(0),ds.find_set(1))

    def test_one_at_a_time(self) :
        ds = DisjointSets(16)
        for i in range(16) :
            self.assertEqual(ds.find_set(i),i)
        for to in range(1,16) :
            ds = DisjointSets(16)
            for i in range(1,to+1) :
                ds.union(0,i)
            for i in range(16) :
                if i <= to :
                    self.assertEqual(ds.find_set(0),ds.find_set(i))
                else :
                    self.assertEqual(ds.find_set(i),ds.find_set(i))
            for i in range(16) :
                if i <= to :
                    self.assertEqual(ds.find_set(0),ds.find_set(i))
                else :
                    self.assertEqual(ds.find_set(i),ds.find_set(i))

    def test_two_at_a_time(self) :
        ds = DisjointSets(16)
        for i in range(0,16,2) :
            ds.union(i,i+1)
        for i in range(15) :
            if i%2==0:
                self.assertEqual(ds.find_set(i),ds.find_set(i+1))
            else :
                self.assertNotEqual(ds.find_set(i),ds.find_set(i+1))
            for j in range(i+2,16) :
                self.assertNotEqual(ds.find_set(i),ds.find_set(j))
        for i in range(15) :
            if i%2==0:
                self.assertEqual(ds.find_set(i),ds.find_set(i+1))
            else :
                self.assertNotEqual(ds.find_set(i),ds.find_set(i+1))
            for j in range(i+2,16) :
                self.assertNotEqual(ds.find_set(i),ds.find_set(j))
        ds = DisjointSets(16)
        for i in range(0,16,2) :
            ds.union(i,i+1)
        for i in range(0,16,4) :
            ds.union(i+1,i+2)
        for i in range(15) :
            for j in range(i+1,16) :
                if i//4 == j//4 :
                    self.assertEqual(ds.find_set(i),ds.find_set(j))
                else :
                    self.assertNotEqual(ds.find_set(i),ds.find_set(j))
        ds = DisjointSets(16)
        for i in range(0,16,2) :
            ds.union(i,i+1)
        for i in range(0,16,4) :
            ds.union(i+1,i+2)
        for i in range(0,16,8) :
            ds.union(i+3,i+6)
        for i in range(15) :
            for j in range(i+1,16) :
                if i//8 == j//8 :
                    self.assertEqual(ds.find_set(i),ds.find_set(j))
                else :
                    self.assertNotEqual(ds.find_set(i),ds.find_set(j))
        ds = DisjointSets(16)
        for i in range(0,16,2) :
            ds.union(i,i+1)
        for i in range(0,16,4) :
            ds.union(i+1,i+2)
        for i in range(0,16,8) :
            ds.union(i+3,i+6)
        ds.union(0,15)
        for i in range(15) :
            for j in range(i+1,16) :
                self.assertEqual(ds.find_set(i),ds.find_set(j))
    
        


if __name__ == '__main__':
    unittest.main()    
