El siguiente texto corresponde a la explicación del fenomeno que se observa en el ejemplo adjunto llamado loss of significance.

para el ejemplo anterior se utilizaron 3 famosos numeros irracionales
  1) Pi
  2) euler
  3) numero de oro (proporción aurea) (1+sqrt(5))/2
  
   A cada uno se le calculó el cuadrado utilizando una calculadora cientifica para posteriormente calcular el mismo cuadrado esta vez utilizando el algoritmo float64 y float32 respectivamente y con ayuda del software python. Finalmente se opuede obserevar que existe una diferencia entre el resultado obtenido por la calculadora cientifica y los obtenidos mediante puntos flotantes. A dicha diferencia se le llamó "error".
   Esta diferencia radica en que cuando se emplean puntos flotantes, se utiliza un algoritmo diferente a la hora de describir un número ya que recordemos que un computador no es capaz de entender un caracter si es que no se ha definido este en terminos de un lenguaje que el computador comprenda como los 1s y 0s por ejemplo. Cuando se utilizan números flotantes, el computador ordena y define los numeros como potencias de base 2 en vez de hacerlo con potencias en base 10. Esto produce que ciertas aproximaciones que se hacen en el calculo de números con infinitos decimales difieran en ambos algoritmos, generando un error entre ambos. Dichas aproximaciones son por ejemplo las que hace una calculadora cuando debe sumar 3 veces "1/3" y obtener "1" debido a que 1/3 es 0,333333333[...] lo que multiploicado por 3 no daexactamente 1 en estricto rigor.
