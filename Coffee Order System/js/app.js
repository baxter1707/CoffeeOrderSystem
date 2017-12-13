let getAllCoffeeURL ="http://dc-coffeerun.herokuapp.com/api/coffeeorders/"
let coffeePostURL = "http://dc-coffeerun.herokuapp.com/api/coffeeorders/"

let orderList= $("#order-list")

$("#view-orders-button").click(function(){
  $.get(getAllCoffeeURL,function(info){
    for(let key in info){

      $("<div>").addClass("order-container")
      .append($("<li>").html(info[key].emailAddress))
      .append($("<li>").html(info[key].coffee))
      .appendTo($(orderList))

    }
    })


  })

$("#search-orders-button").click(function(){
  let inputEmail = $("#email-entry").val()
  $.get(getAllCoffeeURL,function(info){
    for(let key in info){
      console.log(info[key].emailAddress)
      if (inputEmail.toLowerCase() == info[key].emailAddress.toLowerCase()){
        console.log("These are the same")
        $("<div>")
        .append($("<li>").html(info[key].emailAddress))
        .append($("<li>").html(info[key].coffee))
        .append($("<button>").attr("id","delete-order").html("Delete Item"))
        .appendTo($("#search-result"))
///Delete Section
        $("#delete-order").click(function(){
          let deleteOrder = {"emailAddress": info[key].emailAddress,
        "coffee": info[key].coffee}
        console.log(deleteOrder)


        })

      }


}
})
})



$("#submit-button").click(function(){
  let createOrderEmail = $("#create-order-email").val()
  let createCustomerOrder = $("#create-customer-order").val()



  let newOrder = {"emailAddress": createOrderEmail,
"coffee": createCustomerOrder}

  $.post(getAllCoffeeURL,newOrder,function(response){
    console.log(response)
  })
})
