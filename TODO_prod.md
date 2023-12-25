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

add https
`docker exec -it 4sklcom-prod-1 sh`
`docker exec -it 4sklcom-prod-1 certbot --nginx -n -d www.4skl.com --agree-tos --email medi.olivier@hotmail.com --no-eff-email --staging`

for debug :
https://stackoverflow.com/questions/44785585/how-can-i-delete-all-local-docker-images

Unix

To delete all containers including its volumes use,

`docker rm -vf $(docker ps -aq)`
To delete all the images,

`docker rmi -f $(docker images -aq)`