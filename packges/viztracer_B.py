########
# VizTracer is a low-overhead logging/debugging/profiling tool that can trace and visualize your python code execution.
# https://github.com/gaogaotiantian/viztracer
##########

from viztracer import VizTracer

tracer = VizTracer()
tracer.start()
# Something happens here
a = [1] * (10 ** 6)
tracer.stop()
tracer.save() # also takes output_file as an optional argument
