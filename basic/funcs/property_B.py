class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


c = C()
# c.x.
print(c.x)
c.x = 1  # 触发     @x.setter  def x(self, value):
print(c.x)
