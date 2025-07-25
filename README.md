# Suffolk and North East Essex Integrated Care System

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/pypi/pyversions/sneeifstyles.svg)](https://pypi.org/project/sneeifstyles/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/ambv/black)


## SNEE_utils

SNEE_utils is a python package that could be reused from analysts working within the Suffolk and north east Essex Intelligence Function. Repositories in this organisation are created and maintained by analysts working in the [SNEE Intelligence function](https://www.sneeics.org.uk/can-do-health-and-care/creative/knowledge-and-intelligence/) hub.
<br>
It contains two child packages:

### 1. Python Utility Functions : py_utils

 - nb_html_export.py --> This python file contains a set of convenience function to convert notebook to html and add table of contents. This primarily used nbconvert to perform the conversion and bs4 to insert the table of contents.

### 2. SNEE Stylings : snee_styles

- A Python package containing useful functions for implementing SNEE style.

## Installation: How do I install SNEE_utils?

`SNEE_utils` is a parent package that holds both the child packages namely: `py_utils` and `SNEE_styles` Python packages. Installation is using pip:

- It is recommended to use a Virtual Environment
- This will then install the module in your environment, optionally specifying the version

```
pip install git+https://github.com/SNEE-ICS/SNEE_Utils.git
```
or optionally specifying a version:

```
pip install git+https://github.com/SNEE-ICS/SNEE_Utils.git@v0.0.6
```

## How to use py_utils and snee_styles ?

Once the parent package is installed, to use the py_utils or SNEE_styles package in your notebook, use:

```
from py_utils import *

my_notebook = 'Report.ipynb'

# By default this will add table fo content and exclude inputs cells(code)
formatted_html_with_toc = convert_notebook_to_html_string(my_notebok)

# Saves the notebook down to the original file name, but with .html
write_notebook_to_html(formatted_html_with_toc, my_notebook)
```

```
# For Matplotlib and Seaborn Plots
from snee_styles import mpl_styles
mpl_styles()

# For Plotly Plots
from snee_styles import plotly_style
plotly_style()
```

> ⚠️ For Jupyter Notebooks--> Please make sure you run `from snee_styles import mpl_style, plotly_style` and `mpl_style()` `plotly_style` in **code cells** as shown above. 

## What chart types can use SNEE IF Styles?

- Line plots
- Scatter plots
- Bubble plots
- Bar charts
- Pie charts
- Histograms and distribution plots
- 3D surface plots
- Stream plots
- Polar plots

## Examples

To run the examples in [`example.ipynb`](https://github.com/SNEE-ICS/SNEE_Utils/blob/main/snee_styles/example.ipynb), install the required packages using ``pip install -r requirements_notebook.txt`` in a Python virtual environment of your choice.

```python
import matplotlib.pyplot as plt
from snee_styles import mpl_style

def plot():
    mpl_style()
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # the following functions are defined in example.ipynb 
    line_plot(axes[0, 0])
    scatter_plot(axes[0, 1])
    distribution_plot(axes[1, 0])
    ax = plt.subplot(2, 2, 4, projection='polar')
    polar_plot(ax)

plot()
```

### Seaborn or Matplotlib

![png](https://github.com/SNEE-ICS/SNEE_Utils/blob/main/snee_styles/examples/sample_plots.png)

### Plotly

Plotly example plots can be viewed by clicking the link below:

[Line Plot](snee_styles/examples/0.plotly.html)<br>
[Scatter Plot](snee_styles/examples/1.plotly.html)<br>
[Distribution Plot](snee_styles/examples/2.plotly.html)<br>

## What license do you use?

QB Styles is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
<br>
Contributions to code and issues are welcome.
<hr>