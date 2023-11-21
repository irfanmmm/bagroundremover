from rembg import remove
from PIL import Image
from main.models import Removebaground
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import RemovebagroundSerializer
from datetime import datetime
import os
from django.conf import settings


@api_view(["POST"])
def uploadimge(request):
    image = request.data["image"]

    print(image)
    if image:
        input_path = image
        unique_filename = f"removed_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        output_path = os.path.join(settings.MEDIA_ROOT, unique_filename)
        input_ = Image.open(input_path)
        processed_image = remove(input_)
        processed_image.save(output_path)

        print(processed_image)

        instance = Removebaground.objects.create(
            uplodedimage=image, remove_bg=output_path
        )
        response_data = {"status_code": 6000, "message": "Success"}

    else:
        response_data = {"status_code": 6001, "message": "Image Importent"}

    return Response(response_data)


@api_view(["GET"])
def renderdata(request):
    try:
        instance = Removebaground.objects.latest("uplodedimage", "remove_bg")

        context = {"request": request}
        serialzer = RemovebagroundSerializer(instance, context=context)
        response_data = {"status_code": 6000, "data": serialzer.data}
    except:
        response_data = {"status_code": 6001, "message": "Image Dosnot Exist"}

    return Response(response_data)
