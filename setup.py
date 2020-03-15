"""
End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution
"""

from setuptools import setup

setup(
    name='jaidedread',
    packages=['jaidedread'],
    include_package_data=True,
    version='0.9',
    install_requires=['torch', 'torchvision','opencv-python', 'scipy', 'numpy','Pillow'],
    license='Apache License 2.0',
    description='End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution',
    author='Rakpong Kittinaradorn',
    author_email='r.kittinaradorn@gmail.com',
    url='https://github.com/jaided/jaidedread',
    download_url='https://github.com/jaided/jaidedread.git',
    keywords=['ocr optical character recognition deep learning neural network'],
    classifiers=[
        'Development Status :: 4 - Beta'
    ],
)