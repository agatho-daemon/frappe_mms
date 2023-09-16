from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_mms/__init__.py
from frappe_mms import __version__ as version

setup(
	name="frappe_mms",
	version=version,
	description="A Frapperized Maintenance Management System",
	author="Wasaq Group Co",
	author_email="info@wsqgroup.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
