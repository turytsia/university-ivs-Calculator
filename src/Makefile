run:
	start "./dist/Calculator.exe"

profile:
	python ./src/profiling/set_data.py 1000 | python -m src.profiling.profiler

pack:
	tar --format=zip -cvf ./xturyt00_xkolia00_xpodho08_xbuten00.zip src profiling plan debugging.png skutecnost.txt License screenshot.png hodnoceni.txt README.md .gitignore

test:
	python ./src/math/test_math.py

doc:
	doxygen ./Doxyfile

compile:
	pyinstaller --onefile -w --add-data "src;src" ./src/main.py -n Calculator