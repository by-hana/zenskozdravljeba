from django.conf import settings


def upload_image(file, folder='cms'):
    """Upload an image file to Cloudinary and return metadata."""
    import cloudinary
    import cloudinary.uploader

    cloudinary.config(
        cloud_name=settings.CLOUDINARY_CLOUD_NAME,
        api_key=settings.CLOUDINARY_API_KEY,
        api_secret=settings.CLOUDINARY_API_SECRET,
    )

    result = cloudinary.uploader.upload(
        file,
        folder=folder,
        resource_type='image',
    )

    return {
        'url': result.get('secure_url', ''),
        'public_id': result.get('public_id', ''),
        'width': result.get('width'),
        'height': result.get('height'),
    }
