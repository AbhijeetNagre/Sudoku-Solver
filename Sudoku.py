# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:56:05 2019

@author: Sajag PC
"""

import collections 

class Sudoku:
    
    def fromStringList(strings): 
        arr = [[int(c) for c in s] for s in strings]
        
        print(type(arr))
        
        return Sudoku(arr)
    
    def __init__(self, arr) :        
        self._arr = [[arr[j][i] for i in range(9)] for j in range(9)]
        
    
    def generate(self, row,col, val) :
        
        nextPlot = Sudoku(self._arr)        
        nextPlot._arr[row][col] = val
        
        return nextPlot
    
    def isValid(self) :
        
        # Check if duplicate in any row
        duplicate = any([isDuplicate(row) for row in self._arr])
        
        if(duplicate) :
            return False

        # Check if duplicate in any column        
        duplicate = any([isDuplicate([self._arr[row][col] for row in range(9)]) for col in range(9)])
        
        if(duplicate) :
            return False
        
        zones = [self.getList(row * 3,col * 3) for row in range(3) for col in range(3)]
        #print('zone ', zones)
        
        duplicate = any(isDuplicate(zone)  for zone in zones)
        
        return duplicate == False            
    
    def getList(self,row, col):        
        
        return [self._arr[row]    [col], self._arr[row]    [col + 1],self._arr[row]    [col + 2],
                    self._arr[row + 1][col], self._arr[row + 1][col + 1],self._arr[row + 1][col + 2],
                    self._arr[row + 2][col], self._arr[row + 2][col + 1],self._arr[row + 2][col + 2]]
        
        
    def allFilled(self) :
        return False == any([any([self._arr[row][col] == 0 for row in range(9)]) for col in range(9)]) 

    def display(self) :
        for i in range(9):
            print(self._arr[i])
        
    def nextEmptyCell(self) :
        for i in range(9) :
            for j in range(9) :
                if(self._arr[i][j] == 0) :
                    return i,j
    
   
    
def isDuplicate(collection) :
        collection = [x for x in collection if x > 0]
        return len(collection) > len(set(collection))
    
    
    
def solve(plot) :
    
    plots = collections.deque([plot])
    
    while len(plots) > 0 :
        
        print('length of the queue : ', len(plots))
        
        #last = plots[len(plots)]
        last = plots.pop()
    
        #print('Current Plot : ', last.display())
        
        #x = input('temp')
        
        if(last.isValid()) :
            
            if(last.allFilled()) :
                print('Final solution')
                last.display()
                return
            
            r,c = last.nextEmptyCell()
        
            plots.extend([last.generate(r,c,i) for i in range(1,10)])
    
    print('No solution to this game.')
    
   
    
game = [ [0,2,7,5,0,1,9,8,4],
         [0,1,3,0,0,9,2,0,0],
         [0,0,4,0,0,7,6,0,0],
         
         [0,7,5, 4,0,0, 8,3,2],
         [3,0,0,0,1,8,7,0,0],
         [0,0,8,0,5,0,1,0,0],
    
         [0,3,6,1,8,5,0,0,9],
         [0,0,0,0,0,0,3,7,0],
         [9,8,0,3,0,0,0,0,0]]

game2 = ['027501984',
         '013009200',
         '004007600',
         
         '075400832',
         '300018700',
         '008050100',
    
         '036185009',
         '000000370',
         '980300000']

game2 = Sudoku.fromStringList(game2)

game2 = Sudoku(game2)

solve(game2)
