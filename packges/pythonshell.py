import os
# import subprocess

"""
python调用shell"""

docname = "./test.doc"
cmd = "unoconv -f html %s" %docname
# result = subprocess.run(cmd)
os.system(cmd)
# print(result)