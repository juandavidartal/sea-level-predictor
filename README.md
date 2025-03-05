# Sea Level Predictor

This project uses Python with Pandas, Matplotlib, and SciPy to analyze and visualize sea level data, predicting future sea levels based on historical trends.

## Project Description

The `sea_level_predictor.py` script reads sea level data from `epa-sea-level.csv`, generates a scatter plot of the data, and creates two lines of best fit:

1.  **Best Fit Line 1:** A linear regression line calculated using the entire dataset (1880-2050).
2.  **Best Fit Line 2:** A linear regression line calculated using data from the year 2000 onwards (2000-2050).

The script then saves the generated plot as `sea_level_plot.png`.

## Files

* `sea_level_predictor.py`: The Python script that generates the sea level plot.
* `epa-sea-level.csv`: The dataset containing sea level data.
* `sea_level_plot.png`: The generated plot (output).

## Dependencies

* Python 3.x
* Pandas (`pip install pandas`)
* Matplotlib (`pip install matplotlib`)
* SciPy (`pip install scipy`)
