# a python-based visual tool for pairwise sequence alignment
## Goals: 
This is the python-based tool for pairwise sequence alignment by using TKinter as python library binding to the Tk GUI toolkit.
### Performance
We've applied the Needleman-Wunsh (NW) and Smith-Waterman methods (SW) to align two sequences. Once the code is executed, there will be a window where users can choose whether to use NW or SW algorithm. 
1. Click radio buttons labelled with name of the algorithm
2. Input two pairs of sequences and a penalty gap value manually or copy-paste from other resources
3. Click the execution tab for filling the initial values that hold the role of a boundary condition
4. Repeatedly click the next button, ‘>’, to fill in the score of each matrix’s element
5. Click  the back button, ‘<’,  for a glimpse of the prior calculation
6. Continuously click the next button until the last element, and the traceback process is then started resulting the optimal alignment

### The demo video can be downloaded here: 
https://github.com/neo-ewha/bioinformatics-tools/blob/main/Demo.mp4
