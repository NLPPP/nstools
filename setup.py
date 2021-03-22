import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
	long_description = fh.read()

platforms = ['linux/Windows']
classifiers = [
	'License :: OSI Approved :: MIT License',
	'Intended Audience :: Developers',
	'Intended Audience :: Education',
	'Intended Audience :: Science/Research',
	'Development Status :: 3 - Alpha',
	'Topic :: Scientific/Engineering',
	'Topic :: Software Development',
	'Topic :: Software Development :: Libraries',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 2',
	"Operating System :: OS Independent",
]

setuptools.setup(
    name="pylangtools", # Replace with your own package name
    version="0.0.2",
    author="Rosefun",
    author_email="rosefun@foxmail.com",
    description="繁体简体转换",
    long_description=long_description,
    #long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    platforms=platforms,
    classifiers=classifiers,
    keywords=['NLP','繁简文字转换']
    
)
