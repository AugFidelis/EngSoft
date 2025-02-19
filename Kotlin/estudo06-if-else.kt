fun main(){

    val check = false
    val x: Int
    val y = 2

    if (check){ //Se 'check' for true:
        x = 1
    }
    else{
        x = 3
    }

    println(x)

    //-----------------------------

    //O if pode ser colocado dentro do println na mesma linha:
    println(if (y > x) "Y é maior" else "X é maior")

}