from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc_(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(2, 1, 2) == 3
  assert simple_work_calc(1, 7, 2) == 1
  assert simple_work_calc(3, 2, 2) == 5

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(1, 5, 4, lambda n: 2 * n) == 1
  assert work_calc(3, 1, 2, lambda n: 2 * n) == 7
  assert work_calc(2, 1, 2, lambda n: n) == 3

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
  work_fn1 = lambda n: 1
  work_fn1=lambda n: 2 * work_fn1(n//2) + work_fn1(n)
	# create work_fn2
  work_fn2 = lambda n: 1
  work_fn2 = lambda n: 2 * work_fn2(n//2) + work_fn2(n*n)
  
  res = compare_work(work_fn1, work_fn2)
	print(res)

	
def test_compare_span():
  assert span_calc(10, 2, 2, lambda n: 1) == 15
  assert span_calc(20, 1, 2, lambda n: n * n) == 530
  assert span_calc(30, 3, 2, lambda n: n) == 300
