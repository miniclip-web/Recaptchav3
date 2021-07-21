# Recaptchav3
Recaptchav3 is used to stop the unauthorized bots without entering into your application

This is the newest API that helps you to detect abusive traffic on your website without user interaction, Instead of showing a captcha challenge recaptcha v3 returns a score so you can choose the most approriate action for your website

For reference: github.com/praekelt/django/recaptcha

Note to keep in mind: Register your keys in google recaptchav3 console before stsrting development

Recaptcha is all about front end just programatically we have to invoke the challenge and write validations as per our bussiness

Recaptcha flow will be as follows

First we need to generate the recaptcha token from frontenf and need to send it to backend for verification

In backend server before returning any information to frontend, This sends POST request to Google which returns an 16 digit number

The returned number from google needs to be processed according to views logic for example block the request if it was initiated by bot

Andd now return the response for your frontend and block the requests for bots and send HTTP 200 success code to human
