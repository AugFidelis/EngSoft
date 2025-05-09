package material_de_aula

/*
class Contact(val name: String, val phone: String, email: String)

fun main(){
    val c1 = Contact("Mateus","123123123","mateus@mateus.pro.br")
    val c2 = Contact("Augusto","234234234","augusto@email.com")

    //Qual a diferença entre classe e instância?
    //Resposta básica: A instância é a coisa real e a classe é a especificação
}
 */

/*
class Contact {
    var name: String? = null
    var email: String? = null
    var phone: String? = null
}

fun main(){
    val c1 = Contact()
    c1.name = "John"
    println(c1.name)
    c1.email = "john@gmail.com"
    println(c1.email)
    println(c1.phone)

    //Toda classe tem a especificação de um construtor vazio
}
 */

/*
class Resistor{
    var colors: MutableList<String> = mutableListOf()
    var resistanceValue: Double = 0.0

    fun calculateResistance(){
        if(colors.isEmpty()){
            resistanceValue = -1.0
        } else if(colors[0].uppercase().equals("RED")){
            resistanceValue = 100.0
        } else{
            resistanceValue = 1000.0
        }
    }
}

fun main(){
    val r1 = Resistor()
    r1.resistanceValue = 1000.0
    println("Resistance value: ${r1.resistanceValue}")

    val r2 = Resistor()
    r2.colors.add("Azul")
    r2.colors.add("Black")
    r2.colors.add("White")
    r2.colors.add("Black")
    r2.calculateResistance()
    println(r2.colors)
}
 */

/*
//Não fazer isso porque não se deve misturar as especificades em uma única classe, dará problemas...
class Animal(val name: String){
    fun latir(){
        println("Au Au...")
    }
    fun miar(){
        println("Miau...")
    }
    fun mugir(){
        println("Muuu...")
    }
}
 */


//!! Pesquisar: Devemos implementar nossas classes por comportamentos e não por supertipos
//Exemplo do pato, exemplo da loja de guitarras

/*
open class Animal(){
    var name: String? = null
    var weight: Double? = null
}

class Dog(): Animal(){
    fun bark(){
        println("Au Au")
    }
    fun nadar(){

    }

}

class Cat(): Animal(){
    fun miar(){
        println("Miau")
    }
    fun nadar(){

    }

}


fun main(){
    val c1 = Dog()
    c1.name = "Bella"
    c1.weight = 6000.0
    c1.bark()
}
 */



//Essa classe não tem funções, apenas carrega dados
data class Endereco(var logradouro: String, var numero: Int, var complemento: String,
                    var bairro: String, var cidade: String, var uf: String)

data class Pessoa(var nome: String, var altura: Double, var peso: Double, var endereco: Endereco)

data class Empresa(var nome: String, var enderecoMatriz: Endereco)

//Usamos programação orientada a objetos por que devemos nos preocupar com reaproveitamento
//de código por meio de classes que se tornam futuramente componentes

