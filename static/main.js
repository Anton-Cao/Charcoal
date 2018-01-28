$(document).ready(function() {
  function success(rec) {
    $('#recs').empty();
    for (let i = 0; i < 5; i++) {
      $('#recs').append('<li>' + rec[i] + '</li>');
    }
  }

  $('#input').keyup(function(e) {
    const data = {
      story: $('#input').val()
    };
    
    $.ajax({
      type: "GET",
      url: '/rec',
      data: data,
      contentType: "application/json; charset=utf-8", // this
      dataType: "json", // and this
      success:  function(rec) {
        $('#recs').empty();
        for (let i = 0; i < 5; i++) {
          $('#recs').append('<li>' + rec[i] + '</li>');
        }
      }
    });
  });

  $('#story-form').submit(function(event) {
    event.preventDefault();
    $.ajax({
      type: "GET",
      url: '/story',
      data: $(this).serialize(),
      success: function(story) {
        $('#story').empty();
        $('#story').append('<p>' + story + '</p');
      }
    });
  });
});
