require(tidyverse)
require(sqldf)
df = read.csv('out/data.csv')

data = df[,-1] #ignore pandas index
data = sqldf("select * from data 
    where not (x<300 and y>75) and not y=0")
    #removed outlier
g = ggplot(data=data, aes(x=x, y=y, ymin=ymin, ymax=ymax, fill=mutant))

g + 
    geom_line(aes(color=mutant)) +
    geom_ribbon(alpha=0.2) +
    geom_hline(yintercept=50)