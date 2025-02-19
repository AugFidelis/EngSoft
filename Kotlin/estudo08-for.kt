fun main(){

    for (num in 1..5){ //1..5 é o range do for
        print(num)
    }
    println()

    val lista = listOf("banana", "maçã", "abacaxi")

    for(ingrediente in lista){
        println("Na vitamina de hoje, usei $ingrediente.")
    }
}