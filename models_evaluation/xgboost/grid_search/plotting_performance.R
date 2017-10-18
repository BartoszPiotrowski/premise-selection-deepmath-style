library(ggplot2)
library(reshape)

scores <- read.csv(file="scores.csv")
dim(scores)
colnames(scores)

a <- aggregate(.~eta, data = scores, mean)
a[order(a$test.error.mean),]

scores$eta <- as.factor(scores$eta)
scores$max_depth <- as.factor(scores$max_depth)

scores$test.accuracy.mean <- 1-scores$test.error.mean

ggplot(scores, aes(eta, test.auc.mean)) + geom_boxplot() + ggtitle("AUC")
ggplot(scores, aes(eta, test.accuracy.mean)) + geom_boxplot() + ggtitle("Accuracy")

ggplot(scores, aes(max_depth, test.auc.mean)) + geom_boxplot() + ggtitle("AUC")
ggplot(scores, aes(max_depth, test.accuracy.mean)) + geom_boxplot() + ggtitle("Accuracy")


# png('plot_accuracy_eta.png')
# ggplot(scores, aes(eta, test.accuracy.mean)) + geom_boxplot() + ggtitle("Accuracy")
# dev.off()
