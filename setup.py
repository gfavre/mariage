from setuptools import setup, find_packages
print("****************** Installing ****************")
#-e git+https://github.com/fivethreeo/cmsplugin-blog-search#egg=cmsplugin_blog_search
# git+git://github.com/maccesch/cmsplugin-contact.git@ad69dda2d30c0104e0e96a0b3cafd2be4c6a015c
# git+git://github.com/gfavre/cmsplugin-blog.git@3911225e6674220ac909d27e2b2e9f054dfcac42
# git+git://github.com/fivethreeo/cmsplugin-blog-search

#requirements = open('requirements.pip').read().split('\n')
setup(name='mariage',
      author = 'Gregory Favre',
      version='1.0 (alpha)',
      packages=find_packages(),
      package_data={'mariage': ['templates/*.html', 'templates/*/*.html', 'templates/*/*/*.html']},
      include_package_data=True,
      #install_requires=requirements,
)


