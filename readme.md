# Kofran's Blog Platform
A simple blog written in Django by [Kofran](http://blog.kofran.com)

## Disclaimer
This project is in a very early development state. **I really not recomend for production use**.

### Version 0.2

### What features the blog has?
At the moment the blog has a very little features like:
- home page now also include pagination.
- right panel.
- writter page. (administrator user).
- edition page. (administrator user).
- users can register (reCAPTCHA was implemented to avoid bots).
- users can make comments in posts.

### Requeriments
- Django version >= 1.11 .
- Python-decouple 3.1 .

### Important
Raname **.env.example** to **.env**.
Then configure your own SECRET_KEY  **please don't use the same key as the example**.
You need to configure RECAPTHA_SECRET with your own key provided by [reCAPTCHA](https://www.google.com/recaptcha/).

If you are testing your app at localhost or 127.0.0.1, you need to configure your reCAPTCHA's domains to allow them.
