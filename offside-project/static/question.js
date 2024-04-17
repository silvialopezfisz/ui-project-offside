$(document).ready(function(){
    let score = 0;  // Initialize score

    // Handle option selection and submit answer
    $("input[type='radio'][name='options']").change(function(){
        let selectedOption = $(this).val();
        let correctAnswer = $(this).data('answer');

        // Disable further selections after one is made
        $("input[type='radio'][name='options']").attr('disabled', true);

        // Display the explanation
        $("#explanation").show();

        // Update score if correct
        if (selectedOption === correctAnswer) {
            score++;
            // Optional: Update some score display if needed
            // $("#score").text("Score: " + score);
        }
    });

    // Handling the 'Next' button click
    $("#next").click(function(){
        let next = parseInt(Qnumber) + 1;  // Ensure Qnumber is treated as an integer
        if (next > 3){  // Change this to match your total number of questions
            // Send final score to server via POST request and redirect
            window.location.href = "/quizresults?score=" + score;
        } else {
            window.location.href = "/question/" + next;
        }        
    });

    // Handling the 'Previous' button click
    $("#prev").click(function(){
        let prev = parseInt(Qnumber) - 1;  // Ensure Qnumber is treated as an integer
        if (prev >= 1){
            window.location.href = "/question/" + prev + "?type=" + itemType;
        }
    });
});
