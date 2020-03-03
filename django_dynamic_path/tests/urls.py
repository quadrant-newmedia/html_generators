from django.http import HttpResponse
from django.urls import path, include

from django_dynamic_path import DynamicPath

def confirm_args(request, *args, **kwargs):
    if len(args) == 2 and args[0] == 'a' and kwargs['b'] == 2 :
        return HttpResponse()
    raise RuntimeError('did not get expected args/kwargs')

def interact(path):
    import code; code.interact(local=locals())

urlpatterns = [
    path('path_before/', lambda r: HttpResponse('path before'), name='path_before_name'),

    DynamicPath(
        lambda path: path == 'bar/' and ((), {}),
        lambda r: HttpResponse('bar from dynamic'),
    ),

    DynamicPath(
        lambda path: path == 'baz/' and (('a', 'b'), {'a': 1, 'b': 2}),
        confirm_args,
    ),

    path('included/', include([DynamicPath(
        lambda path: path == 'baz/' and (('a', 'b'), {'a': 1, 'b': 2}),
        confirm_args,
    )])),

    path('path_after/', lambda r: HttpResponse('path after'), name='path_after_name'),
    path('path_after/<value>/', lambda r: HttpResponse('path after'), name='path_after_name'),
]