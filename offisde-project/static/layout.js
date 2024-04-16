$(document).ready(function(){
    $('.form-inline').submit(function(event){
        
        event.preventDefault();

        let search_val = $('.search-bar').val().trim();
        if (search_val === ''){
            $('.search-bar').val('');
            $('.search-bar').focus();

            return;
        }

        $(this).unbind('submit').submit();
    });
});