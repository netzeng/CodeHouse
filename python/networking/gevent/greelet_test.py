# coding:utf-8
from greenlet import greenlet

def test1(x, y):
    z = gr2.switch(x+y)
    print 'z', z

def test2(u):
    print 'u', u
    gr1.switch(42)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch("hello", " world")