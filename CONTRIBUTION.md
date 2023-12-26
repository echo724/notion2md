# Notion2md Contribution Guide

Thank you for having an interest in contributing **Notion2md**

Here are some guides for you to how to contribute

## To-do

- [x] Download file object(image and files)
- [x] Table blocks
- [ ] Page Exporter
- [ ] Database Exporter
- [ ] Child page
- [ ] Column List and Column Blocks
- [ ] Synced Block


The list above is the features or blocks needed to be exported in notion2md. You may choose one of these to contribute, or you can also contribute to implementing new feature not in the list.

## How to make PR

Pull requests are welcome.
1. fork this repo into yours
2. make changes and push to your repo
3. send pull request from your **develop** branch to this develop branch

**This is only way to give pull request to this repo. Thank you**

Please make sure that you do the following before submitting your code:
1. Run the tests: `poetry run python -m unittest discover tests`
2. Format the code `poetry run black .`
3. Use isort the code `poetry run isort .`
4. Lint the code `poetry run flake8 .`