

NOTE: there are certain 'bad' programming practices used to keep the code using simpler tools. For example I don't use things like lambda functions and 
List Comprehension in the code because we don't cover them in class. I also generally find List Comprehension generally difficult to read. The exception to this
is ballDetection.py which uses opencv2. I was not about to sit here and program up a gausian blur by hand.

Also not we are doing image recognition with just a simple opencv color map. Although we talked about using a CNN in class it's a bit slow to use for 30FPS.
The way I used was to use a FAST-CNN object detection architecture and used transfer learning. I also used tensorflow2 which might be slower than pytorch
in this situation.
I think a better way would be to use a two phase CNN and program a custom object detector. You could just use a opencv2 map of all orange like colors.
Then run the image detection on each object. This would mean your CNN could probably be alot smaller hence faster. 


STUCTURE OF THE CODE

Students write the code in main
Controller.py is the file that interfaces with the library. It also includes some functions that may be useful for students

Note when running keyboard controller through ssh terminal need to set export defualt to 0
Run this command: export DISPLAY=:0
This is due to how linuxs handles different users and security. Which took me way too longer than it should of to realise

Tests files includes relevent tests to see if robots working
testmotors.py tests turns all motors forwards and backwards



IMPROVEMENTS:
This whole thing really should be multithreaded. The whols program is I/O bound on camera so it's bottlenecked by that.
Currently everything is singlethreaded and executed linearly. 
Not sure how to make it work better in python though with the GIL(global interpreter lock). Probably could be done but would take significant architecutre
redesigns.
Maybe the async library for python could do it?
Could rewrite in C++ but its quite unneccassry seeing that the program is I/O bound not CPU bound.

-Also need to implement better way of sleeping than using time.sleep()
-This pasues all activity in the program
Should use some kind of dispatched thread that interupts in n seconds or something
Maybe theres some way of doing asynchronou functionality in python more easily that I'm not aware of

We are also not currently using the IMU's position data
I couldn't find a library online to do it so I'd have to program in myself.
The accelerations are given relative to the rotation. We want absolute acceleration
So you'd have to make a rotation matrixs to apply the transformation to the given acceleration values to convert it to an absolute position


