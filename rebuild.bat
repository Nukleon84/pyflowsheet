echo "Rebuilding documentation"
pdoc --html --force --output-dir docs pyflowsheet 
move docs\pyflowsheet\*.* docs\
rmdir docs\pyflowsheet\

echo "Rebuilding dist"
python setup.py sdist bdist_wheel