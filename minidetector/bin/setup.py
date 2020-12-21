import setuptools


setuptools.setup(
    name="minidetector",
    version="0.0.1",
    author="Amit Itzkovitch",
    author_email="amit7itz@gmail.com",
    description="A small example package",  
    packages=setuptools.find_packages(),
    install_requires=['scapy', 'sqlalchemy', 'psycopg2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
