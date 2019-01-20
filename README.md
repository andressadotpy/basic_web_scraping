# Web scraping of an image

Web scraping of the logo of this Wikipedia page: https://en.wikipedia.org/wiki/Cicada_3301

## Here follows some code explanation:

- First go to the link, click on the image with the right button and choose inspect element
  - See the part of the code that is about the image <img class="thumbimage"...>
- Second, request gets all html code.
- We have to search for the name of the class we saw when inspecting element
  - Thumbimage is searched and selected
- cicada = image_info[0] holds all the info but only 'src' is needed
- cicada['src'] doesn't have "http:" before "//" so we have to concatenate
- cicada_image_link is passed to a jpg file as "wb" and saved as "cicada_new.jpg".
