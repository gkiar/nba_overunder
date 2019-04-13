from setuptools import setup
import os.path as op

VERSION = "0.0.1"
DEPS = [
         "requests",
         "pandas"
       ]

setup(name="nbaou",
      version=VERSION,
      description="NBA Over-Under (pronounced N-B-Oww) - tool for running an " +
                  "Over-Under league on NBA team win-loss projections.",
      url="http://github.com/gkiar/nbaou",
      author="Greg Kiar",
      author_email="gkiar07@gmail.com",
      python_requires=">=3.5",
      classifiers=[
                "Programming Language :: Python",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.5",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: Implementation :: PyPy",
                "License :: OSI Approved :: MIT License",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "Operating System :: OS Independent",
                "Natural Language :: English"
                  ],
      license="MIT",
      packages=["nbaou"],
      include_package_data=True,
      test_suite="pytest",
      tests_require=["pytest", "pytest-runner", "pycodestyle"],
      setup_requires=DEPS,
      install_requires=DEPS,
      entry_points = {
        "console_scripts": [
            "nbaou=nbaou.main:main",
        ]
      },
      zip_safe=False)

