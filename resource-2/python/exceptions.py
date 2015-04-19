class A(Exception):
	pass

def ig1():
	raise A

def ig2():
	try:
		ig1()
	except A:
		## add something ;)
