        Documentation for running the fastapi application locally


Preconditions:

  . python
	
	Python must be installed in your windows 

Clone the project:
  
   	https://github.com/8naren/AddressBook.git

Run local:
  
   Install dependencies:

	Open the command promt and run the below command
      
	      pip install -r requirements.txt
	
	To create the Virtual Environment run the below command
		
			Virualenv (name)
	
	To enter the virtual Environment Run the below command
	
		.\(name)\Scripts\Activate.Bat

	Then you will enter into Virtaul Environment

To Run the Server:

To Run the server locally run the below command
		
		uvicorn main:app --reload 

it will automatically reload when you do the changes it the code.

it will redirect into browser then you can see message displaying 

       "message":http://127.0.0.1:8000/.docs

type the above url in browser then you see fastapi docs, then you can perform what ever you want






After that select endpoint and you will find try option then you can try with your inputs.










After Giving your Inputs you will find the Responses of that api below.




