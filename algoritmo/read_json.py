import json
from typing import List
from algoritmo.media import media_um, media_dois
from arquivos_json import document

find_key = ["include_media_id", "include_media_slug"]

print(document)

def get_media_slug():
    media = media_um
    return media


def get_media_id():
    media = media_dois
    return media


def interpolate_json(get_json, find_key: List[str]):
    content = get_json
    if isinstance(content, dict):
        for key, value in content.items():

            if isinstance(content[key], dict) and find_key[0] in content[key]:
                # media_slug = value[find_key[0]]
                get_info_media_slug = get_media_slug()
                content[key] = get_info_media_slug

            elif isinstance(content[key], dict) and find_key[1] in content[key]:
                # media_id = value[find_key[1]]
                get_info_media_id = get_media_id()
                content[key] = get_info_media_id

            else:
                interpolate_json(content[key], find_key)

    elif isinstance(content, list):
        for item in content:
            interpolate_json(item, find_key)
    else:
        return content
    return content


print("Novo conteúdo: ", interpolate_json(json_item, find_key))
