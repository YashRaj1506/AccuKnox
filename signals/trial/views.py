from django.db import transaction
from django.contrib.auth.models import User
from trial.models import Data


try:
    with transaction.atomic():
        user = User.objects.create(username = "testuser")
        print("User created inside the transaction")

        data = Data.objects.get(user=user)
        print(f"data created by signal: {data.background}")

        raise Exception("Rolling back the transaction!")
    
except Exception as e:
    print(e)   

data_exists = Data.objects.filter(user__username="testuser").exists()
print(f"data exists after rollback: {data_exists}")    
