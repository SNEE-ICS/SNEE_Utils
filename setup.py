from setuptools import setup, find_packages

setup(
    name="python_utils",
    version="0.1.0",
    packages=find_packages(),  # This will find both py_utils and style_utils
    description="Common Python utility functions for reuse across projects.",
    author="Ibrahim Khan",
    license="Apache-2.0",
    license_files=["LICENSE"],
    install_requires=[],  # Add any dependencies here or parse requirements.txt if needed
    include_package_data=True,  # <- This allows MANIFEST.in to include non-code files
    package_data={
        "snee_styles": ["snee.mplstyle","SNEE_plotly.json"],  # Explicitly include the .mplstyle file
    },
)
