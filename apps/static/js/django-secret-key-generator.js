var clipboard = new Clipboard('.btn'); // instantiation of clipboard.js

var $message_div = $('#message-div');

$('#refresh-btn').on('click', function () {
    location.reload();
});

clipboard.on('success', function (e) {
    $message_div.removeClass('in');
    e.clearSelection();
    $('#success').text("copied to clipboard!");
    $message_div.fadeIn('fast').delay(600).fadeOut('fast');
});

clipboard.on('error', function (e) {
    console.error('Action:', e.action);
    console.error('Trigger:', e.trigger);
});