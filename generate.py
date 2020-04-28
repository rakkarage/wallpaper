#!/usr/bin/env python3

import json
import os

from github import Github

g = Github()
repo = g.get_repo("rakkarage/wallpaper")
contents = repo.get_contents("images")

images = []

for content_file in contents:
    image = {}
    image["url"] = content_file.download_url
    images.append(image)

print(json.dumps(images, indent=2))
