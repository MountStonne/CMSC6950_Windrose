# Makefile to get and process datafiles, generate a plot and build LaTeX report.

report.pdf: report.tex  images/figure1.png images/figure2.png images/figure3.png images/figure4.png images/figure5.png
	pdflatex report.tex

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

# winddata.csv:
#	wget -O winddata.csv https://www.smartatlantic.ca/erddap/tabledap/SMA_st_johns_wharf.csv?time%2Cwind_spd_avg%2Cwind_dir_avg&time%3E=2019-08-01T00%3A00%3A00Z&time%3C=2020-07-31T23%3

.PHONY:  clean  almost_clean

clean: almost_clean
	rm report.pdf
	rm report.run.xml

almost_clean:
	latexmk -c
	rm windData.csv
