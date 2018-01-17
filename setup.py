from setuptools import setup

setup(name="calculus",
	version='0.1',
	description='a symbolic calculus toolkit',
	url='http://github.com/georgercarder/calculus',
	author='George Carder',
	author_email='georgercarder@gmail.com',
	license='MIT',
	scripts=[],	
	install_requires=[], ## other packages	
	dependency_links=[], ## links for dep not on pypi	
	test_suite='',		## nose.collector	
	tests_require=[],	## 'nose'
	packages=['calculus'],
	zip_safe=False)

