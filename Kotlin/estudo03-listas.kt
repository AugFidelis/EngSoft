fun main(){

    val lista: MutableList<String> = mutableListOf("item 1", "item 2", "item 3")

    println("O primeiro item da lista é o ${lista[0]}") //Assim que se lê valores de lista em strings

    //----------------------------------------------------------------

    //.first() , .last() e .count() são funcões de extensão:

    println(lista.first())

    //ou

    println("O primeiro item é ${lista.first()}")

    println("Existem ${lista.count()} itens na lista")

    //----------------------------------------------------------------

    //Checar se há um valor na lista:
    println("item 2" in lista) //true

    //----------------------------------------------------------------

    //Adicionar e remover itens de uma lista:
    lista.add("item adicionado")

    lista.remove("item 3")

    lista.removeAt(0) //Descobri sozinho, não está na documentação nessa parte

    println(lista)

}