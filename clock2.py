from pyturtle import *
def draw():    speed('fastest')
    hour=rand(24)    minute = rand(60)
  #  say("{0}時{1}分です".format(hour,minute))
    line_color(100,75,20)    
    line_width(3)
    fill_color(100,75,20)  
    begin_hover()  
    turnto(90)   
    forward(200)   
    turnto(0)   
    end_hover()   
    begin_fill()   
    circle(200,'right')   
    end_fill()
    
    
    line_color(100,25,50) 
    line_width(1)   
    fill_color(100,25,50) 
    begin_hover()  
    turnto(270)   
    forward(186)  
    turnto(0)    
    mark()    
    forward(180)  
    end_hover()  
    for i in range(13):       
      turnto(270)       
      begin_fill()      
      for j in range(3):   
      forward(20)          
      turn(240)       
      end_fill()      
      begin_fill()    
      for j in range(2): 
      turnto(0)          
      arc(5,-180)       
      end_fill()     
      begin_hover()   
      back()       
      mark()       
      turn(-30 * i)
      forward(180) 
      end_hover()
      
      
    line_color(75,0,25) 
    fill_color(75,0,25) 
    line_width(15)   
    begin_hover()  
    turnto(180)    
    forward(182)   
    end_hover()    
    turnto(0)    
    mark()   
    hour1 = hour * 30 + (minute / 60) * 30  
    turn(-hour1)  
    forward(150)
    
    
    line_color(100,100,75)  
    fill_color(100,100,75) 
    line_width(10)   
    begin_hover() 
    back()   
    end_hover() 
    turnto(0)   
    mark()   
    minute1 = minute * 6  
    turn(-minute1)   
    forward(180)
    
launch(draw)
