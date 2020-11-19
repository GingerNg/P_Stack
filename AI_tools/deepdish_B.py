import deepdish as dd
import numpy as np
####  序列化和反序列化工具
# https://pypi.org/project/deepdish/0.3.2/
# pip3 install deepdish
#  save and load all kinds of data as HDF5s
# sudo apt install hdf5-tools
# Easy to inspect the content from the command line (using h5ls or our specialized tool ddls)

# ddls test.h5
# /foo                  array (10, 20) [float64]
# /sub                  dict
# /sub/bar              'a string' (8) [unicode]
# /sub/baz              1.23 [float64]
####
d = {
    'foo': np.ones((10, 20)),
    'sub': {
        'bar': 'a string',
        'baz': 1.23,
    },
}
dd.io.save('test.h5', d)
