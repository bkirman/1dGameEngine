from lib.hsv_to_rgb import hsv_to_rgb

class Display1d:
    '''Abstract class for different rendering engines to implement, based on specific technical requirements. 
    The assumption is that it is implements pixel by pixel operations. 
    The main draw function will then be responsible for clearing the screen etc depending on requirements'''
    def setRgb(self,i,rgb):
        return

    def setHsv(self,i,hsv:tuple):
        ''' hsv is a tuple (h,s,v)'''
        self.setRgb(i,hsv_to_rgb(hsv[0],hsv[1],hsv[2]))
    
    def refresh(self):
        return