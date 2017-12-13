
// ul declared in the html page
let movieList = $("#movieList")
let movieDetails = $("#movieDetails")

let moviesURL = "http://www.omdbapi.com/?s=batman&apikey=564727fa"

// get the movies using jquery
$.get(moviesURL,function(data){

  // data.Search is a list/array of movie objects

  $(data.Search).each(function(index,item){

      $("<div>")
      .append($("<li>").append($("<a>").attr("href","#").attr("imdbID",item.imdbID).html(item.Title).click(function(){
        // anchor tag is clicked
        console.log($(this))
        let imdbID = $(this).attr("imdbID") // provide the key to get the value
        populateMovieDetailsByImdbID(imdbID)

        // $(this) what is this? The anchor tag

      })))
      .append($("<img>").addClass("poster").attr("src",item.Poster))
      .appendTo(movieList)

  })

})
function populateMovieDetailsByImdbID(imdbID) {

    let movieDetailsURL = "http://www.omdbapi.com/?i="+imdbID+"&apikey=564727fa"

    $.get(movieDetailsURL,function(data){

        $("<div>")
        .append($("<h1>").html(data.Title))
        .appendTo(movieDetails)

        console.log(data)

    })

    // http://www.omdbapi.com/?i=tt0096895&apikey=564727fa

}
