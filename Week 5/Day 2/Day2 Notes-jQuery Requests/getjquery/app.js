
let url = 'https://jsonplaceholder.typicode.com/photos'
//let photoList = document.getElementById("photoList")

let usersURL = "https://jsonplaceholder.typicode.com/users"

$.get(usersURL,function(users){

  $(users).each(function(index,user){

    $("<div>")
    .append($("<li>").html(user.name))
    .append($("<li>").addClass("someliclass").html(user.email))
    .append($("<li>").html(user.address.street))
    .append($("<li>").html(user.address.geo.lat))
    .appendTo($("#photoList"))

    //$("<li>").html(user.name).appendTo($("#photoList"))
  })

})


//$.get(url,function(data){

  // using plain vanilla JS with ES6 syntax
  /*
  for(let index =0; index<data.length;index++) {
    let li = `<li>${data[index].title}</li>`
    photoList.innerHTML += li
  }*/

  // jQuery
//  $(data).each(function(index ,item){
//    $("<li>").html(item.title).appendTo($("#photoList"))
  //})

// })


// http://dc-coffeerun.herokuapp.com/api/coffeeorders/
// http://dc-coffeerun.herokuapp.com/api/coffeeorders/<email address>
