import json
import os
import vimeo

# Load the SDK
# Instantiate the library with your client id, secret and access token
# (pulled from dev site)
client = vimeo.VimeoClient(
   token='79649392b9d3964d27e97d60fbb1fcc5',
   key='108039b6c7c021a4c845f8e19b63b6c6f99de8bd',
   secret='RHe7hofOMNr1oHFMfTDkoaOYi7XNyYwGTvFmhd0ZSrBxv4gypVwHCHgYoSl+97viJZP28Z3D7WwcsXCQPAVvBeZN5jEWCobEQQc3P5aq7WrycUL7rcmyJKvNhHtye3Q/'
)

# Upload the video
# file_name = 'D:\\Program Files\\Workspace\\templates\\res\\test3.mp4'
# uri = client.upload(file_name, data={
#   'name': 'Untitled',
#   'description': 'The description goes here.'
# })

# print('Your video URI is: %s' % (uri))      # Your video URI is: /videos/761339054

# response = client.get(uri + '?fields=transcode.status').json()
# if response['transcode']['status'] == 'complete':
#   print('Your video finished transcoding.')
# elif response['transcode']['status'] == 'in_progress':
#   print('Your video is still transcoding.')
# else:
#   print('Your video encountered an error during transcoding.')

response = client.get('/users/186926471/folders/root')


# response = client.get(uri + '?fields=link').json()
# echo "Your video link is: " . $response['link']



# response = client.get(uri)
print(response.json())
with open('./test2.json', 'w') as outfile:
    json.dump(response.json(), outfile)