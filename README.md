# **Smart Python Calculator**
#### Video Demo:  <https://youtu.be/jYAPgm5fQr8>
#### Description:
Hello **CS50**, it's Sebastian from Ecuador.
I really liked working with python
so I have developed a smart calculator using Tkinter for the GUI.

I started by watching a youtube tutorial on how to use Tkinter, I found it harder than other languages like Java, but at the end I managed to design a friendly interface packing all of the elements in a nice way.

For the colors I have used a Harvard theme, I also added a button wich enables light mode changing some element colors to white, and did the same with a dark mode. The basic calculator uses functions for each operation, and works as a normal calculator displaying the results and remembering the las result obtained.

From the Python lecture, I liked the posibilities that Python allows. So i decided to add an special feature to the calculator using the libraries:
speech_recognition
pyttsx3(wich is a text-to-speech conversion library)

### Listen function
There is a Listen button that call a function that listen for a math problem as a voice imput and calculates the result. The function uses:
recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
from the speech_recognition and pyttsx3 library, using the current microphone as asource, it tells the user that the program is listenting and waits for audio that later is converted to text using the google recognizer in English language. If the text is no null, it will call a function that uses the eval() function to give an answer to the math problem if valid.

### eval() function
According to realpython.com the function eval() "dynamically evaluate expressions from a string-based or compiled-code-based input. If you pass in a string to eval() , then the function parses it, compiles it to bytecode, and evaluates it as a Python expression."
I have used it with the result obtained from the listen function, wich is raw text recognized by google. Evaluated it in the eval() function and displayed the results in the interface. It uses text to speech to say the result out loud. In case of error, it will use text to speech to say an error has ocurred.

### Operators function
When a number is pressed, the program will store the value in a globlal variable so it can be operated with another one after. Once an operand is selected, the program will know if the result will be a sum, multiplication, substraction or division. When the equals button is pressed, the program uses the two numbers stored and operates by the operand selected. It will display the result and store it as a number so this answer can be operated again.

### Theme color
When the dark mode or the light mode is pressed, the program iterates through the list of buttons changing the color value.

### Running it
To execute the program, python will be needed to be installed in the computer. No extra configurations are needed.