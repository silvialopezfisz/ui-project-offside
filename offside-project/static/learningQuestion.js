$(document).ready(function() {
    // Initially disable the "Resume Learning" button until an option is selected
    $("#resumeLearning").prop("disabled", true).css("cursor", "default");
    $("#explanationMedia").css("display", "none");

    // Handle option click events
    $(".form-check-input").click(function() {
        // Prevent multiple selections by disabling all options once one is selected
        $(".form-check-input").prop("disabled", true);
        $(".form-check-input").css("cursor", "default");

        // Remove any previous selections or styles
        $(".form-check-input").removeClass("selected correct wrong");

        // Mark the clicked option as selected
        $(this).addClass("selected");

        // Retrieve the correctness and explanation from data attributes
        var isCorrect = $(this).data('correct');
        var explanation = $(this).data('explanation');
        var explanationMedia = $(this).data('explanationMedia');

        console.log("Is Correct:", isCorrect); // Check if the correct status is being retrieved
        console.log("Explanation:", explanation); // Check what explanation is being retrieved

        $("#explanation").text(explanation); // Display the explanation

        if (explanation.length > 0) {
            $("#explanation").addClass("visible-explanation").show(); // Make sure to show the explanation if it is not empty
        } else {
            $("#explanation").removeClass("visible-explanation").hide(); // Hide the explanation if it is empty
        }

        $("#explanationMedia").css("display", "flex");
        // Apply styles based on whether the answer was correct or not
        if (isCorrect) {
            $(this).parent().addClass("correct");
        } else {
            $(this).parent().addClass("wrong");
            // Automatically mark the correct option for educational purposes
            $(".form-check-input[data-correct='1']").parent().addClass("correct");
        }

        // Enable the "Resume Learning" button to allow going back to the lesson
        $("#resumeLearning").prop("disabled", false).css("cursor", "pointer");
    });

    // Resume learning button navigates back to the associated lesson
    $("#resumeLearning").click(function() {
        window.location.href = "/lesson/" + lessonNumber;
    });
});
