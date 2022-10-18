"""
Pip is a package management system that is used to install
and uninstall packages in python for use.

Example: before you can use numpy for data analysis you need
to install it first using pip then import for use.

syntax:

In PC terminal: pip install package-name
e.g. pip install numpy

After install, you can then import the package into your
working file for use

"""

import numpy as np #np is an alias
test_array = np.array( [ [3,4,5],[7,5,8] ])
print(test_array)
