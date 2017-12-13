
// jquery function
// fires when the DOM is READY
$(document).ready(function(){

    console.log("DOM is loaded")
    console.log("Access the Div1 element inside document.ready")
    // jquery get element by id
    let div1 = $("#div1")
    console.log(div1)

})

// plain vanilla JS
let div1UsingVanillaJS = document.getElementById("div1")
console.log(div1UsingVanillaJS)

console.log("Access the Div1 element")
// jquery get element by id
let div1 = $("#div1")
// for get the actual HTML element
// div1[0]
console.log(div1)

// get elements with class name using jquery
let div2 = $(".my-div")

console.log(div2)

// get element by tag name using jquery
let p = $("p")
console.log(p)

// create element using jquery
let div5 = $("<div>")
// add class to div5
div5.addClass("my-div")
div5.html("This DIV is created using jQuery")
// add id to div5
div5.attr("id","div5")

// add event listener using jQuery
$("#btnGreet").click(function(){
  console.log("greetings")

  // hide the greeting div
  //$("#greetingDiv").hide(1000)

  // slide
  //$("#greetingDiv").slideUp(500)

  $("#greetingDiv").slideToggle(500)

})

// get the body element using jquery
let body = $("body")

body.append(div5)

// looping using jquery Library
$("#taskList").children().each(function(index,value){
  // value is <li></li> elements
//  $(value).css({"background-color":"yellow","font-size":10})

  $(value).addClass("some-other-list-item")

  // removing a class
//  $(value).removeClass("some-other-list-item")


  console.log($(value))
})

// chaining jquery functions

let innerDiv = $("#div1").append("<div>")
console.log("inner div")
console.log(innerDiv[0]) // parent element


//$("#div1").addClass("div1-class").append("<br>").css({"background-color":"purple"})
/*
let div_1 =  $("#div")
div_1.addClass("div1-class")
div_1.append("<br/>")
div_1.css({"background-color":"purple"})
*/

// make list sortable using jquery ui
$( "#taskList" ).sortable();
