from .constants import allowed_methods

class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, methods):
        def register_route(handler):
            if path in self.routes:
                raise Exception(f"A rota '{path}' já está registrada!")
            self.routes[path] = {}
            for method in methods:
                if method not in allowed_methods:
                    raise Exception(f"Invalid HTTP method '{method}'")
                self.routes[path][method] = handler  # corrigido aqui

            return handler
        return register_route

    def handle_route(self, request, response):
        route = self.routes.get(request.path)
        if route is None:
            response.status_code = 404
            return
        handler = route.get(request.method)
        if request.method not in allowed_methods or handler is None:
            response.status_code = 405
            return

        try:
            handler(request, response)
        except Exception:
            response.status_code = 500  # corrigido aqui
