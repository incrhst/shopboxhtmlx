# Makefile for setting up Tailwind CSS and Flowbite in a Flask project

install:
	npm install -D tailwindcss
	npm install flowbite

init-tailwind:
	npx tailwindcss init

create-input-css:
	mkdir -p static/src
	echo "@tailwind base;\n@tailwind components;\n@tailwind utilities;" > static/src/input.css

compile-tailwind:
	npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css

configure-tailwind: init-tailwind create-input-css compile-tailwind

include-tailwind:
	echo '<link rel="stylesheet" href="{{url_for('static',filename='dist/css/output.css')}}">' >> templates/base.html

configure-flowbite:
	echo 'module.exports = {\n\tplugins: [\n\t\trequire("flowbite/plugin")\n\t]\n}' > tailwind.config.js
	echo 'module.exports = {\n\tcontent: [\n\t\t"./templates/**/*.html",\n\t\t"./static/src/**/*.js",\n\t\t"./node_modules/flowbite/**/*.js"\n\t],\n\ttheme: {\n\t\textend: {},\n\t},\n\tplugins: [\n\t\trequire("flowbite/plugin")\n\t],\n}' > tailwind.config.js

include-flowbite-js:
	echo '<script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.2.0/flowbite.min.js"></script>' >> templates/base.html

setup: install configure-tailwind include-tailwind configure-flowbite include-flowbite-js

start-install:
	python3 -m venv venv;\
		. venv/bin/activate;\
		pip install -r requirements.txt

start:
	. venv/bin/activate;\
		python main.py