var x=10;
console.log(x);
var name;
console.log(name);

function exampleVar() {
    for (var i=0;i<3; i++){
        console.log(i);
    }
    console.log(i);
}


function exampleLet() {
    for (let i=0;i<3; i++){
        console.log(i);
    }
    console.log(i);
}


function exampleLet2() {
    let let=1;
    for (let i=let;i<3; i++){
        console.log(i);
    }
    console.log(i);
}


function ejemploLet(){
    let j=5;
    if (true){
        j =10;
        console.log(j);
    }
    console.log(j);
}


const person = {
    name : "john",
    age : 30
};


function alcance(tipo){
    var varGlobal=5;
    if (tipo == "global") {
        console.log(varGlobal);
    } else if(tipo=="local"){
        let varLocal=10;
        console.log(varLocal);
    }
    
    console.log(varGlobal);
    console.log(varLocal);
}

function name(params) {
    for (let index = 0; index < array.length; index++) {
        const element = array[index];
        
    }
}


let persona= {
    nombre: "juan",
    edad: 23,
    sexo: "Hombre",
    altura : 1.86,
    suscrito : false,
    telefono : "3121212122",
    correo :"juan@gmail.com"
}



contraseña: MiAmor --> hash
            R O M a I m 

            r o m A A i M M


{"array": [1,2,3], "boolean": true, "color": "gold", "null": null, "number": 123, "object": {"a": "b","c": "d"}, "string": "Hello World" }