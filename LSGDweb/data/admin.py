from django.contrib import admin

# Register your models here.
from .models import Aadhar
from .models import User
from .models import Accessibility
from .models import FamilyIncome
from .models import Availability
from .models import Transportation
from .models import CurrentHealth
from .models import MedicalAccessibility
from .models import Land
from .models import CurrentlyResiding
from .models import Credits


admin.site.register(Aadhar)
admin.site.register(User)
admin.site.register(Accessibility)
admin.site.register(FamilyIncome)
admin.site.register(Availability)
admin.site.register(Transportation)
admin.site.register(CurrentHealth)
admin.site.register(MedicalAccessibility)
admin.site.register(Land)
admin.site.register(CurrentlyResiding)
admin.site.register(Credits)
