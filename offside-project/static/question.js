$(document).ready(function(){
    let score = 0;

    $("input[type='radio'][name='options']").change(function(){
        let selectedOption = $(this).val();
        let correctAnswer = $(this).data('answer');

        $("input[type='radio'][name='options']").attr('disabled', true);
        $("#explanation").show();

        if (selectedOption === correctAnswer) {
            score++;
            // Optional: Update some score display if needed
            // $("#score").text("Score: " + score);
        }
    });

    $("#next").click(function(){
        let next = parseInt(Qnumber) + 1;  
        if (next > 3){
            window.location.href = "/quizresults?score=" + score;
        } else {
            window.location.href = "/question/" + next;
        }        
    });

    $("#prev").click(function(){
        let prev = parseInt(Qnumber) - 1;  // Ensure Qnumber is treated as an integer
        if (prev >= 1){
            window.location.href = "/question/" + prev + "?type=" + itemType;
        }
    });
});
