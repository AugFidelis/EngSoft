fun main(){

    val listaimut = listOf("item1", "item2")
    val listamut: MutableList<String> = mutableListOf("coisa1", "coisa2")//Pode ser modificada
    //MutableList<String> define o tipo da lista como string explicitamente

    println(listaimut)
    println(listamut)

    listamut.add("nova coisa")

    println(listamut)

    //No caso da lista mutável ser val e não var, é por que mesmo sendo val a lista pode ser alterada por
    //ser mutável, mas nesse caso ela não poderia ser mudada para OUTRA LISTA, podendo ser alterada mas não
    //substituída, com var ela poderia ser transformada em uma outra lista completamente diferente.

    var listamutavelalteravel = mutableListOf("coisa01", "coisa02")

    println(listamutavelalteravel)

    listamutavelalteravel = mutableListOf("coisa diferente, lista diferente")

    println(listamutavelalteravel)
}