from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import os
import uuid
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.
@login_required
@csrf_exempt
def tinymce_upload_image(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    file_size_MB = 5
    file = request.FILES['file']
    allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp', 'image/svg+xml']

    if file.content_type not in allowed_types:
        return JsonResponse({
            'error': 'Unsupported file type. Please upload JPEG, PNG, GIF, WEBP, or SVG.'
        }, status=400)

    if file.size > file_size_MB * 1024 * 1024:
        return JsonResponse({
            'error': f'File too large. Maximum size is {file_size_MB}MB.'
        }, status=400)
    
    try:
        extension = file.name.split('.')[-1]
        filename = f"{uuid.uuid4()}.{extension}"

        upload_dir = os.path.join(settings.MEDIA_ROOT, 'blog/post/images')
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, filename)
        default_storage.save(file_path, ContentFile(file.read()))
    
        return JsonResponse({'location': filename})
        
    except Exception as e:
        return JsonResponse({'error': f'Upload failed: {str(e)}'}, status=500)