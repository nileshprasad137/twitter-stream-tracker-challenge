from requests_oauthlib import OAuth1Session
import webbrowser

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'


def get_access_token(consumer_key, consumer_secret):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='oob')

    print('\nRequesting temp token from Twitter...\n')

    request_token = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)

    auth_url = oauth_client.authorization_url(AUTHORIZATION_URL)

    print('Opening up browser to visit the following Twitter page '
          'if a browser will not start, copy the URL to your browser '
          'and retrieve the pincode to be used '
          'in the next step to obtaining an Authentication Token: \n'
          '\n\t{0}'.format(auth_url))

    webbrowser.open(auth_url)
    pincode = input('\nEnter your pincode? ')

    print('\nGenerating and signing request for an access token...\n')

    oauth_client = OAuth1Session(
        consumer_key, client_secret=consumer_secret,
        resource_owner_key=request_token.get('oauth_token'),
        resource_owner_secret=request_token.get('oauth_token_secret'),
        verifier=pincode
    )
    try:
        access_token = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    except ValueError as e:
        raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)

    print('''Your tokens/keys are as follows:
        consumer_key         = {ck}
        consumer_secret      = {cs}
        access_token_key     = {atk}
        access_token_secret  = {ats}'''.format(
            ck=consumer_key,
            cs=consumer_secret,
            atk=access_token.get('oauth_token'),
            ats=access_token.get('oauth_token_secret')
        )
    )
    return access_token.get('oauth_token'), access_token.get('oauth_token_secret')
