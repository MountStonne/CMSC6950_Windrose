# Makefile to get and process datafiles, generate a plot and build LaTeX report.

winddata.csv:
	wget -O winddata.csv https://www.smartatlantic.ca/erddap/tabledap/SMA_st_johns_wharf.csv?time%2Cwind_spd_avg%2Cwind_dir_avg&time%3E=2019-08-01T00%3A00%3A00Z&time%3C=2020-07-31T23%3

