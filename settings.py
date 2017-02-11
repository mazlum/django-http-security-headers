# ....
# References
# - https://blog.appcanary.com/2017/http-security-headers.html
# - https://docs.djangoproject.com/en/1.10/ref/settings/


# 1. X-XSS-Protection 
# Default: False
# If True, the SecurityMiddleware sets the X-XSS-Protection: 1; mode=block header 
# on all  responses that do not already have it.
SECURE_BROWSER_XSS_FILTER = True


# 2. Content Security Policy
# pip install django-csp
MIDDLEWARE_CLASSES = (
	# ...
	'csp.middleware.CSPMiddleware',
	# ...
)
CSP_DEFAULT_SRC = ("'self'", 'cdn.example.net')
# for more example; http://django-csp.readthedocs.io/en/latest/configuration.html


# 3. HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000 
#Default: False
# If True, the SecurityMiddleware adds the includeSubDomains directive to the HTTP Strict Transport Security header. 
# It has no effect unless SECURE_HSTS_SECONDS is set to a non-zero value.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# Default: 0
# If set to a non-zero integer value, the SecurityMiddleware sets the 
# HTTP Strict Transport Security header on all responses that do not already have it.


# 4. X-Frame-Options
# Default: 'SAMEORIGIN'
# The default value for the X-Frame-Options header used by XFrameOptionsMiddleware. 
# You can use this settings if you want
# X_FRAME_OPTIONS = 'DENY'


# 5. X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
# Default: False
# If True, the SecurityMiddleware sets the X-Content-Type-Options: nosniff 
# header on all responses that do not already have it.


# 6. SESSION_COOKIE_HTTPONLY
# Default: True
# Whether to use HTTPOnly flag on the session cookie. If this is set to True, 
# client-side JavaScript will not to be able to access the session cookie.
SESSION_COOKIE_SECURE = True
# Default: False
# Whether to use a secure cookie for the session cookie. If this is set to True, 
# the cookie will be marked as “secure,” which means browsers may ensure 
# that the cookie is only sent under an HTTPS connection



