import threading

_thread_locals = threading.local()

def save_current_request_middleware(get_response):
    def middleware(request, *args, **kwargs):
        _thread_locals.current_request = request
        response = get_response(request)
        return response
    return middleware

def get_current_request():
    return _thread_locals.current_request