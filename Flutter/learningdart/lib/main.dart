import 'package:flutter/material.dart';

//-- Functions --
// const age = 27;
// const twiceAge = age * 2;

// String getFullName(String firstName, String lastName){
//   //return firstName + ' ' + lastName;
//   return '$firstName $lastName';
// }

// String getFullName(String firstName, String lastName) => '$firstName $lastName'; 
//Não precisa de retorno em funções simples assim

// void printMyName(String name){
//   print(name);
// }

void main() {
  // var name = 'Alex';
  // name = 'Anthony';
  runApp(const MyApp());
}

void testCap4(){
  //-- If, Else, Else If --
  // final name = 'Foo';

  // if(name == 'Foo'){
  //   print('Yes this is Foo');
  // }
  // else if(name != 'Bar'){
  //   print('This value is not Bar');
  // }
  // else{
  //   print("I don't know what this is \" "); 

  //   //Pra evitar o problema de ' dentro da string use " ", 
  //   //ou \ antes do ' ou " pra dizer que não é o fim do string
  // }

  // if(name == 'Foo')  print('Yessss'); //Pode escrever assim pra one liners

  //------------------------------------------------------------------------------------------------

  //-- Operators --
  // var age = 20;
  // final halfOfAge = age / 2;
  // print(halfOfAge);

  // final doubleOfAge = age * 2;
  // print(doubleOfAge);

  // final ageMinusOne = --age; //Diminui o age também
  // print('$age, $ageMinusOne');

  // final name = 'Foo ';
  // final nameTimes20 = name * 20; //Você pode multiplicar texto pra usar ao invés de lorem ipsum
  // print(nameTimes20);

  //------------------------------------------------------------------------------------------------
  
  //-- Lists --
  // var names = ['Foo', 'Bar', 'Baz']; //Listas usam []
  // final foo = names[0];
  // print(foo);
  // print(names.length);

  // names.add('My name');
  // print(names.length);

  //------------------------------------------------------------------------------------------------

  //-- Sets --
  // var names = {'Foo', 'Bar', 'Baz'}; //Sets usam {}, não podem ter itens repitidos
  // names.add('Foo');
  // names.add('Bar');
  // names.add('Baz');
  // print(names);

  //------------------------------------------------------------------------------------------------

  //-- Maps --
  // var person = {
  //   'age': 20, //Nome da chave entre '' e o valor depois do :
  //   'name': 'Foo'
  // };
  // print(person);

  // person['name'] = 'FOOOOOOOOOOO'; //Assim que se altera um valor de uma chave
  // print(person);

  // person['lastname'] = 'Baz'; //Assim você adiciona uma nova chave e valor
  // print(person);
}

void testCap5(String? firstName, String? middleName, String? lastName){
  
  // //-- Nullable --
  // String? name = null;
  // print(name);

  // name = 'Foo';
  // print(name);

  // //LISTA OBRIGATÓRIA DE ITENS OPCIONAIS
  // List<String?> names = [null, 'Foo']; 
  // //Dentro das chaves significa que pode ter null dentro da lista ou ser uma lista de nulls

  // //LISTA OPCIONAL DE ITENS OBRIGATÓRIOS
  // List<String>? namesnull; //Igual a List<String>? namesnull = null;
  // //Fora da chave significa que a lista NÃO pode ter nulls dentro dela mas pode ser nula 
  // //caso a lista não tenha sido inicializada

  // //LISTA OPCIONAL DE ITENS OPCIONAIS
  // List<String?>? names2 = [null, 'Foo', null, 'Bar']; //Aqui pode os dois
  // names2 = null;

  // //------------------------------------------------------------------------------------------------

  // //-- Cherry picking nullables (??) --
  // const String? firstName = null;
  // const String? middleName = null;
  // const String? lastName = 'Baz';

  // // if(firstName != null){
  // //   print('First name is the first non-null value');
  // // }
  // // else if(middleName != null){
  // //   print('Middle name is the first non-null value');
  // // }
  // // else if(lastName != null){
  // //   print('Last name is the first non-null value');
  // // }

  // //Ao invés de fazer esse if todo:

  // //?? significa: se o valor à minha esquerda é nulo, selecione o que está à minha direita
  // const firstNonNullValue = firstName ?? middleName ?? lastName;

  //------------------------------------------------------------------------------------------------

  // //-- Null-aware assignment operator (??=) --
  // String? name = firstName;

  // name ??= middleName; 
  // //Basicamente pergunta: o valor atual é null? Se for, vou colocar o novo valor

  // name ??= lastName; 
  // //Mesmo depois disso, ele continua como middleName pois o middleName não é null

  // print(name);

  //------------------------------------------------------------------------------------------------
}

void testCap5_2(List<String>? names){
    
  // // -- Conditional invocation (?.) --
  // // int length = 0;
  // // if(names != null){
  // //   length = names.length;
  // // }

  // //Pra não ter que fazer esse if:

  // final length = names?.length ?? 0; 
  // //O '?? 0' é pra garantir que length não possa ser nulo e seja um int normal

  // names?.add('Baz'); 
  // //Aqui precisa do ?. por exemplo caso a lista não exita e seja null

}

//------------------------------------------------------------------------------------------------

// //-- Enumerations --
// enum PersonProperties {
//   firstName, lastName, age
// }

// void testCap6(){
//   print(PersonProperties.firstName);
//   print(PersonProperties.firstName.name);
// }

//------------------------------------------------------------------------------------------------

// //-- Switch Statement --
// enum AnimalType {
//   cat, dog, bunny
// }

// void testCap6_2(AnimalType animalType){
//   switch(animalType){
//     case AnimalType.bunny:
//       print('Bunny');
//       break;
//     case(AnimalType.cat):
//       print('Cat');
//       break;
//     case(AnimalType.dog):
//       print('Dog');
//       break;
//   }
//   //Usar return; no lugar de break; pularia esse print pois sairia da função
//   print('Function is finished!');
// }

//------------------------------------------------------------------------------------------------

//-- Classes --
// class Person{
//   // void run(){
//   //   print('Running');
//   // }

//   // void breathe(){
//   //   print('Breathing');
//   // }

//   //------------------------------------------------------------------------------------------------

//   // //-- Constructors --
//   final String name;

//   Person(this.name); //Construtor

//   //------------------------------------------------------------------------------------------------

//   // void printName(){
//   //   print('Name of the person:');
//   //   print(name); //Não usar this. aqui
//   // }

// }

// void testCap6_3(){
//   // final person = Person();
//   // person.run();
//   // person.breathe();

//   //------------------------------------------------------------------------------------------------

//   final foo = Person('Foo Bar');
//   //print(foo.name);

//   //------------------------------------------------------------------------------------------------

//   foo.printName();

// }

//------------------------------------------------------------------------------------------------

// //-- Inheritance / Subclassing --
// abstract class LivingThing{
//   void breathe(){
//     print('Living thing is breathing');
//   }
//   void move(){
//     print('I am moving');
//   }
// }

// class Cat extends LivingThing{

// }

//------------------------------------------------------------------------------------------------

// //-- Factory Constructors --
// class Cat extends Object{
//   final String name;

//   Cat(this.name); //Construtor normal

//   // factory Cat.fluffBall(){ 
//   //   //Factory constructor, pra casos onde várias instâncias tem o mesmo nome por exemplo
//   //   return Cat('Fluff ball');
//   // }

//   //------------------------------------------------------------------------------------------------

//   // //-- Custom Operators --
//   // @override 
//   // bool operator ==(covariant Cat other) => other.name == name;
//   // //Dentro das parenteses é o com o que está sendo comparado
//   // //'covariant' diz ao dart que pode esqueçer a superclasse original já que temos certeza que será Cat

//   // @override
//   // int get hashCode => name.hashCode;

// }

// void testCap6_4(){
//   // final fluffers = Cat();
//   // fluffers.move();
//   // fluffers.breathe();

//   //------------------------------------------------------------------------------------------------

//   // final fluffBall = Cat.fluffBall();
//   // print(fluffBall.name);

//   //------------------------------------------------------------------------------------------------

//   // final cat1 = Cat('Foo');
//   // final cat2 = Cat('Foo');
//   // if(cat1 == cat2){
//   //   print('They are equal');
//   // }
//   // else{
//   //   print('They are not equal');
//   // }
// }

//------------------------------------------------------------------------------------------------

////-- Extensions --

// class Cat{
//   final String name;
//   Cat(this.name);

// }

// class Person{
//   final String firstName;
//   final String lastName;

//   Person(this.firstName, this.lastName);
// }

// extension Run on Cat{
//   void run(){
//     print('Cat $name is running');
//   }
// }

// extension FullName on Person{
//   String get fullName => '$firstName $lastName';
// }

// void testCap7(){
//   final meow = Cat('Fluffers');
//   print(meow.name);
//   meow.run();

//   final foo = Person('Foo', 'Bar');
//   print(foo.fullName);

// }

//------------------------------------------------------------------------------------------------

////-- Future --

// Future<int> heavyFutureThatMultipliesByTwo(int a){
//   return Future.delayed(const Duration(seconds: 3), () => a * 2); // => é basicamente  {return a * 2}
// }

// void testCap7_2() async { //async permite o uso de funções assíncronas (ex: await)
//   final result = await heavyFutureThatMultipliesByTwo(10); 
//   //Sem await ele printa 'Instance of 'Future<int>' '
//   //await é usado para esperar pelo resultado de um Future
  
//   print(result);
// }

//------------------------------------------------------------------------------------------------

////-- Streams --

// Stream<String> getName(){
//   return Stream.periodic(const Duration(seconds: 1), (value){
//     return 'Foo';
//   }); //A cada 1 segundo retorna a string 'Foo'
// }

// void testCap7_3() async {
//   await for (final value in getName()){
//     print(value);
//   }
//   print('Stream finished working');
// }

//------------------------------------------------------------------------------------------------

////-- Generators --

// Iterable<int> getOneTwoThree() sync*  { //sync* ou async* (tem que adicionar a tag de stream se for async*)
//   yield 1;
//   yield 2;
//   yield 3;
// }

// void testCap7_4() async {
//   for(final value in getOneTwoThree()){
//     print(value);

//     if(value ==2){
//       break;
//     }
//   }
// }

//------------------------------------------------------------------------------------------------

// //-- Generics --

// class PairOfStrings{
//   final String value1;
//   final String value2;
//   PairOfStrings(this.value1, this.value2);
// }

// class PairOfIntegers{
//   final int value1;
//   final String value2;
//   PairOfIntegers(this.value1, this.value2);
// }

// //Ao invés das duas classes iguais:
// class Pair<A, B> {
//   final A value1;
//   final B value2;
//   Pair(this.value1, this.value2);
// }

// void testCap7_5() {
//   final names = Pair('Foo', 20);
// }

//------------------------------------------------------------------------------------------------



class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    //print(getFullName('Foo', 'Bar'));
    
    // testCap5(null, 'Bar', 'Baz');
    // testCap5_2(null);
    // testCap6();
    // testCap6_2(AnimalType.cat);
    // testCap6_3();
    // testCap6_4();
    // testCap7();
    // testCap7_2();
    // testCap7_3();
    // testCap7_4();
    // testCap7_5();
    
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: .fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // TRY THIS: Try changing the color here to a specific color (to
        // Colors.amber, perhaps?) and trigger a hot reload to see the AppBar
        // change color while the other colors stay the same.
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          //
          // TRY THIS: Invoke "debug painting" (choose the "Toggle Debug Paint"
          // action in the IDE, or press "p" in the console), to see the
          // wireframe for each widget.
          mainAxisAlignment: .center,
          children: [
            const Text('You have pushed the button this many times:'),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            // Text('$age, dobro: $twiceAge')
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
