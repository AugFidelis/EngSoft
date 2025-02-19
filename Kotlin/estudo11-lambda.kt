fun main(){

    //Uma expressão lambda é uma função anônima (sem nome)
    //que pode ser armazenada em uma variável ou passada como parâmetro.

    val textomaiusculo = { texto: String -> texto.uppercase() }

    val teste = { println("teste") }

    val soma = { a: Int, b: Int -> a+b } //O formato é { parâmetros -> corpo da função }

    println(textomaiusculo("bom dia"))

    teste()

    println(soma(1, 5))

    //------------------------------------

    //Função .filter() em lambda:

    val numeros = listOf(1, -4, 3, 4, -19, 200)

    val positivos = numeros.filter({x: Int -> x > 0})

    println(positivos)

    //Outra maneira de escrever a mesma coisa que os positivos
    val checarNegativo = {x: Int -> x < 0}
    val negativos = numeros.filter(checarNegativo)

    println(negativos)

    //Definindo o tipo de uma função com lambda:

    val textominusculo: (String) -> String = {texto -> texto.lowercase()}

    println(textominusculo("BOM DIA"))

    //----------------------------------------------------

    //Ao fazer uma função retornar uma função lambda:

    //O (Int) -> Int define o tipo da função lambda q ele vai retornar
    fun funcao(x: Int, y:Int): (Int) -> Int{
        return {z -> x + y * z} //Retorna uma função lambda
    }

    val funcLambda = funcao(5, 10) //Define a função lambda retornada como {z -> 5 + 10 * z}

    println(funcLambda(2))
}