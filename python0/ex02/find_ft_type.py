def all_thing_is_obj(object: any) -> int:
	if isinstance(object, tuple):
		print("Tuple: <class 'tuple'>")
	elif isinstance(object, list):
		print("List: <class 'list'>")
	elif isinstance(object, set):
		print("List: <class 'set'>")
	elif isinstance(object, dict):
		print("List: <class 'dict'>")
	elif isinstance(object, str):
		print("List: <class 'str'>")
	else:
		print("Type not found")
	return 42
