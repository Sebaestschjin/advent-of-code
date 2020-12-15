# from https://gist.github.com/fragmuffin/a245f59bdcd457936c3b51aa2ebb3f6c#file-runtests-py-L42

def testlabel(*labels):
    """
    Usage::
        @testlabel('quick')
        class MyTest(unittest.TestCase):
            def test_foo(self):
                pass
    """

    def inner(cls):
        # append labels to class
        cls._labels = set(labels) | getattr(cls, '_labels', set())

        return cls

    return inner
