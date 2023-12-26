from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.management import call_command
from django.http import HttpResponse
from django.views import View
import io, os
import tempfile
from django.core.files.storage import FileSystemStorage


class DumpDataView(UserPassesTestMixin, View):
    def test_func(self):
        # Only allow admin users
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        # Create a StringIO object
        output = io.StringIO()

        # Call the 'dumpdata' command and save the output in the StringIO object, excuding the contenttypes, auth.Permission and sessions.session tables as being useless there and a potential security issue
        # The User model is included in the dumpdata output because it is needed to not have to create a new superuser after loading the data
        # This is still safe cause the password is in a salted and slow hashed form (also the password choosen for the superuser is strong and not used anywhere else)
        call_command(
            'dumpdata', 
            stdout=output, 
            natural_foreign=True, 
            natural_primary=True, 
            exclude=['contenttypes', 'auth.Permission', 'sessions.session'], 
            indent=4
        )

        # Create a HttpResponse to send the data back as a file download
        response = HttpResponse(output.getvalue(), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=dumpdata.json'

        return response
    
class LoadDataView(UserPassesTestMixin, View):
    def test_func(self):
        # Only allow admin users
        return self.request.user.is_superuser

    def post(self, request, *args, **kwargs):
        # Get the file from the request
        data_file = request.FILES['data']

        # Save the file to a temporary location
        fs = FileSystemStorage(location=tempfile.gettempdir())
        filename = fs.save(data_file.name, data_file)
        filepath = fs.path(filename)

        # Call the 'loaddata' command with the path of the uploaded file
        call_command('loaddata', filepath)

        # Delete the temporary file
        fs.delete(filepath)

        return HttpResponse('Data loaded successfully')