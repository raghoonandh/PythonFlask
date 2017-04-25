$(function() {
    $('button').click(function() {
        // console.log('here');
        // var user = $('#txtUsername').val();
        // var pass = $('#txtPassword').val();
        // $.ajax({
        //     url: '/signUpUser',
        //     data: $('form').serialize(),
        //     type: 'POST',
        //     success: function(response) {
        //         console.log(response);
        //     },
        //     error: function(error) {
        //         console.log(error);
        //     }
        // });

     var url = 'getdata?search=test'
     d3.json(url, function(data){
        console.log(data);
     })

    });
});