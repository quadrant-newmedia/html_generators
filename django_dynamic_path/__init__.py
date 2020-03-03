from django.urls.resolvers import ResolverMatch, RegexPattern, URLPattern

class DynamicPath(URLPattern):
    def __init__(self, resolver_func, view_func):
        self.resolver_func = resolver_func
        self.view_func = view_func

        super().__init__(
            # Note - this regex matches nothing
            # We implement our own resolve() method, and we ignore this.
            # It still needs to be a valid regex, though, or urls.reverse() will break.
            RegexPattern(r'^(?!x)x'),
            view_func,
        )

    def resolve(self, path):
        r = self.resolver_func(path)
        if r :
            args, kwargs = r
            return ResolverMatch(
                self.view_func,
                args,
                kwargs,
                route='_DYNAMIC_PATH_ROUTE_',
            )