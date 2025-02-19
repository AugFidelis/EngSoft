//Precisa especificar os tipos das variaveis E da função quando ela retorna algo
fun soma(x: Int, y: Int): Int{
    return x + y
}

//Outro jeito de se escrever uma função de uma linha só como a soma():
//fun soma(x: Int, y: Int) = x + y



fun itens(item1: String, item2: String = "Coisa 2 padrão"){ //Pode se especificar valores padrões aqui
    println("O primeiro item é $item1")
    println("O segundo item é $item2")
}



fun main(){

    val num1 = 3
    val num2 = 10

    println(soma(num1, num2)) //Chama a função dentro do print

    //Pode se especificar os parâmetros, e com isso pode se atribuir eles fora de ordem:

    itens(item2 = "Coisa 1", item1 = "Coisa 2")

    itens(item1 = "Coisa 1") //No caso de itens(), o item 2 tem um valor padrão então ele pode ficar vazio
}

