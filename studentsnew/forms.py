from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data['age']

        if age <= 18:
            raise forms.ValidationError(
                "Age must be greater than 18"
            )

        return age