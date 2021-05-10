# cloudwiry_backend_task
simple chat application with python backend

The chat application will have the following features:
 User authentication and session management
 One to One chat - the message sent would include only text.
 An interface (cli / web based) to send, receive and view messages.
 End-to-End encryption for chats

Application flow
User logs in to the application using username and password (Authentication to happen over HTTP using REST API)
Selects a username to send messages to
A connection is established between server and client for message transmission. Eg: Socket connection.
If the receiver is offline then the messages should be stored in the database and be delivered once the user is back online.
The message stored must be encrypted. You can use any standard encryption method.
