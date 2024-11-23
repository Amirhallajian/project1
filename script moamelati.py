
def slope(x1,y1,x2,y2):
    """تابع شیب خط"""
    if x2 - x1 == 0:
        return "bdone shib"
    m_slope = (y2 - y1) / (x2 - x1) # فرمول شیب 


    def width(slope,x,y):
        """تابع عرض در مبدا"""
        b_width = y - slope *x  #فرمول عرض در مبدا

        if m_slope == m_slope :
            print (f'shibe= {m_slope:.2}\narzedar mbda= {b_width:.2}')


            def line(m,b,x):
                """معادله خط"""
                return f'Y={m}*{x} + {b} = {m*x + b}' # فرمول 
            print(line(m_slope,b_width,x1))

            
        else:
            None

    (width(m_slope,x1,y1))



x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
slope(x1,y1,x2,y2)
