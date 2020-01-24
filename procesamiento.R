library(float)
completo <- read.csv2("C:/Users/Luis Toro/Documents/GitHub/Cenacad/completo.csv",header = F)
names(completo) = c("anio","semestre","codigo_materia","materia","paralelo","profesor","pregunta","media","desviacion")
general <- cbind.data.frame(completo$pregunta,as.numeric(levels(completo$media))[completo$media],as.numeric(levels(completo$desviacion))[completo$desviacion],stringsAsFactors = FALSE)
nombres <- c("Pregunta","Media","Desviacion")
names(general)= nombres
summary(general)
str(general)
cor(general$Media,general$Desviacion)
plot(general$Pregunta,general$Media,main = "grafico de preguntas vs calificacion",ylab = "calificacion",xlab="preguntas")
plot(general$Pregunta,general$Desviacion,main = "grafico de preguntas vs diferencia de calificacion",ylab = "diferencia de calificacion",xlab="preguntas")
hist(general$Media)
hist(general$Desviacion)
#hist(general$Desviacion)
preguntas <- as.factor(general$Pregunta)
summary(preguntas)
pregunta1<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[1]],general$Media[general$Pregunta==preguntas[1]],general$Desviacion[general$Pregunta==preguntas[1]])
pregunta2<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[2]],general$Media[general$Pregunta==preguntas[2]],general$Desviacion[general$Pregunta==preguntas[2]])
pregunta3<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[3]],general$Media[general$Pregunta==preguntas[3]],general$Desviacion[general$Pregunta==preguntas[3]])
pregunta4<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[4]],general$Media[general$Pregunta==preguntas[4]],general$Desviacion[general$Pregunta==preguntas[4]])
pregunta5<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[5]],general$Media[general$Pregunta==preguntas[5]],general$Desviacion[general$Pregunta==preguntas[5]])
pregunta6<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[6]],general$Media[general$Pregunta==preguntas[6]],general$Desviacion[general$Pregunta==preguntas[6]])
pregunta7<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[7]],general$Media[general$Pregunta==preguntas[7]],general$Desviacion[general$Pregunta==preguntas[7]])
pregunta8<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[8]],general$Media[general$Pregunta==preguntas[8]],general$Desviacion[general$Pregunta==preguntas[8]])
pregunta9<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[9]],general$Media[general$Pregunta==preguntas[9]],general$Desviacion[general$Pregunta==preguntas[9]])
pregunta10<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[10]],general$Media[general$Pregunta==preguntas[10]],general$Desviacion[general$Pregunta==preguntas[10]])
pregunta11<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[11]],general$Media[general$Pregunta==preguntas[11]],general$Desviacion[general$Pregunta==preguntas[11]])
pregunta12<-cbind.data.frame(general$Pregunta[general$Pregunta==preguntas[12]],general$Media[general$Pregunta==preguntas[12]],general$Desviacion[general$Pregunta==preguntas[12]])
names(pregunta1)=nombres
names(pregunta2)=nombres
names(pregunta3)=nombres
names(pregunta4)=nombres
names(pregunta5)=nombres
names(pregunta6)=nombres
names(pregunta7)=nombres
names(pregunta8)=nombres
names(pregunta9)=nombres
names(pregunta10)=nombres
names(pregunta11)=nombres
names(pregunta12)=nombres
summary(pregunta1)
media1 = mean(pregunta1$Media)
media2 = mean(pregunta2$Media)
media3 = mean(pregunta3$Media)
media4 = mean(pregunta4$Media)
media5 = mean(pregunta5$Media)
media6 = mean(pregunta6$Media)
media7 = mean(pregunta7$Media)
media8 = mean(pregunta8$Media)
media9 = mean(pregunta9$Media)
media10 = mean(pregunta10$Media)
media11 = mean(pregunta11$Media)
media12 = mean(pregunta12$Media)
#Agrupacion de las preguntas que consideremos para cada factor que elegimos
#Calidad de la enseñanza del profesor y como lo percibe el estudiante
factor1 <- cbind.data.frame(pregunta1$Media,pregunta2$Media,pregunta4$Media,pregunta5$Media)
factor1v <- cbind(pregunta1$Desviacion,pregunta2$Desviacion,pregunta4$Desviacion,pregunta5$Desviacion)
#destreza pedagógica del profesor
factor2 <- cbind.data.frame(pregunta2$Media,pregunta4$Media)
factor2v <- cbind(pregunta2$Desviacion,pregunta4$Desviacion) 
#entorno
factor3 <- cbind.data.frame(pregunta3$Media,pregunta6$Media,pregunta7$Media,pregunta8$Media)
factor3v <- cbind(pregunta3$Desviacion,pregunta6$Desviacion,pregunta7$Desviacion,pregunta8$Desviacion)
cor(factor1)
cor(factor2)
cor(factor3)
cor(factor1v)
cor(factor2v)
cor(factor3v)
#Primer Factor
cor.test(pregunta1$Media,pregunta2$Media)
cor.test(pregunta1$Media,pregunta4$Media)
cor.test(pregunta1$Media,pregunta5$Media)
cor.test(pregunta2$Media,pregunta4$Media)
cor.test(pregunta2$Media,pregunta5$Media)
cor.test(pregunta4$Media,pregunta5$Media)
#Tercer Factor
cor.test(pregunta3$Media,pregunta6$Media)
cor.test(pregunta3$Media,pregunta7$Media)
cor.test(pregunta3$Media,pregunta8$Media)
cor.test(pregunta6$Media,pregunta7$Media)
cor.test(pregunta6$Media,pregunta8$Media)
cor.test(pregunta7$Media,pregunta8$Media)
plot(factor1,main = "Factor 1")
plot(factor2,main = "Factor 2")
plot(factor3,main = "Factor 3")
