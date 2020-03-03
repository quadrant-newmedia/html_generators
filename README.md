# django_dynamic_path

A django path() replacement enabling truly dynamic urls.

Rather than mapping a regular expression to a view function, you map a "resolver function" to a view function. The resolver function receives the path as an argument, and decides whether or not it wants to handle the request. If it does want to the handle the request, it should return a tuple of args and kwargs, which will be passed to the view function.

## Use Cases

TODO