import requests
import time
def get_random_joke():
    '''Fetch a random joke from the Officail Joke API.'''
    url='https://official-joke-api.appspot.com/random_joke'
    response=requests.get(url)
    if response.status_code==200:
        print(f'Full JSON Response:{response.json}')
        return response.json()
    else:
        return{'error':'failed to fetch joke'}
def main():
    while True:
        user_input=input("Press Enter to get a new joke, or type'q'/'exit to quit : ").strip().lower()
        if user_input in ("q","exit"):
            print('Goodbye!')
            break
        joke = get_random_joke()
        if "setup" in joke and "punchline" in joke:
            print(joke['setup'])
            time.sleep(10)
            print(joke["punchline"])
        else:
            print(joke.get('error',"Unexpected response format"))


main()