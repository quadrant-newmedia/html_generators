'''
	Various utility methods for building html attributes.
'''
def styles(*styles):
	'''Join multiple "conditional styles" and return a single style attribute'''
	return '; '.join(filter(None, styles))

def classes(*classes):
	'''Join multiple "conditional classes" and return a single class attribute'''
	return ' '.join(filter(None, classes))