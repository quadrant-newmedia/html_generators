'''
    Various utility methods for building html attributes.
'''
def styles(*_styles):
    return '; '.join(filter(None, _styles))

def classes(*_classes):
    return ' '.join(filter(None, _classes))