# Makefile to get and process datafiles, generate a plot and build LaTeX report.

report.pdf: report.tex  winddata.csv
    latexmk -pdf

#winddata.csv:
#	wget -O winddata.csv https://www.smartatlantic.ca/erddap/tabledap/SMA_st_johns_wharf.csv?time%2Cwind_spd_avg%2Cwind_dir_avg&time%3E=2019-08-01T00%3A00%3A00Z&time%3C=2020-07-31T23%3

.PHONY:  clean  almost_clean

clean:
	rm report.log
	rm report.aux
	rm report.bcf
	rm report.out
	rm report.toc
	rm report.run.xml

almost_clean:
	rm winddata.csv
	rm report.pdf
