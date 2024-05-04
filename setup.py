from setuptools import setup

try:
    long_description = open("README.md").read()
except:
    long_description = ""

version = '0.5.6a'

if version.endswith('a'):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

setup(
    name='soundcloud-lib',
    version=version,
    description='Python Soundcloud API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/3jackdaws/soundcloud-lib',
    author='Ian Murphy',
    author_email='3jackdaws@gmail.com',
    license='MIT',
    packages=['sclib'],
    python_requires='>=3.6',
    install_requires=['mutagen', 'aiohttp'],
    test_suite='pytest',
    tests_require=['pytest', 'pytest-asyncio'],
)