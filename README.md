# itWorks

What is 'itWorks'?
----------------------

Remember those dark days, when your internet didn't work? when you would  
plug in your external hard drive and watch movies, maybe check your  
downloads folder for \*insert some weird package here\*, browse  
/usr/share/doc to read something that's interesting, all the while  
regularly pinging a site to know if you're internet is up or not?  

Well 'itWorks' automates that last part.  
It keeps trying to ping a website( by default www.google.com )  
until the ping is successful, and displays a dtop notification  
when it does succeed.

You can customize the notification to your liking. It works currently   
uses libnotify(notify-send) for the popup notification. So it currently  
only works for Linux. Here's how the notification looks by default: 
  

![Example Screen Shot](data/itworks.png)

System Requirements
------------------
Well, you'd need a system that supports notify-send.  
Apart from that, it should work everywhere.
