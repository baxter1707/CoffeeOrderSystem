let mathOp = ""

let addButton = document.getElementById("addButton")

addButton.addEventListener("click", function() {
  mathOp = "+"

  //console.log(mathOp)
})

let subButton = document.getElementById("subButton")

subButton.addEventListener("click", function(){
  mathOp = "-"
})

let multiplyButton = document.getElementById("multiplyButton")

multiplyButton.addEventListener("click", function(){
  mathOp = "*"
})

let divideButton = document.getElementById("divideButton")

divideButton.addEventListener("click", function(){
  mathOp = "/"
})

let calculate = document.getElementById("calculate")

calculate.addEventListener("click", function(){
  let firstNumber = document.getElementById("firstNumber");
  let secondNumber= document.getElementById("secondNumber");

  if(mathOp == "+"){
    result = parseInt(firstNumber.value) + parseInt(secondNumber.value)
    window.alert(result)
  }

  if(mathOp == "-"){
    result = parseInt(firstNumber.value) - parseInt(secondNumber.value)
    window.alert(result)
  }

  if(mathOp == "*"){
    result = parseInt(firstNumber.value) * parseInt(secondNumber.value)
    window.alert(result)
  }

  if(mathOp == "/"){
    result = parseInt(firstNumber.value) / parseInt(secondNumber.value)
    window.alert(result)
  }
})
