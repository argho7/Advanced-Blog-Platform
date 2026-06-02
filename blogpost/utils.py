from uuid import uuid4
from django.utils.text import slugify
def Generate_Slug(model, name):
    slug=slugify(name)

    while model.objects.filter(slug=slug).exists():
        slug=slug + str(uuid4())[:4]
    return slug