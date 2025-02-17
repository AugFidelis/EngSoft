fun main(){

    //Sets são desorganizados e seus valores são únicos,
    //por exemplo no print o "item1" só aparece a primeira vez pois ele não pode ser duplicado

    val set1: Set<String> = setOf("item1", "item2", "item3", "item1")
    val set2: MutableSet<String> = mutableSetOf("coisa1", "coisa2", "coisa1")

    println(set1)
    println(set2)

    //Comandos de lista (os que não acessam index pois eles não são organizados) também funcionam:

    println("O set 1 tem ${set1.count()} itens!")//Ele não conta itens repetidos pq é um set

    println("coisa2" in set2) //true

    set2.add("coisa nova")

}