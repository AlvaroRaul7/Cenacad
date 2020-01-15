completo <- read.csv2("C:/Users/Luis Toro/Documents/GitHub/Cenacad/completo.csv",header = F)
names(completo) = c("anio","semestre","codigo_materia","materia","paralelo","profesor","pregunta","media","desviacion")
general <- cbind.data.frame(completo$pregunta,completo$media,completo$desviacion)
names(general)=c("Pregunta","Media","Desviacion")
preguntas<- preguntas[duplicated(preguntas),]
? hist
pregunta1 = c(general$Pregunta=preguntas[1])
summary(general)
str(general)
cor(numeric(general$Media),numeric(general$Media))
plot(general$Pregunta,general$Media)aaa
summary(general$Media)
hist(general$Media)
