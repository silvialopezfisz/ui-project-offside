$(document).ready(function(){

    $("#next").click(function(){
        let next = lesson_num + 1

        window.location.href = "/lesson" + next;

    });

    $("#prev").click(function(){
        let prev = lesson_num - 1

        if (prev == 0){
            window.location.href = "/" ;
        }
        else{
            window.location.href = "/lesson" + prev;
        }

    });
    

});