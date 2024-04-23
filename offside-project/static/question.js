$(document).ready(function(){


    var next = parseInt(Qnumber) + 1;
    var current = parseInt(Qnumber)

    if (current == 1){
        console.log("hey")  
        $.get('/init_score');
    }

    var optionClicked = false;
    $("#next").prop("disabled", true).css("cursor", "default");

    $(".option").hover(function() {
        if (!optionClicked) {
            $(this).addClass("hovered");
        }
    }, function() {
        if (!optionClicked) {
            $(this).removeClass("hovered");
        }
    });

    $(".option").click(function() {

        if (optionClicked) {
            return;
        }
        optionClicked = true;

        $(".option").css("cursor", "default");

        $(".option").removeClass("selected correct wrong");

        $(this).addClass("selected");

        var isCorrect = $(this).data("correct");
        var explanation = $(this).data("explanation");

        $("#explanation").text(explanation);

        if (explanation.length > 0) {
            $("#explanation").text(explanation).addClass("visible-explanation");
        } else {
            $("#explanation").text("").removeClass("visible-explanation");
        }

        console.log(isCorrect)
        if (isCorrect) {
            $(this).addClass("correct");
            $.get('/increment_score');
        } else {
            $(this).addClass("wrong");
            $(".option[data-correct=1]").addClass("correct");
        }
        $("#next").prop("disabled", false).css("cursor", "pointer");;
    });

    $("#next").click(function(){

        if (!optionClicked) {
            return;
        }
        if (next <= 3){
            window.location.href = "/question/" + next;
        } else {
            window.location.href = "/quizresults";
        }        
    });
});
