# PackageDistributionIntroduction
Package distribution introduction

Let us start with the folder layout. Your project directory should be structured in the following way and we will explain why later.

```
project_name
├── .github
│   ├── workflows
│       └── main.yml
├── README.assets
├── docs
│   ├── make.bat
│   ├── Makefile
│   ├── README.md
│   ├── conf.py
│   └── index.rst
├── examples
│   └── example.py
├── package_name
│   └── __init__.py
│   └── main.py
├── tests
│   └── __init__.py
├── .gitignore
├── .readthedocs.yml
├── LICENSE.txt
├── MANIFEST.in
├── README.md
├── requirements.txt
└── setup.py
```

Now, this is a lot of files, let us look at these to understand what the different components are and why they are necessary in a Python project.

The setup files
