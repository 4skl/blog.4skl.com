Can you explain shortly CORS and CSRF ?

GitHub Copilot
Sure.

CORS (Cross-Origin Resource Sharing): This is a mechanism that allows many resources (e.g., fonts, JavaScript, etc.) on a web page to be requested from another domain outside the domain from which the resource originated. It's a way to relax the same-origin policy, which is enforced by browsers to prevent potential attacks from malicious web pages.

CSRF (Cross-Site Request Forgery): This is an attack that tricks the victim into submitting a malicious request. It uses the identity and privileges of the victim to perform an undesired function on their behalf. For most sites, browser requests automatically include any credentials associated with the site, such as the user's session cookie, IP address, etc. Therefore, if the user is authenticated to the site, the site cannot distinguish between legitimate requests and forged requests.



Check user app and group app for nginx/app user; group in dockerfile


fail2ban et req-limit

https://docs.gunicorn.org/en/latest/deploy.html

modify django settings.py as prod

add 0auth