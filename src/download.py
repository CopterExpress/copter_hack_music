import os
import cgi
import requests
import shutil


def download_url(url, directory, get_params=None):
    """Download file from url to directory

    URL is expected to have a Content-Disposition header telling us what
    filename to use.

    Returns filename of downloaded file.

    """
    response = requests.get(url, params=get_params, stream=True)
    response.raise_for_status()

    params = cgi.parse_header(
        response.headers.get('Content-Disposition', ''))[-1]
    if 'filename' not in params:
        raise ValueError('Could not find a filename')

    filename = os.path.basename(params['filename'])
    abs_path = os.path.join(directory, filename)
    with open(abs_path, 'wb') as target:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, target)

    return filename
