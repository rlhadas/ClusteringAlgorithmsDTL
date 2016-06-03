import nni

T = nni.test_conjecture(6, 1000)

if T is None:
    print "no counterexamples found"
else:
    print "counterexample found!"
