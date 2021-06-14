from django import http


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if (request.method == "OPTIONS"):
            response = http.HttpResponse()
            response["Content-Length"] = "0"
            response["Access-Control-Max-Age"] = 86400
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE, GET, OPTIONS, PATCH, POST, PUT, HEAD"
        response["Access-Control-Allow-Headers"] = "accept, accept-encoding, authorization, content-type, referer, sec-ch-ua, sec-ch-ua-mobile, dnt, origin, user-agent, x-csrftoken, x-requested-with"
        return response
