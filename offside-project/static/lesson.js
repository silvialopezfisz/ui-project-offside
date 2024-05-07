$(document).ready(function(){

    $("#next").click(function(){
        let nextLessonNumber = parseInt(lessonNumber) + 1;  // Convert to integer and increment
        if (nextLessonNumber > 7){
            window.location.href = "/quizStart"
        }
        else{
            window.location.href = "/lesson/" + nextLessonNumber;  // next lesson
        }
    });

    $("#prev").click(function(){
        let prevLessonNumber = parseInt(lessonNumber) - 1;  // Convert to integer and decrement
        if (prevLessonNumber < 1) {
            window.location.href = "/";  // Return to the homepage
        } else {
            window.location.href = "/lesson/" + prevLessonNumber;  // previous lesson
        }
    });

});
