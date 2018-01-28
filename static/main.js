$(document).ready(function() {
  console.log("javascript loaded");

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
      type: "POST",
      url: '/',
      data: JSON.stringify(data, null, '\t'),
      contentType: "application/json; charset=utf-8", // this
      dataType: "json", // and this
      success: success
    });
  });
});
