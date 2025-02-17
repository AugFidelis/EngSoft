fun main(){

    //Mapas tem keys/chaves que apontam para um valor, como "coisa1" aponta para o valor 100
    //Valores podem ser repetidos, como "coisa1" e "coisa3" ambos tem valor 100

    val mapa1 = mapOf("coisa1" to 100, "coisa2" to 200, "coisa3" to 100)
    val mapa2: MutableMap<String, Int> = mutableMapOf("item1" to 1549, "item2" to 54)

    //Para acessar o valor, use a chave como o índice:

    println("O valor da coisa 1 é: ${mapa1["coisa1"]}")

    //Adicionando valores a um mapa:

    mapa2["nova coisa"] = 250

    println(mapa2)
    
    //Removendo valores:

    mapa2.remove("item2")

    println(mapa2)

    //Contando valores:
    println("O mapa 1 tem ${mapa1.count()} valores-chave.")

    //Checando se há uma chave existente no mapa:
    println(mapa1.containsKey("coisa3"))

    //Para dar print em somente chaves ou somente valores se usa:
    println(mapa1.keys)

    println(mapa1.values)

    //Isso também pode ser usado para checar se um valor ou chave específicos existem no mapa:
    println("coisa6" in mapa1.keys) //false

    println(100 in mapa1.values) //true

}