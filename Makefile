
default:
	#python main.py
	cp results.csv ./analysis/
	R -e "rmarkdown::render('analysis/analysis.Rmd')"
	firefox ./analysis/analysis.html
