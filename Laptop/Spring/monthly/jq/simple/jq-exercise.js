// Q in jQuery is always capital
// checking if jquey has been loaded properly
if(jQuery){
    alert("jquery active")
} else {
    alert("not found")
}

// chnage bakground of div
$("div").css("background", "purple");
// chnage div names highlight class
$("div.highlight").css("width", "200px");
// id called third
$("#third").css("border", "2px solid orange");
// first-of class selcts the first of Selector; JS function
$("div:first-of-type").css("color", "pink");

// to fetch a text
$("h1").text();

// to set a text value; intrestingliy if applied on a list all the elements of list of chnaged by jq but not by js.
$("h1").text("you have changed!");

// to fetch html and set it 
$("li").html();
$("li").html("<strong>Stronger<strong>");

// fetched the wodth of image
$('img').css("width");
// reduces it
$('img').css("width", "400px");
// to fetch a internal attribute like src below and change it.
$('img').attr('src', 'https://bestoldmovie.com/wp-content/uploads/2020/01/The-Exact-Moment-Captain-America-Become-Worthy-Explained-2.jpg')

// to fetch type of a particular element
$('input').attr('type');
//  changed it 
// $('input').attr('type', 'color')

// to affect only first image
$('img:first-of-type').css("width", "100px");


// to affect only last
$('img').last().css("width", "100px");

// to fetch value which are dynamic in nature,  like dropdown, text, image radio button etc.
$("input").val();

// to find what was seletced inisde the select tag of HTML
$("select").val();

