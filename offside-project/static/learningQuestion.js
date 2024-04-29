$(document).ready(function() {
    // Initially disable the "Resume Learning" button until an option is selected
    $("#resumeLearning").prop("disabled", true).css("cursor", "default").hide();
    $("#explanationMedia").css("display", "none");

    var optionClicked = false;


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

        $("#explanation").text(explanation); 

        if (explanation.length > 0) {
            $("#explanation").addClass("visible-explanation").show(); 
        } else {
            $("#explanation").removeClass("visible-explanation").hide();
        }

        $("#explanationMedia").css("display", "flex");

        
        if (isCorrect) {
            $(this).addClass("correct");
            $.get('/increment_score');
        } else {
            $(this).addClass("wrong");
        }
        $("#resumeLearning").prop("disabled", false).css("cursor", "pointer").show();
    });

    // Resume learning button navigates back to the associated lesson
    $("#resumeLearning").click(function() {
        window.location.href = "/lesson/" + lessonNumber;
    });
});
