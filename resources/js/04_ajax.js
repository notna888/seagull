function navigate(urlToGoTo){
  console.log(urlToGoTo)

  // do some history stuff

  //check that the url isn't leaving out site

  urlToVisit = "/content" + urlToGoTo
  console.log(urlToVisit)
  $.ajax({
    url: urlToVisit,
    async : true,
    type : 'GET',
    timeout : 10000,
    success: function(result, status, request){
      // console.log('SUCCESS!')
      // console.log(request)
      $('#main-section').html(result)
    },
    error : function(request, status, err){
      console.log(request)
      // window.location.href = urlToGoTo
    },
  });
  removeHrefAddOnclick()
}

function removeHrefAddOnclick(){
  $('a').each(function(){
    link = this
    // console.log(link)
    linkText = link.getAttribute("href")
    if(linkText.indexOf('#') != -1){
      // If the link is like an internal one of like used for the bootstrap navbar
      return true
    }
    if(linkText == '/' || linkText == ''){
      linkText = 'index.html'
    }
    // link.removeAttribute("href")
    link.setAttribute("onclick", "navigate('" + linkText + "')")
  })
}

function preventLinkAction(){
  $('a').click(function(e) {
    e.preventDefault();
    urlToLoad = e.target.href
    urlEnding = new URL(urlToLoad).pathname

    var stateObj = { id: urlEnding };
    history.pushState(stateObj, "CSSC", urlEnding);
  });
}

$( document ).ready( function(){
  preventLinkAction()
  removeHrefAddOnclick()
})
