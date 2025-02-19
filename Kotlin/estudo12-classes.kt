//Em classes, as propriedades podem estar dentro dos parênteses ou dentro das chaves:
class Contato(val id: Int, var email: String) {
    var telefone: Int = 0
}

fun main(){

    val contato1 = Contato(1, "exemplo@email.com")
    contato1.telefone = 981815656

    println(contato1.id)
    println(contato1.email)
    println(contato1.telefone)
}