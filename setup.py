from setuptools import setup, find_packages

setup(
    name='spotify-videoclips',
    version='1.3.4',
    packages=find_packages(),
    description='Simple tool to show Youtube videoclips and lyrics for the playing Spotify songs',
    url='https://github.com/marioortizmanero/spotify-videoclips',
    license='MIT',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Mario O.M.',
    author_email='marioortizmanero@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='spotify videoclip videoclips video videos lyrics',
    python_requires='>=3.5',
    install_requires=[
        'youtube-dl',
        'python-vlc',
        'lyricwikia',
        'dbus-python',
        'spotipy==2.4.4'
    ],
    dependency_links=[
        'git+https://git@github.com/plamere/spotipy.git@master#egg=spotipy-2.4.4' # Fix for https://github.com/plamere/spotipy/issues/211
    ],
    entry_points={
        'console_scripts' : [ 'spotify-videoclips = spotify_videoclips.spotify_videoclips:main' ]
    }
)