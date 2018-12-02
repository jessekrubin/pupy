rm -rf build dist src/pupy.egg-info
python setup.py install
sphinx-build -b html docs dist/docs
