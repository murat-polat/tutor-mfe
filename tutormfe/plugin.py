from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}muratp/mfe",
        "HOST": "apps.{{ LMS_HOST }}",
        "COMMON_VERSION": "{{ OPENEDX_COMMON_VERSION }}",
        "AUTHN_MFE_APP": {
            "name": "authn",
            "repository": "https://github.com/opendx/frontend-app-authn",
            "port": 1999,
            "env": {
                "production": {
                    "COACHING_ENABLED": "",
                    "ENABLE_DEMOGRAPHICS_COLLECTION": "",
                }
            }
        }
    }
}

hooks = {
    "build-image": {
        "mfe": "{{ MFE_DOCKER_IMAGE }}",
    },
    "remote-image": {
        "mfe": "{{ MFE_DOCKER_IMAGE }}",
    },
    "init": ["lms"],
}


def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
