

let pendingTaskList = $("#pendingTaskList")

// button click add task button
$("#btnAddTask").click(function(){

  let title = $("#taskTextBox").val()

  // $('<input />', { type: 'checkbox', id: 'cb'+id, value: name })

  $("<div>").addClass("todoListItem").append($("<input/>",{type:'checkbox'}).click(function(){
        // $(this) is the scope of the current object on which the event
        // is called
        if($(this).is(":checked")) {

        }

  })).append($("<li>").html(title)).append($("<button>").html("Remove"))
  .appendTo(pendingTaskList)

})

// this represents the outer most container which is window object
console.log(this)
