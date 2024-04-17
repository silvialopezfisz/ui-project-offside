$(document).ready(function(){
    $("#startlearning").click(function(){
        console.log("Start learning clicked!");
        window.location.href = "/lesson/1";
    });

    $("#startquiz").click(function(){
        console.log("Start quiz clicked!");
        window.location.href = "/quizStart";
    });
});
