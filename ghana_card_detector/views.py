from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import os
import uuid
from django.conf import settings

def index(request):
    """
    Render the main Ghana Card detector interface
    """
    return render(request, 'ghana_card_detector/index.html')


@csrf_exempt
def verify_card(request):
    """
    API endpoint to receive captured Ghana Card images and verify them
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    
    try:
        # Check if we have form data with file or JSON with base64
        if 'card_image' in request.FILES:
            # Handle file upload
            image_file = request.FILES['card_image']
            
            # Save temporarily if needed for processing
            # file_path = save_temp_image(image_file)
            
            # Process the image (implement your verification logic here)
            # This is a placeholder for your actual verification logic
            result = {
                'valid': True,  # Replace with actual verification result
                'message': 'Ghana Card verification successful',
                'card_id': '123456789'  # This would come from your verification system
            }
            
            return JsonResponse(result)
            
        elif request.content_type == 'application/json':
            # Handle JSON with base64 encoded image
            data = json.loads(request.body)
            if 'image_data' not in data:
                return JsonResponse({'error': 'Missing image_data field'}, status=400)
                
            # Extract base64 data
            image_data = data['image_data']
            if 'base64,' in image_data:
                # Remove the data URL prefix if present
                image_data = image_data.split('base64,')[1]
            
            # Convert base64 to binary
            image_binary = base64.b64decode(image_data)
            
            # Save temporarily if needed
            # file_path = save_temp_image_from_binary(image_binary)
            
            # Process the image (implement your verification logic here)
            # This is a placeholder for your actual verification logic
            result = {
                'valid': True,  # Replace with actual verification result
                'message': 'Ghana Card verification successful',
                'card_id': '123456789'  # This would come from your verification system
            }
            
            return JsonResponse(result)
        else:
            return JsonResponse({'error': 'Unsupported content type'}, status=415)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def save_temp_image(image_file):
    """
    Save uploaded image to a temporary location
    """
    # Create temp directory if it doesn't exist
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    # Generate unique filename
    filename = f"ghana_card_{uuid.uuid4()}.jpg"
    file_path = os.path.join(temp_dir, filename)
    
    # Save the file
    with open(file_path, 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)
            
    return file_path


def save_temp_image_from_binary(image_binary):
    """
    Save binary image data to a temporary location
    """
    # Create temp directory if it doesn't exist
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    # Generate unique filename
    filename = f"ghana_card_{uuid.uuid4()}.jpg"
    file_path = os.path.join(temp_dir, filename)
    
    # Save the file
    with open(file_path, 'wb') as f:
        f.write(image_binary)
            
    return file_path