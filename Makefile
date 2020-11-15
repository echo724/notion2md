release: upload clean build
	twine upload dist/*

upload:
	echo "Enter Commit Message:"
	read commit1
	git pull
	git add .
	git commit -m "$commit1"
	git push

clean:
	rm -rf build dist

build:
	python setup.py bdist_wheel