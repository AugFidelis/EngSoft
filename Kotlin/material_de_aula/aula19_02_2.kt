package material_de_aula

//Criar uma calculadora de resistores
//O usuário vai informar quatro cores e o programa dará a saida de qual o valor do resistor
//Dica: USAR a calculadora de qualquer site bom (digikey.com)
//TRABALHAR com resistores de 4 faixar (4 cores)
//Ex: VERMELHO, PRETO, VERMELHO, DOURADO

fun saudacao(){
    println("CALCULADORA DE RESISTORES")
    println("Informe as cores do resistor, separadas por vírgula:")
}

fun obterCores(): List<String> {
    var coresStr: String = readLine()!!
    coresStr = coresStr.uppercase().replace(" ","")
    return coresStr.split(",")
}

fun calcFaixas(corfaixa: String): String{
    val valorfaixa = when(corfaixa){
        "PRETO" -> ""
        "MARROM" -> "1"
        "VERMELHO" -> "2"
        "LARANJA" -> "3"
        "AMARELO" -> "4"
        "VERDE" -> "5"
        "AZUL" -> "6"
        "VIOLETA" -> "7"
        "CINZA" -> "8"
        "BRANCO" -> "9"
        else -> ""
    }
    return valorfaixa
}

fun calcMult(corfaixa: String): Double{
    val multiplicador: Double = when(corfaixa){
        "PRETO" -> 1.0
        "MARROM" -> 10.0
        "VERMELHO" -> 100.0
        "LARANJA" -> 1000.0
        "AMARELO" -> 10000.0
        "VERDE" -> 100000.0
        "AZUL" -> 1000000.0
        "VIOLETA" -> 10000000.0
        "CINZA" -> 100000000.0
        "BRANCO" -> 1000000000.0
        "DOURADO" -> 0.1
        "PRATA" -> 0.01
        else -> 0.0
    }
    return multiplicador
}

fun calcTolerancia(corfaixa: String): Double{
    val tolerancia = when(corfaixa){
        "MARROM" ->  1.0
        "VERMELHO" ->  2.0
        "VERDE" ->  0.5
        "AZUL" ->  0.25
        "VIOLETA" ->  0.1
        "CINZA" ->  0.05
        "DOURADO" ->  5.0
        "PRATA" ->  10.0
        else -> 0.0
    }
    return tolerancia

}

fun main(){
    saudacao()
    val listaCores = obterCores()
    var totalfaixas = ""

    if(listaCores.size == 4){
        for(i in 0..1){
            totalfaixas += calcFaixas(listaCores[i])
        }
        var resistencia = totalfaixas.toDouble()

        resistencia *= calcMult(listaCores[2])

        println("$resistencia Ohms ${calcTolerancia(listaCores[3])}%")

    } else{
        println("Você deve informar 4 cores. Recomece.")
    }
}
