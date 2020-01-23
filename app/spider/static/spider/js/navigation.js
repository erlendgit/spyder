(function ($, document, window) {
    "use strict";
    var jqDocument = $(document);
    var scrollPos = {x: null, y: null};

    function copyScrollPos() {
        scrollPos.x = jqDocument.scrollLeft();
        scrollPos.y = jqDocument.scrollTop();
    }

    copyScrollPos();
    $(window).scroll(copyScrollPos);

    (function init_feeditems_pager() {
        $('.feeditems').each(function () {
            var feeditems = $(this);
            $('.reload', feeditems).not('processed').each(function () {
                var reloadButton = $(this);
                var scrollTo;
                reloadButton.addClass('processed');
                reloadButton.click(function () {
                    $.ajax({
                        method: 'GET',
                        url: reloadButton.data('target'),
                        data: {
                            category: reloadButton.data('category'),
                            count: reloadButton.data('count'),
                            next_page: reloadButton.data('next-page'),
                        },
                        beforeSend: function () {
                            scrollTo = {
                                x: scrollPos.x,
                                y: scrollPos.y,
                            };
                        },
                        success: function (content, status, jqXHR) {
                            feeditems.replaceWith(content);
                            window.scrollTo(scrollTo.x, scrollTo.y);
                            init_feeditems_pager();
                        }
                    });
                });
            });
        });
    })();
})(jQuery, document, window);
