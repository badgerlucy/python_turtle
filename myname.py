from pyturtle import *
#韓国語での私の名前を表現しようとしましたが、パクイランの「パ」の部分しかまだ作られませんでした。
def draw() :    
  line_color(50,25,25)    
  fill_color(50,25,25)    
  line_width(3)    
  begin_hover()    
  forward(200)   
  turnto(90)    
  forward(200)    
  end_hover()   
  begin_fill()    
  forward(30)    
  turn(90)    
  forward(200)    
  turn(90)    
  forward(160)    
  turn(90)   
  forward(200)   
  turn(90)    
  forward(130) 
  end_fill()  
  line_color(100,100,100)
  fill_color(100,100,100)   
  begin_fill()  
  turn(90)  
  forward(100)
  turn(90)   
  forward(100) 
  turn(90)  
  forward(100) 
  turn(90)   
  forward(100)
  end_fill()   
  begin_hover()
  turnto(180)  
  forward(130) 
  end_hover()  
  begin_fill() 
  forward(40)  
  turn(90)  
  forward(100) 
  turn(90)
  forward(40)
  turn(90)   
  forward(100)  
  end_fill()  
  begin_hover()
  turnto(270)  
  forward(240) 
  turnto(180)  
  forward(50)  
  end_hover()  
  line_color(50,25,25) 
  fill_color(50,25,25)
  begin_fill()    
  turnto(0)  
  forward(200) 
  turnto(270)  
  forward(30)  
  turnto(180)  
  forward(85)  
  turnto(270)  
  forward(50)  
  turnto(180)  
  forward(30)  
  turnto(90)   
  forward(50)  
  turnto(180)  
  forward(85)  
  turnto(90)   
  forward(30)  
  end_fill()
launch(draw)