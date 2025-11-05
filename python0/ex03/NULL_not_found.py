def NULL_not_found(object: any) -> int:
	if not object:
		print(object, type(object))
		return 0
	elif isinstance(object, float) and object != object:
		print("Cheese", object, type(object))
		return 0
	else:
		print("Type not found")
	return 1
