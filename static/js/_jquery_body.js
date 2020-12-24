(function($)
{
  $(function(){
    // Plugin initialization
    $('select').not('.disabled').formSelect();
  });
})(jQuery); // end of jQuery name space


var infinite = new Waypoint.Infinite(
{
    element: $('.infinite-container')[0],
    offset: 'bottom-in-view',
    onBeforePageLoad: function(){
    $('.spinner-layer').show();
    },
    onAfterPageLoad: function(){
    $('.spinner-layer').hide();
    },
});


$('.btn-main').click(function()
{
    $('.infinite-container').hide();
});
