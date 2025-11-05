import sys

def is_integer(object: any) -> bool:
	try:
		int(sys.argv[1])
	except Exception as err:
		return False
	return True

def start():
	sys.tracebacklimit = 0
	if len(sys.argv) > 2:
		assert False, "more than one argument is provided"
	elif len(sys.argv) < 2:
		exit(1)
	assert(is_integer(sys.argv[1])), "argument is not an integer"

def parity(x:int):
	if x % 2 :
		print("I'm Odd.")
	else:
		print("I'm Even.")

def main():
	start()
	parity(int(sys.argv[1]))

main()





