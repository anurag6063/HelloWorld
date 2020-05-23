var simpleButtonas = document.querySelector("button");
console.log("found button: ",simpleButtonas);
va
/*
simpleButtonas.addEventListener("click", function(){
    alert("i have been selected");
});


simpleButtonas.addEventListener("click", function(){
alert("clicked")
});

*/

simpleButtonas.addEventListener("click", function(){
    document.body.style.background= "purple";
    this.style.background="red";
    document.body.style.background= "purple";

});


