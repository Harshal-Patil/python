import math
def paint_calc(height,width,cover):
  area=height*width
  num_of_cans=math.ceil(area/cover)
  print(f"Number cans you need {num_of_cans} to paint.")

test_h=int(input("Enter the height Wall="))
test_w=int(input("Enter the width Wall="))
coverage=int(input("Enter how many area to cover="))
paint_calc(height=test_h,width=test_w,cover=coverage)