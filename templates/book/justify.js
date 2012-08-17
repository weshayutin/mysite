$(document).ready(function() {
    var max = 0;
    $("label").each(function(){
        if ($(this).width() > max)
            max = $(this).width();    
    });
    $("label").width(max);
});



var first_name = document.getElementById("first_name").value;
   var last_name = document.getElementById("last_name").value;
   var email = document.getElementById("email").value;
     
   var data = JSON.stringify({
      "first_name": first_name,
      "last_name": last_name,
      "email": email
   });
   

body, input, textarea {
    font-size:12px;
    line-height:18px;
    font-family:Verdana, Geneva, sans-serif;
}
input {width:300px;}
.submit {width:120px;}
