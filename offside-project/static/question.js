$(document).ready(function(){

    $("#next").click(function(){
        let next = Qnumber + 1
        if (next == 6){
            window.location.href = "/quizStart"
        }
        else{
            window.location.href = "/question/" + next;
        }
    });

});