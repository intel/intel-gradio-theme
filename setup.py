import os
from setuptools import setup, find_packages

# Dynamically load the version from the __version__ variable in the package
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "intel_gradio_theme", "__init__.py")
    with open(version_file, "r") as fp:
        for line in fp:
            if line.startswith("__version__"):
                # Extract the version string and ignore comments
                return line.split("=")[1].strip().strip('"').strip("'")
    raise RuntimeError("Unable to find version string in intel_gradio_theme/__init__.py")

setup(
    name='intel_gradio_theme',
    version=get_version(),  # Dynamically set the version
    packages=find_packages(),
    package_data={
        "intel_gradio_theme": ["*.css", "*.html"],
    },
    include_package_data=True,
    install_requires=[
        'gradio>=4.0.0',
    ],
    author='Erin Olmon',
    author_email='erin.olmon@intel.com',
    maintainer='Erin Olmon, Agustín Francesa',
    maintainer_email='erin.olmon@intel.com, agustin.francesa.alfaro@intel.com',
    description='A custom theme for Gradio',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/intel/intel-gradio-theme',
    license='Apache 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)