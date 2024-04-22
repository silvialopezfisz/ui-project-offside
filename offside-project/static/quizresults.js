$(document).ready(function(){
    $.get('/get_score', function(score) {
        $("#score").text("You scored " + score + " out of 3.");
    });
});