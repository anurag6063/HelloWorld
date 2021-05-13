// if (jQuery) {
//     alert("loaded");
// }


// // check off a specific todo list by clicking
// $("li").on("click" , function(event){
//     // alert("li clicked");
//     // $(this).css("color", "red").css("text-decoration", "line-through");
//     console.log("clor", $(this).css("color"));
//     // if black (0, 0, 0) change to else chnage to black
//     if( $(this).css("color") === "rgb(0, 0, 0)" ){ // blue in RHS will not work since colors are stred in rgb ##Note the space after , is needed (0,0,0) will not work, needs (0, 0, 0)
//         console.log("clor", $(this).css("color"));
//         $(this).css({
//             color: "blue",
//             //  if the key has - then it does not works in this style replace with camel casing
//             textDecoration: "line-through"

//         });
//     }else {
//         $(this).css({
//             color: "black",
//             // to remove text decoration put as solid or none
//             textDecoration: "solid"
//         })
//     }
// });

// either the above full functionlaity or jsut one toggle class, the class defination is in css file
//  $("li").on("click", function (event) { <- didnt account for fucture li elements that we added with .append()
// with on click, $([name-a-elemet-that-exists-and-all-its childs-event-will-be-listend-to]).on("[type=of-event]", "[which-chile-to-look-out-to-add-event lsitener even in future]", function()){};
$("ul").on("click", "li", function(event) {
    // be aware of the syntax, the IDE does not shows the error till it finally runs.
    $(this).toggleClass("completed");
});



// removing with span
// all the events have a bubble effects, if we put a event in a inner class it calls up all its parent.
// to stop bubble we need event.stopBubble() from jQuery
$("ul").on("click","span",function () {
    // alert("spaniedd..");
    // .parent will get its parent and then act on it.
    $(this).parent().fadeOut(1000, function () {
        // here this means li as in above this was casted to parent.
        $(this).remove();
    });

    event.stopPropagation();
});


// adding todo
// type specified to make it very accurate
$("input[type='text']").keypress(event, function () {
    // console.log("button pressed");
    if (event.which === 13) {
        console.log("enter pressed! adding to-do");

        // extract the data in input and clear the box val() gets the text value.
        var newTodo = $(this).val();
        // this will remove text inside input box .val("");
        $(this).val("");
        console.log(newTodo);
        // the string appending same as in java.
        $("ul").append("<li><span><i class='fa-trash'></i></span> " + newTodo + "</li>");
    }
});

$("fa-plus").click(function(){
    $("input[type='text']").fadeToggle();
});