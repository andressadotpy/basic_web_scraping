# Web scraping of an image

Web scraping of the logo of this Wikipedia page: https://en.wikipedia.org/wiki/Cicada_3301
- First go to the link, click on the image with the right button and choose inspect element
  - See the part of the code is about the image <img class="thumbimage"...>
- Second, request get all code.
- The class "thumbimage" is searched and selected
- cicada = image_info[0] holds all the info but only src is needed
- cicada['src'] doesn't have "http:" before "//" so we have to concatenate
- cicada_image_link is passed to a jpg file as "wb" and saved as "cicada_new.jpg".
