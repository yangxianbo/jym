from django.contrib import admin
from authsys.models import *

# Register your models here.
admin.site.register(authorization)
admin.site.register(perauthorization)
admin.site.register(accesslog)
admin.site.register(machine_info)
admin.site.register(permachine_info)
admin.site.register(group_info)
admin.site.register(upload_file)
admin.site.register(package)
admin.site.register(package_relateapp)
