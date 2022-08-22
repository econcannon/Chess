# Chess
This program is a simple chess game using the pygame library. The game functions as normal with the exception of promotion and castling which has not yet been included.
The program is designed with an MVC style architecture. The piece classes and board class are contained within the Model module, the game controller class combines
the logic of the Model with the game view for displaying the output. 

Unfortunately text to speech was not a viable method of controlling the pieces because the voice recognition software avaliable could not reliably understand voice input of short things such as numbers and letters. As such it was cut from the final product.
