require([
  'jquery',
], function($){
  'use strict';

    function setup_rer_pubblicazioni_search_form(){
        $(document).on('click', '.search-pubblicazioni input[type=submit]', function (e) {
            e.preventDefault();
            var $form = $(e.target).parents('form');
            var searchable = $form.find('[name=SearchableText]').val();
            var author = $form.find('[name=authors\\:list]').val();
            var ptype = $form.find('[name=publication_types\\:list]').val();
            var plang = $form.find('[name=publication_language\\:list]').val();
            var pstart = $form.find('[name=start]').val();
            var pend = $form.find('[name=end]').val();
            var path = $form.find('[name=path]').val()

            var querystring = '?portal_type=Pubblicazione'
            if (searchable){
                querystring = querystring + '&SearchableText=' + encodeURI(searchable);
            }
            if (author !== '--NOVALUE--'){
                querystring = querystring + '&authors=' + encodeURI(author);
            }
            if (ptype !== '--NOVALUE--'){
                querystring = querystring + '&publication_types=' + escape(ptype);
            }
            if (plang !== '--NOVALUE--'){
                querystring = querystring + '&publication_language=' + escape(plang);
            }
            if (pstart && !pend){
                querystring = querystring + '&publication_date.query:record:list:date=' + pstart + '&publication_date.range:record=min';
            }
            if (pend && !pstart){
                querystring = querystring + '&publication_date.query:record:list:date=' + pend + '&publication_date.range:record=max';
            }
            if (path.length !== 0){
                querystring = querystring + '&path=' + path;
            }
            $form.find('.error-message').remove();
            if (pstart && pend){
                var start = new Date(pstart.split('-'));
                var end = new Date(pend.split('-'));
                if (end < start){
                    var errormessage = $('.dates').data('error-message');
                    var $pmessage = $('<p class="error-message" style="color:red">' + errormessage + '</p>');
                    $form.find('.dates').after($pmessage);
                    return
                }
                querystring = querystring + '&publication_date.query:record:list:date=' + pstart + '&publication_date.query:record:list:date=' + pend + '&publication_date.range:record=min:max';
            }
            var to_url = $('link[rel=search]').attr('href') + querystring;
            console.log(to_url);
            window.location.href = to_url;
        });
    };

    // $(document).on('rtTilesLoaded', '.pat-tiles-management .tilesList .search-pubblicazioni', function(e) {
    //     debugger;
    //     $('#form-widgets-publicationAuthor').select2();
    //     $('#form-widgets-publicationTypes').select2();
    //     $('#form-widgets-publicationLanguage').select2();
    // });
    $(document).ready(function(){
        setup_rer_pubblicazioni_search_form();
    });
});

define("/Users/arsenico13/work/redturtle/rer/rerp5/rerplone/src/rer.pubblicazioni/src/rer/pubblicazioni/browser/static/rerpubblicazioni.js", function(){});

