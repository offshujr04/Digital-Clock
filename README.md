<h1>Digital Clock</h1>



This project creates a simple digital clock that continuously updates the displayed time, date, and day of the week using the Tkinter GUI framework and the time module.

<!-- <div align="center">

![GitHub Repo stars](https://img.shields.io/github/stars/jaydeepdey03/youtube-clone?style=social)
![GitHub Repo forks](https://img.shields.io/github/forks/jaydeepdey03/youtube-clone?style=social)
![GitHub Repo Contributors](https://img.shields.io/github/contributors/jaydeepdey03/youtube-clone?style=social)

</div> -->
<br>

![image](https://github.com/offshujr04/Digital-Clock/assets/114171354/ce68dbf7-a297-4b76-b000-d9bae6d0471a)  
<br>


### **Libraries Used :**
<hr>
<p>Tkinter-----> needs to be installed in your idle
  <br>
Time-----> is already present in your idle[vscode it was preinstalled]
</p>
<h3>Working :</h3>
<hr>
<br>
Importing required modules: The program starts by importing the “Tk” class from the tkinter module and the strftime function from the time module.<br>
Create a Tkinter window: The Tk() function is called to create the main window of the application, which is assigned to the root variable. The title() method sets the title of the window to "Digital Clock". <br>
Define the clock update function: The fun() function is defined to update the time, date, and day labels of the clock. It is designed to be called repeatedly using the root.after() method based on recursion. <br>
Update the time label: The strftime() function is used to format the current time as a string in the format HH:MM:SS AM/PM ['%H:%M:%S %p']. The resulting string is assigned to the timestring variable. The config() method of the time\_label widget is then called to update its text to the timestring. <br>
Update the date label: The strftime() function is used to format the current date as a string in the format Month DD, YYYY ['%B %d, %Y']. The resulting string is assigned to the date\_string variable. The config() method of the date\_label widget is then called to update its text to the date\_string. <br>
Update the day label: The strftime() function is used to format the current day of the week as a string. The resulting string is assigned to the day\_string variable. The config() method of the day\_label widget is then called to update its text to the day\_string. <br>
Create and pack the labels: Three Label widgets are created to display the time, date, and day. The font option sets the font style and size, and the fg and bg options set the foreground (text) and background colors of the labels. The pack() method is called on each label to add them to the window and automatically arrange them. <br>
Call the update function and start the main loop: The fun() function is initially called to start updating the clock. Then, the mainloop() method is called on the root window to start the event loop, which handles user interactions and updates the GUI. Recursive update of the clock: The root.after() method is used to schedule the next call to the fun() function after 1000 milliseconds (1 second). This creates a recursive loop that continuously updates the clock every second. 









