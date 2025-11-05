def all_thing_is_obj(object: any) -> int:
	if isinstance(object, (tuple, list, set, dict, str)):
		print(object, type(object))
	else:
		print("Type not found")
	return 42
