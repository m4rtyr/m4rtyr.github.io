window.addEventListener('load', function() {
  var links = document.getElementsByTagName('a');
  for (var i = 0; i < links.length; i++) {
    if (!links[i].hasAttribute('class'))
      links[i].setAttribute('class', 'posta');
  }
});
