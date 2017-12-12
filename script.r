install.packages("factoextra")
install.packages("cluster")
install.packages("magrittr")

library("cluster")
library("factoextra")
library("magrittr")



data("USArrests")

my_data <- USArrests %>% na.omit() %>% scale()

my_data = read.csv(file = "mini_table10000.csv", sep = ";")

row.names(my_data) <- my_data$id_protein

my_data <- my_data[,-c(1,2,3)]

my_data <- na.omit(my_data)
my_data <- scale(my_data)



#res.dist <- get_dist(my_data, stand = TRUE, method = "pearson")
#fviz_dist(res.dist,  gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
fviz_nbclust(my_data, kmeans, method = "gap_stat")
set.seed(123)
km.res <- kmeans(my_data,10, nstart = 25)
fviz_cluster(km.res, data = my_data,
             ellipse.type = "convex",
             palette = "jco",
             ggtheme = theme_minimal())
