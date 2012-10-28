import os
from setuptools import setup, find_packages
print("****************** Installing ****************")
#-e git+https://github.com/fivethreeo/cmsplugin-blog-search#egg=cmsplugin_blog_search
# git+git://github.com/maccesch/cmsplugin-contact.git@ad69dda2d30c0104e0e96a0b3cafd2be4c6a015c
# git+git://github.com/gfavre/cmsplugin-blog.git@3911225e6674220ac909d27e2b2e9f054dfcac42
# git+git://github.com/fivethreeo/cmsplugin-blog-search

#requirements = open('requirements.pip').read().split('\n')
def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
django_dir = 'mariage'

for dirpath, dirnames, filenames in os.walk(django_dir):
    # Ignore PEP 3147 cache dirs and those whose names start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or dirname == '__pycache__':
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(name='mariage',
      author = 'Gregory Favre',
      version='1.0 (alpha)',
      packages = packages,
      data_files = data_files,
      
      
      #install_requires=requirements,
)


