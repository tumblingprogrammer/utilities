var $message_div = $('#message-div');

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

