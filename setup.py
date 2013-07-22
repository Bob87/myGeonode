import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="my_geonode2",
    version="0.1",
    author="",
    author_email="",
    description="my_geonode2, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="my_geonode2 geonode django",
    url='https://github.com/my_geonode2/my_geonode2',
    packages=['my_geonode2',],
    install_requires=["geonode==2.0b30"],
    include_package_data=True,
    zip_safe=False,
)