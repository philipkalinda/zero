from distutils.core import setup
setup(
  name = 'zero',
  packages = ['zero'],
  version = '0.01',
  license='MIT',
  description = 'Project Zero',
  author = 'Philip Kalinda',
  author_email = 'philipkalinda@gmail.com',
  url = 'https://philipkalinda.com',
  download_url = 'https://github.com/philipkalinda/zero/archive/v_001.tar.gz',
  keywords = ['zero'],
  install_requires=[
          'numpy',
          'sklearn',
          'scipy',
		      'geneticfs',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
