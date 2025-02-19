fun main(){

    //When é melhor para quando há mais do que duas condições, como o switch em C por exemplo

    val num = 2

    val dia = when(num){ //Pode ser usado na declaração de um valor

        1 -> "Domingo"
        2 -> "Segunda"
        3 -> "Terça"
        4 -> "Quarta"
        5 -> "Quinta"
        6 -> "Sexta"
        7 -> "Sábado"
        else -> "Dia Inválido"
    }

    println(dia)

}