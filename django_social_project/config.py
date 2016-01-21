SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '75calirpyvhcw9'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '1jHkmwpkx84hinRp'
OCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'

SOCIAL_AUTH_LINKEDIN_SCOPE = [
    'r_basicprofile', 'r_emailaddress', 'rw_company_admin', 'w_share', 'r_fullprofile']
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = [
    'email-address',
    'public-profile-url',
    'interests',
    'skills',
    'headline',
    'industry',
    'picture-url',
    'public-profile-url'
]

SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [('id', 'id'),
                                   ('first-name', 'first_name'),
                                   ('last-name', 'last_name'),
                                   ('email-address', 'email_address'),
                                   ('headline', 'headline'),
                                   ('industry', 'industry')]


