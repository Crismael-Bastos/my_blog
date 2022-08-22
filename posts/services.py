import numpy as np
from imagekitio import ImageKit
from prettyconf import config

imagekit = ImageKit(
    private_key=config("PRIVATE_KEY", default=""),
    public_key=config("PUBLIC_KEY", default=""),
    url_endpoint=config("URL_ENDPOINT", default=""),
)


def upload_image(file):
    result = imagekit.upload_file(
        file=np.array(file.read()),  # required
        file_name=file.name,  # required
        options={
            "folder": "/blog_django/",
            "tags": ["sample-tag"],
            "is_private_file": False,
            "use_unique_file_name": True,
            "response_fields": ["is_private_file", "tags"],
        },
    )
    return result["response"]["url"]
