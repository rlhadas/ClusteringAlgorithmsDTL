import nni

pg = lambda g : nni.pprint(dict(g))
T12 = nni.test_conjecture(6, 1000)
T100 = nni.test_conjecture(100, 1000)
