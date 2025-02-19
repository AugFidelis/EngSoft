fun main(){

    var num = 0

    while(num <= 10){ //Repete o seu conteúdo até a condição ser falsa
        println("($num/10)")
        num++
    }

    //-------------------------------------------

    //do/while sempre executa o bloco antes, então mesmo que a condição seja falsa desde o começo,
    //o bloco vai executar ao menos uma vez

    var num2 = 10

    do{
       println("($num2/9)")
        num2++
    } while(num2 < 9) //false

}