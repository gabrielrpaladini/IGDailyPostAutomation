from images import Photos
from user import UserClass
from upload import PostGenerator
from locators import Locators
from phrase import Quote

if __name__ == "__main__":

    file_name = 'nome'

    image = Photos(file_name)

    print('*** Gen photo')

    image.download_photo()

    print('*** Gen quote')

    quote = Quote().get_quote()

    print(f'*** Quote: {quote}')

    print('*** Gen post')

    post = PostGenerator(Locators.CHROME_EXECUTABLE_PATH)

    post.upload_photo(file_name, quote)

    print('*** Done')