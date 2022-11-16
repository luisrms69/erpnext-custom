from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_custom/__init__.py
from erpnext_custom import __version__ as version

setup(
	name="erpnext_custom",
	version=version,
	description="Campos custom de erpnext marcados para exportacion a traves de fixture",
	author="buzola",
	author_email="admin@appcity.mx",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
