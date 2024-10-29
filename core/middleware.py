from django.http import JsonResponse

class BlockIPMiddleware:
    BLOCKED_IPS = ['192.168.1.1']  # Example blocked IPs

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['REMOTE_ADDR'] in self.BLOCKED_IPS:
            return JsonResponse({'error': 'Access denied.'}, status=403)
        return self.get_response(request)
