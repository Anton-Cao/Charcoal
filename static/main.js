$(document).ready(function() {
  window.speechSynthesis.cancel();
  
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
        $('#story').append('<p id="story-text">' + story + '</p>');
        $('#read-button').prop('hidden', false);
        window.speechSynthesis.cancel();
      }
    });
  });

  $('#read-button').click(function() {
    if (!window.speechSynthesis.speaking) {
      $('#icon').removeClass('fa-play').addClass('fa-pause');
      let story = $('#story-text').text();
      story = story.replace(/\*/g, ' ');
      console.log(story);
      const msg = new SpeechSynthesisUtterance(story);
      window.speechSynthesis.speak(msg);
      window.speechSynthesis.resume();
    }
    else {
      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
        $('#icon').removeClass('fa-play').addClass('fa-pause');
      } else {
        window.speechSynthesis.pause();
        $('#icon').removeClass('fa-pause').addClass('fa-play');
      }
    }
  });
});
