import sys
import os


def manage_secret_key():
    """
    Look for secret_key.py and return the SECRET_KEY entry in it if the file exists.
    Otherwise, generate a new secret key, save it in secret_key.py, and return the key.
    """
    secret_key_dir = os.path.dirname(__file__)
    secret_key_filepath = os.path.join(secret_key_dir, 'secret_key.py')
    sys.path.insert(1, secret_key_dir)

    if os.path.isfile(secret_key_filepath):
        from secret_key import SECRET_KEY  # pylint: disable=import-error
        return SECRET_KEY

    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&amp;*(-_=+)'
    new_key = get_random_string(50, chars)
    with open(secret_key_filepath, 'w') as _file:
        content = '# Django secret key\n# Do NOT check this into version control.\n\n'\
                  'SECRET_KEY = "{0}"\n'.format(new_key)  # noqa
        _file.write(content)
    from secret_key import SECRET_KEY  # pylint: disable=import-error
    return SECRET_KEY
