# A python-based visual tool for pairwise sequence alignment

## Goals: 
This is the python-based tool for pairwise sequence alignment by using TKinter as python library binding to the Tk GUI toolkit. The code can be executed through Jupyter notebook.

## Installation
Sections below describe the anaconda installation as an environment for execute the code. Anaconda is a open-source distribution of the Python and R programming languages that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS. Manual instalation links are as follow:

[Installing on windows](https://docs.anaconda.com/anaconda/install/windows/)

[Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)

[Installing on Linux](https://docs.anaconda.com/anaconda/install/linux/)

You might have to install numpy packages in anaconda environment before executing the code. The steps are: open Anaconda, select the Environment tab, select base (root), look for Numpy and tick the boxes next to it, click apply, and check/confirm the changes. Cek this [link](https://www.youtube.com/watch?v=kOpW-CeHzJQ) for the visual step.

## Code Execution
After installing the package, open Anaconda navigator and launch Jupyter notebook. The web application component of the notebook will be hosted on your local computer and the notebook document will save to a file directory on your local computer. It may take some time for the notebook to open in a browser window. Download the code file [Tkinter-BABA_final.ipynb](https://github.com/neo-ewha/bioinformatics-tools/blob/main/Tkinter-BABA_final.ipynb) and select this items from the files part of jupyter notebook window. You can execute the contents of a cell code by using Shift-Enter, clicking the Play button in the toolbar, or Run icons in the menu bar.

## Interface Performance
Once the code is executed, there will be a window where users can choose whether to use NW or SW algorithm to align two sequences. Below are some important steps. 
1. Click radio buttons labelled with name of the algorithm.
2. Input two pairs of sequences and a penalty gap value manually or copy-paste from other resources.
3. Click the execution tab for filling the initial values that hold the role of a boundary condition.
4. Repeatedly click the next button, ‘>’, to fill in the score of each matrix’s element.
5. Click  the back button, ‘<’,  for a glimpse of the prior calculation.
6. Continuously click the next button until the last element, and the traceback process is then started resulting the optimal alignment.
7. There are also '>>' and '<<' buttons to run the whole process without repeating clicking the previously mentioned buttons.

The demo video for these steps can be downloaded [here](https://github.com/neo-ewha/bioinformatics-tools/blob/main/VideoDemo.mp4).
