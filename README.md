
Django Signals:

Answer 1) 

By default django signals are executed synchronously. 
below is the proof for it.

![image](https://github.com/user-attachments/assets/ecb3c981-e8d1-4834-8ae8-9d0f27628d60)

here, between the Process starts and Process ends there is a 5 sec delay,until then the main thread is on hold until this very action is not completed.


Answer 2)

Yes, django signals run in the same thread as the caller.

In the below image i used the threading module and printed both the threads name, and as we can see both are same. So django signals run in the same thread as the caller.

![image](https://github.com/user-attachments/assets/e2157138-d078-4d32-b876-a7399fb42a59)


Answer 3)

Yes, By default do django signals run in the same database transaction as the caller.

below is the signals.py
![image](https://github.com/user-attachments/assets/a2bbe50d-447a-43e3-9210-1cae9ed49272)

below is the models.py

![image](https://github.com/user-attachments/assets/c9eacbf9-8ffe-4bb4-b4a4-2852064362d9)


below is the proof of it.
![image](https://github.com/user-attachments/assets/d3cbcd6c-0845-46ba-921e-531cec8b8760)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Custom Classes in Python:

![image](https://github.com/user-attachments/assets/5ff8ed2e-108d-4fd9-8df6-2cbfcf5a735d)








