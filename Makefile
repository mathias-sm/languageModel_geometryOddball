
default:
	#python main.py
	cp result.json ./analysis/
	R -e "rmarkdown::render('analysis/analysis.Rmd')"
	firefox ./analysis/analysis.html
