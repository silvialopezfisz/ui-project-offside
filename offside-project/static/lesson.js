$(document).ready(function(){

    $("#next").click(function(){
        let next = lessonNumber + 1
        if (next == 8){
            window.location.href = "/quizStart"
        }
        else{
            window.location.href = "/lesson/" + next;
        }

    });

    $("#prev").click(function(){
        let prev = lessonNumber - 1

        if (prev == 0){
            window.location.href = "/" ;
        }
        else{
            window.location.href = "/lesson/" + prev;
        }
    });

});