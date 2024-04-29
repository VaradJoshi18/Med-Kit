import logging
logger = logging.getLogger(__name__)

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")
        logger.error("Before opening URL")


    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        logger.error("after opening url")
        print("This is after View")
        return response