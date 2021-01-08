$("a[href='#top']").on("click", function()
{
    $('html, body').animate({ scrollTop: 0 }, 5000); //this will helps you to smooth scroll to top
    return false
});