# Word Filter in Python/Django

## Technology 
* Python 
* Django 
* NLTK (Natural Language Processing ToolKit in Python)

## Implementation
The project renders 2 web pages. 
The welcome page that allows the upload of a file containing strings. Upon submission, the file is saved and the processing function is called with another thread (Multi threading implementation using the threading module in Python)

The user is then redirected to the output page where the result of the processing is displayed. 
If the processing is not complete at the time the user gets to the result page, the page displays a message to tell the user to refresh in a couple of seconds to see the result. The result is a also saved on the database item that has the file into a field. 

### The processing flow is as follows: 
    * The file is retrieved from the database and read to get only the content of strings. 
    * A process called tokenization is performed on the string from the file uploaded by the user. This process separates sentences into individual string of words instead of entire sentences. The output of this is a list of words and punctuation if available.
    * Unique strings from the content is produced by pasing it through the set() builtin function in Python 
    * Then a set of all stopwords from the NLTK library in Python is generated from the corpus module. 
    * The final step is to generate a new list of words that are not in the stopwords. That is, removing the stopwords from our list of strings output. 
    * The result is saved in the database as an update to the database instance that contains the file uploaded in the first place

A unique file ID is used to identify every uploaded file and this helps to routing as well. 



