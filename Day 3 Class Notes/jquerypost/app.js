
let postURL = "https://jsonplaceholder.typicode.com/posts"
let flowerPostURL = "https://flowers.vapor.cloud/flower"


$("#btnPOST").click(function(){

  let title = $("#titleTextBox").val()
  let description = $("#descriptionTextBox").val()
  let userId = $("#userIdTextBox").val()

  /* { "title": "foo",
    "body": "bar",
    "userId": 1
  }
  */

  let data = {body: description, userId: userId}

  $.post(flowerPostURL,data,function(response){
    console.log(response)
  })

})
