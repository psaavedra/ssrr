from setuptools import setup, find_packages

version = "0.0.2"

long_description = ""
try:
    long_description=file('README.md').read()
except Exception:
    pass

license = ""
try:
    license=file('MIT_License.txt').read()
except Exception:
    pass


setup(
    name = 'ssrr',
    version = version,
    description = 'Simple Stream Reflector for RTMP servers',
    author = 'Pablo Saavedra',
    author_email = 'pablo.saavedra@treitos.com',
    url = 'http://github.com/psaavedra/ssrr',
    packages = find_packages(),
    zip_safe=False,

    install_requires=[
        "simplejson",
    ],
    scripts=[
        "tools/ssrr",
    ],

    download_url= 'https://github.com/psaavedra/ssrr/zipball/master',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Video",
    ],
    long_description=long_description,
    license=license,
    keywords = "python ffmpeg rtmp erlyvideo",
)
