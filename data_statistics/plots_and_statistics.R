library(RcppCNPy)
library(ggplot2)

sums_of_rows = npyLoad("sums_of_rows.npy")
sums_of_cols = npyLoad("sums_of_cols.npy")
uno = npyLoad("uno.npy")[1]

sums_of_rows <- sums_of_rows/uno
sums_of_cols <- sums_of_cols/uno

length(sums_of_rows)
length(sums_of_cols)

ggplot() + aes(sums_of_rows) + geom_histogram(bins = 70) + scale_x_log10(breaks = c(1, 10, 30, 100, 300, 1000))
ggplot() + aes(sums_of_cols) + geom_histogram(bins = 50) + scale_x_log10()

max(sums_of_rows)
min(sums_of_rows)
max(sums_of_cols)
min(sums_of_cols)
