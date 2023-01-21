# Find-Longest-Path-v2
## Summary
This program finds and highlights the longest path in a matrix of numbers. The longest path has to be the same number and can be from any direction adjacent to the matrix entry including corners. This is v2 of Find the Longest Path. It's GUI implementation is the same as v1 but the algorithm is different. 

For more information on the algorithm, please go to and main.py and Implementation (Algorithm).

Developed Using Python 3.1.2 & Conda 4.12.0

<details>
<summary> Input </summary>
This program takes in a csv file of numbers. Numbers may be different. Above are some acceptable csv file examples.

Condition:  
- Every row must have the same amount of numbers
* Must be numbers
+ Letters, symbols, signs, etc. are unacceptable
</details>

<details>
  <summary> Output </summary>
  Longest path is highlighted in the GUI application. If there are 2 longest path, then the one that is found the earliest is highlighted.
  
  | Example 1 | Example 2 | Example 3 | Example 4 |
  | --------- | --------- | --------- | --------- |
  | ![Screen Shot 2023-01-21 at 6 13 25 PM](https://user-images.githubusercontent.com/115419534/213892342-b98024e5-6e36-4254-9b9a-7345ee62ad60.png) | ![Screen Shot 2023-01-07 at 3 28 43 PM](https://user-images.githubusercontent.com/115419534/211169431-90bf60ca-7dcd-45cf-a5cb-28b61a28b480.png) | ![Screen Shot 2023-01-07 at 3 29 03 PM](https://user-images.githubusercontent.com/115419534/211169433-6f478410-da0c-45ba-a1b6-1e4c2374e0d5.png) | ![Screen Shot 2023-01-07 at 3 29 19 PM](https://user-images.githubusercontent.com/115419534/211169435-f56d9af0-88ee-45c0-8ba7-9aa878f9b1bd.png) |



</details>

<details>
<summary> Implementation (Algorithm) </summary> 
  <details>
    <summary> Adjacency </summary>
    The algorithm operates on every equal and adjacent entry of a current entry. The location of an adjacent entry has an associated direction denoted by a letter. The following table depicts it.  
    
  | A | B | C |
  | - | - | - |
  | D | x | - |
  | - | - | - |.
  
  'A', 'B', 'C', 'D' represents potential adjacent entry and 'x' represents the current entry. In this version, the definition of an adjacent entry is any equal, entry to the 'A', 'B', 'C', or 'D' direction of an entry. The '-' represents entries in those directions but those are not accounted for. The algorithm ignores those entries, no matter if they are the same or not, due to the nature of the algorithm. The algorithm uses a bottom-up like approach so processing those entries are not necessary.
  
  </details>
  <details>
    <summary> Length Matrix </summary>
    The Length Matrix is an alternative matrix created for the algorithm to be dependent on. It is the same size as the original matrix but it's entries are different. The Length Matrix is declared with each entry containing a dictionary: {"A":1, "B":1, "C":1, "D":1}. The letters represents the direction and the number represents the length in the corresponding direction.
  </details>
  
  <details>
    <summary> Algorithm </summary>
    The algoirthm uses a bottom-up approach. It traverses through the matrix top-down and left-right. For each current entry, all adjacent matrices with their corresponding lengths are obtained. It is then processed by updating the length in the same direction in the Length Matrix of the current entry. The length is updated using the adjacent entry's length plus 1.  For example, take the following matrix:  
    
    | 0 | 1 |
    | 0 | 1 |
   
   After traversing through the 1st row, nothing will change. Next traversal will be on the row 2, column 1. Before the processing, the Length Matrix in row 2, column 1 is {"A":1, "B":1, "C":1, "D":1}. After processing, the Length Matrix in row 2, column 1 will be {"A":1, "B":2, "C":1, "D":1}.  
   
   While traversing and updating the whole matrix, the algorithm keeps track of the row, column, and direction of the longest length. When the travseral is completed, the information of the longest length is used to obtain all of the coordinates of the longest path. It is then fed to the MainWindow class and transform the GUI.
   
  </details>
</details>
