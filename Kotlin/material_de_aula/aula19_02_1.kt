package material_de_aula

//Como saber o resultado do cálculo, usando o depurador?
fun calcCompCircunf(pi: Double, r: Double): Double{
    return 2 * pi * r
}

fun main(){

    val r = 100.0
    val pi = 3.1415

    println(calcCompCircunf(pi, r))
}

//    for (i in 0..10){
//        println("i = $i")
//    }
//

//    val n = 100
//    var n1: Double = 0.0
//    n1 = 10.5
//
//    println("Os numeros sao $n e $n1")