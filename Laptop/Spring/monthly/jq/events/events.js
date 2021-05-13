// if(jQuery){
//     alert("loaded jq");
// }

// invoked when the box of h1 is clicked anywhere.
$("h1").click(function () { alert("clicked") });

//  jq applies click function to all the child methods if the parent has this function. in JS we will have to 
// iterate and add event to all of them.
// $("button").click(function(){alert("clicked button")});

// to select an element use $(this), changed Background color 
$("button").click(function () { $(this).css("background", "yellow") });

$("input").keypress(function (event) {
    console.log("pressed");
    // runs when enter (char code JS 13) is pressed
    // note event.which is JS style capture if value no $ 
    if (event.which === 13) {
        alert("enter");
    }
});

/*
// incorrect fade and remove method
$("button").on("click", function (event) {
    console.log("button clicked");
    //  fade away is done using fadeOut([time]); dafult is 400ms
    $("div").fadeOut(3000);
    // this remove will remove all before it fades out in the timeout. since the above and this line are 2 events and are executed in asny manner.
    $("div").remove();
});

*/

// correct fade and remove method
$("button").on("click", function (event) {
    console.log("button clicked");
    //  fade away is done using fadeOut([time]); dafult is 400ms
    $("div").fadeOut(3000, function (event) {
        // nesting it inside the fucntion block makes its execution only when the outer block has completed.
        // $(this).remove();
        // or
        // $("div").remove();
        // but i guess former one is better 
    });

});


// correct fade in
$(".wanna-shine").on("click", function (event) {
    console.log("button clicked");
    //  fade away is done using fadeOut([time]); dafult is 400ms
    $(".fadeInDiv").fadeIn(3000, function (event) {       
        // but i guess former one is better 
    });

});


