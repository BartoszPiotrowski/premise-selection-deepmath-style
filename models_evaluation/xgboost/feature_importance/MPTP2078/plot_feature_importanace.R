library(ggplot2)

importance_w <- read.csv(file="importance_weight.csv", sep=";")
importance_g <- read.csv(file="importance_gain.csv", sep=";")

dim(importance_w)
dim(importance_g)

importance_w$f_number <- as.factor(importance_w$f_number)
importance_w$feature <- as.factor(importance_w$feature)
importance_w$thm_prm <- as.factor(importance_w$thm_prm)

importance_g$f_number <- as.factor(importance_g$f_number)
importance_g$feature <- as.factor(importance_g$feature)
importance_g$thm_prm <- as.factor(importance_g$thm_prm)

png('plot_importance_gain.png')
ggplot(importance_g, aes(importance)) + geom_histogram(bins=70) + scale_x_log10()
dev.off()

png('plot_importance_weight.png')
ggplot(importance_w, aes(importance)) + geom_histogram(bins=70) + scale_x_log10()
dev.off()

