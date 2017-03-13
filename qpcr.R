
#library
library(ggplot2)


#read data
dat = read.table("~/Box Sync/2017/3March/NPB/qpcr/ermb.qpcr.tsv", sep='\t', header= F)

#pre-proces
sub_dat = subset(dat, V11 != "NaN")
sub_dat$date = paste(sub_dat$V10, sub_dat$V8, sub_dat$V9, sep="_")
sub_dat$V6 = gsub("NBA", "AD", sub_dat$V6)
sub_dat$V7 = gsub("1", "", sub_dat$V7)
sub_dat$V7 = gsub("2", "", sub_dat$V7)
sub_dat$V7 = gsub("3", "", sub_dat$V7)


#plot
ggplot(sub_dat, aes(x=date, y= V12))+geom_boxplot()+geom_point(position = position_jitter(width = 0.2))+facet_grid(V7~V6)+scale_y_log10()