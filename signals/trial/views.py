from django.db import transaction
from django.contrib.auth.models import User
from trial.models import Data


try:
    with transaction.atomic():
        user = User.objects.create(username = "testuser")
        print("User created inside the transaction")

        data = Data.objects.get(user=user)
        print(f"Profile created by signal: {Data.background}")

        raise Exception("Rolling back the transaction!")
    
except Exception as e:
    print(e)   

profile_exists = Data.objects.filter(user__username="testuser").exists()
print(f"Profile exists after rollback: {profile_exists}")    
