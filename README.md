# Intro

An automated pipeline that aggregates news articles from limited-access sources and archives them to Scribd. This project ensures permanent access to information by bypassing temporary download restrictions.

## Problem

Main problem is that the news is not freely accessible as there are paywalls on news channels.

The problem with news article published online for free at my given source is that if many people downloads the file g drive reaches maximum download limit and cannot download the files so at first i download them and upload to a public pdf provider where any user can access any pdf virtually any number of times.

But what happens when already the limit reached.

Then we can't do anything 
and the uploaded files on scribd will show errors

## Running

### Running your own this via github actions
Fork this repo and in repo secrets 

Add 
- SCRIBD_SESSION
- CAPTCHA_KEY

SCRIBD_SESSION is the value of cookie _scribd_session
CAPTCHA_KEY is the value of api key obtained from [2Captcha](https://2captcha.com/enterpage)

### Running on your local machine

1) Clone the repo
```
git clone https://github.com/lsnnt/news-upload 
```
2) Go to the repo location
```
cd news-upload
```
2) Install the dependencies
```
pip3 install -r requirements.txt
```
3) Export the secrets 
```
export SCRIBD_SESSION="Your long scribd session id here"
export CAPTCHA_KEY="your 2captcha key here"  
```
4) Run the main function
```
python3 main.py
```

Now you know how to run in your local machine now you can run it anywhere. !!! 🥳

### Running via docker

The easiest just install docker
```
docker run \
  -e SCRIBD_SESSION="Your long scribd session id here" \
  -e CAPTCHA_KEY="your 2captcha key here" \
  ghcr.io/lsnnt/news-upload:latest
```

## Support

Contact me on Session at 05501ebf09a0fe363d76046f0f2c027f3ce031bd649dbb94113622e6cb25563334

On email at tnityanand523@gmail.com
use pgp encryption 74B98BF367A3084CC8202FAF8DFEF50F58A432A6

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEaFvucBYJKwYBBAHaRw8BAQdAV1Was61jXtFiI12folbbWsQYKiWyfzMZwf8j
zC3fJxi0Kk5pdHlhbmFuZCBUaGFrdXIgPHRuaXR5YW5hbmQ1MjNAZ21haWwuY29t
PoiZBBMWCgBBFiEEdLmL82ejCEzIIC+vjf71D1ikMqYFAmhb7nACGwMFCQWjmoAF
CwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQjf71D1ikMqZfXAEAgETg8YN6
ABWqtQvevIWV4mcU8Whep/7sqq0SBQZWg/UA/0TNSUS/cHQB29JqElX4UgkRwH+C
gmXxKEN1uLdsdHAPuDgEaFvucBIKKwYBBAGXVQEFAQEHQEGOsxY0fyh9x9qB0OgL
QhlSv+ZSNXmo31713iL6ZWY+AwEIB4h+BBgWCgAmFiEEdLmL82ejCEzIIC+vjf71
D1ikMqYFAmhb7nACGwwFCQWjmoAACgkQjf71D1ikMqbgVwEAoDilntsraWSxGklf
BPpUhkYxbziUD9jXLyZoI+qUyRgA/i8MHCYkYBm8qYJXawR4GLxcM/OSEzfLgiCN
Jg9mg78E
=CX9H
-----END PGP PUBLIC KEY BLOCK-----
```

## Sources

We source our news from [here](https://epaperwave.com/) 
You can find all news paper for free.

My Scribd url :- [my scribd profile](https://www.scribd.com/user/688308679/Nityanand-Thakur)

## Issue

Any issue open an issue

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU GPL](https://choosealicense.com/licenses/gpl-3.0/)
