# Makefile to get and process datafiles, generate a plot and build LaTeX report.
FIGURES = images/figure1.png images/figure2.png images/figure3.png images/figure4.png images/figure5.png
report.pdf: report.tex  $(FIGURES)
	latexmk -pdf -pdflatex='pdflatex -shell-escape'
images/figure1.png: plot.py winddata.csv
	python plot.py
images/figure2.png: plot.py winddata.csv
	python plot.py
images/figure3.png: plot.py winddata.csv
	python plot.py
images/figure4.png: plot.py winddata.csv
	python plot.py
images/figure5.png: plot.py winddata.csv
	python plot.py

winddata.csv: process_data.py
	python process_data.py

.PHONY:  clean  almost_clean

clean: almost_clean
	rm report.pdf
	rm report.run.xml
	rm report.bbl

almost_clean:
	latexmk -c
	rm windData.csv
