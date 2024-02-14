# REST API for wikipedia
## Summary
This API is used for GETing quick summary of Wikipedia article.

## Usage


Invoke-WebRequest -URI http://127.0.0.1:5000/wiki/"pivo"?Accept-Language="cs" | Select-Object -Expand Content
