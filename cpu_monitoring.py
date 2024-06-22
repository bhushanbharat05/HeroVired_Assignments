import psutil

i=1
def monitoring():
    print("Monitoring CPU!!")
    threshold= float(input("Enter your CPU threshold value in % : "))
    while i==1:
        # assuming CPU threshold set as 85%  and will print in an interval of 1 sec
        if psutil.cpu_percent(interval=1) > threshold :  
            print(f'Alert! CPU usage exceeds threshold: {psutil.cpu_percent(1)} %')
    
monitoring()

