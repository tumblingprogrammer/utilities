new Clipboard('.btn'); // instantiation of clipboard.js

var $text_to_slugify = $('#text-to-slugify');
var $slugified_text = $('#slugified-text');
var $prefix_to_slugified_text = $('#prefix-to-slugified-text');
var $suffix_to_slugified_text = $('#suffix-to-slugified-text');
var $markdown_link_prefix_to_the_link_constructor = $('.markdown-link-prefix-to-the-link-constructor');
var $prefix_to_the_link_constructor = $('#prefix-to-the-link-constructor');
var $markdown_link_text_to_slugify = $('.markdown-link-text-to-slugify');
var $location_of_the_file = $('#location-of-the-file');
var $markdown_link_location_of_the_file = $('#markdown-link-location-of-the-file');
var $markdown_link_slugified_file_name = $('#markdown-link-slugified-file-name');
var $markdown_link = $('#markdown-link');


var text_to_slugify = $text_to_slugify.val();

function construct_strings() {
    $markdown_link.removeClass('dimmed-text');
    var slugified_text = $prefix_to_slugified_text.val() + slugify($text_to_slugify.val()) +
        $suffix_to_slugified_text.val();
    if (slugified_text === '') {
        $slugified_text.text('the slugified text will show here');
    }
    else {
        $slugified_text.removeClass('dimmed-text');
        $slugified_text.text(slugified_text);
    }


    $markdown_link_prefix_to_the_link_constructor.text($prefix_to_the_link_constructor.val());
    $markdown_link_text_to_slugify.text($text_to_slugify.val());

    $markdown_link_location_of_the_file.text($location_of_the_file.val());
    $markdown_link_slugified_file_name.text($slugified_text.text());
}

function clear_slugify_fields() {
    $prefix_to_slugified_text.val("");
    $suffix_to_slugified_text.val("");
    $text_to_slugify.val("");
    $slugified_text.addClass('dimmed-text');
    $slugified_text.text('the slugified text will show here');
}

function clear_markdown_image_link_constructor_fields() {
    $prefix_to_the_link_constructor.val("");
    $location_of_the_file.val("");
    $markdown_link.addClass('dimmed-text');
}

$(document).on('click', '#clear-slugifier-fields', function () {
    clear_slugify_fields();
});

$(document).on('click', '#clear-markdown-link-fields', function () {
    clear_markdown_image_link_constructor_fields();
});

$(document).on('click', '#clear-all-fields', function () {
    clear_slugify_fields();
    clear_markdown_image_link_constructor_fields();
});

$(document).on('input', $text_to_slugify, function () {
    construct_strings();
});

$(document).on('input', '#prefix-to-slugified-text', function () {
    construct_strings();
});

$(document).on('input', '#suffix-to-slugified-text', function () {
    construct_strings();
});

$(document).on('input', '#prefix-to-the-link-constructor', function () {
    construct_strings();
});

$(document).on('input', '#location-of-the-file', function () {
    construct_strings();
});