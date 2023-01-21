import csv
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QMenuBar, QPushButton, QVBoxLayout, QWidget, QGridLayout

#The class MainWindow is used to generate the GUI by taking in original matrix and longest path from the Matrix class. The class utilizes
#the QGridLayout class.
#1. makeMatrix(matrix, grid): for every corresponding entry of the original matrix, this method creates a Qlabel widget of the same value.
#2. highlight(matrix, grid): traverses through every list in path and obtains the row & column of an entry that should be highlighted. 
#   For every entry that should be highlighted, it creates a new QLabel widget with the same information, but yellow. It then replaces the old
#   uncolored widget with the yellow widget in the same entry.
#3. buttonClicked(): calls highlight() when the user clicks the button "Solve"
class MainWindow(QWidget):
    def __init__(self, matrix, path):
        super().__init__()
        self.matrix = matrix 
        self.path = path
        self.grid = None

        self.resize(200,250)
        self.setWindowTitle('Find Longest Path')  

        self.grid = QGridLayout()  
        self.makeMatrix(matrix, self.grid)

        button = QPushButton("Solve")
        button.clicked.connect(self.buttonClicked)

        layout = QVBoxLayout()
        layout.addLayout(self.grid, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(button)
        layout.setContentsMargins(10,10,10,10)

        self.setLayout(layout)

        self.show()

    def makeMatrix(self, matrix, grid):
        for i in range(len(matrix)):
            for j in range(len(matrix[1])):
                widget = QLabel(str(matrix[i][j]))
                widget.setStyleSheet('color: #002d7c;background-color:white;'
                                     'font-weight: bold;')
                widget.setMargin(10)
                widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
                

                grid.addWidget(widget, i , j)

        grid.setHorizontalSpacing(1)
        grid.setVerticalSpacing(1)
    
    def highlight(self, matrix, grid):
        for i in range(len(self.path)):
            widget = QLabel(str(matrix[self.path[i][0]][self.path[i][1]]))
            widget.setStyleSheet('color: #002d7c;background-color:yellow;'
                                'font-weight: bold;')
            widget.setMargin(10)
            widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.replaceWidget(grid.itemAtPosition(self.path[i][0],self.path[i][1]).widget(), widget)

    def buttonClicked(self):
        self.highlight(self.matrix, self.grid)

#The class Matrix takes in a matrix, finds and produces a list of coordinates of the lognest path in the matrix
#1. createLenMatrix(): creates a default alternative matrix that is the same size as the original matrix. Each entry has the dictionary 
#   {"A":1, "B":1, "C":1, "D":1}. The Letters represents the direction and the number represents the length in the corresponding direction.
#2. getAdjacentEqualEntries(matrix, currentRow, currentCOlumn): generates the row, column, direction of equal entries, in the given directions, 
#   that are adjacent to the current one. 
#3. findLongestPathCoord(row, column, len, dir): takes in the information about the longest length in the len matrix, produces the list of
#   coordinates of the longest path and stores it into the variable path

#4. solveMatrix(): utilizes every above method. It first calls createLenMatrix() and then traverses through the matrix top-down, left-right.
#   For every entry, it calls getAdjacentEqualEntries(). For every adjacent entry, the dictionary of the current entry is updated. The length 
#   in the direction of the adjacent is updated by using the adjacent entries' length in the same direction. While traversing through the 
#   matrix, it keeps track of the information of the longest length and at the end, it calls findLongestPathCoord() using the information.

#The following diagram shows the directions of a matrix
# A | B | C
# D | x | 
#   |   |
class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.numRow = len(matrix)
        self.numColumn = len(matrix[1])
        self.__lenMatrix = []
        self.longestPathRow, self.longestPathColumn, self.longestPathLength, self.longestPathDir = -1, -1, -1, ''
        self.__path = []
        
    def getOriginalMatrix(self):
        return self.matrix
    
    def getLenMatrix(self):
        return self.__lenMatrix

    def getLongestPath(self):
        return self.__path

    def createLenMatrix(self):

        for i in range(self.numRow):
            row = []
            for j in range(self.numColumn):
                allLength = {"A":1, "B":1, "C":1, "D":1}
                row.append(allLength)
            self.getLenMatrix().append(row)
 
    def getAdjacentEqualEntries(self, matrix, currentRow, currentColumn):
        #top left
        if (currentRow-1 != -1 and currentColumn-1 != -1) and matrix[currentRow-1][currentColumn-1] == matrix[currentRow][currentColumn]:
            yield currentRow-1, currentColumn-1, 'A'
        
        #top
        if (currentRow-1 != -1) and matrix[currentRow-1][currentColumn] == matrix[currentRow][currentColumn]:
            yield currentRow-1, currentColumn, 'B'

        #top right
        if (currentRow-1 != -1 and currentColumn+1 != self.numColumn) and matrix[currentRow-1][currentColumn+1] == matrix[currentRow][currentColumn]:
            yield currentRow-1, currentColumn+1, 'C'
        
        #left
        if (currentColumn-1 != -1) and matrix[currentRow][currentColumn-1] == matrix[currentRow][currentColumn]:
            yield currentRow, currentColumn-1, 'D'
        
    def findLongestPathCoord(self, row, column, len, dir):
        if dir == 'A':
            for i in range(len):
                self.getLongestPath().append([row,column])
                row -=1
                column -=1
        elif dir == 'B':
            for i in range(len):
                self.getLongestPath().append([row,column])
                row -= 1
        elif dir == 'C':
            for i in range(len):
                self.getLongestPath().append([row, column])
                row -= 1
                column += 1
        elif dir == 'D':
            for i in range(len):
                self.getLongestPath().append([row, column])
                column -=1

    def solveMatrix(self):
        self.createLenMatrix()

        for currRow in range(self.numRow):
            for currColumn in range(self.numColumn):
                currEntry = self.getLenMatrix()[currRow][currColumn]
                for adjRow, adjColumn, direction in self.getAdjacentEqualEntries(self.matrix, currRow, currColumn):
                    adjEntry = self.getLenMatrix()[adjRow][adjColumn]
                    currEntry[direction] = adjEntry.get(direction)+1
                if (max(currEntry.values()) > self.longestPathLength):
                    self.longestPathRow = currRow
                    self.longestPathColumn = currColumn
                    self.longestPathLength = max(currEntry.values())
                    self.longestPathDir = max(currEntry, key=currEntry.get)
        
        self.findLongestPathCoord(self.longestPathRow, self.longestPathColumn, self.longestPathLength, self.longestPathDir)
            
def main():
    matrix = Matrix(list(csv.reader(open(sys.argv[1], 'r'))))
    matrix.solveMatrix()
    app = QApplication(sys.argv)
    window = MainWindow(matrix.getOriginalMatrix(), matrix.getLongestPath())
    window.show()
    app.exec()

main()
