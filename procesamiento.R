completo <- read.csv2("C:/Users/Luis Toro/Documents/GitHub/Cenacad/completo.csv",header = F)
names(completo) = c("anio","semestre","codigo_materia","materia","paralelo","profesor","pregunta","media","desviacion")
general <- cbind(completo["pregunta"],completo["media"],completo["desviacion"])
preguntas<- (completo["pregunta"]) 
preguntas<- preguntas[duplicated(preguntas),]

