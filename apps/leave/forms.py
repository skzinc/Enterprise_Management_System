from django import forms
from .models import Leave, MyUser
from django.db.models import Q


class CreateleaveForm(forms.ModelForm):
    pl = forms.IntegerField(label='PL')
    cl = forms.IntegerField(label='CL')
    half_day = forms.IntegerField(label="HALF_DAY")
    comp_off = forms.IntegerField(label='COMP_OFF')

    class Meta:
        model = Leave
        fields = ('pl', 'cl', 'half_day', 'comp_off')

    def save(self, commit=True):
        employee = MyUser.objects.filter(~Q(designation="Client"))
        instance = super(CreateleaveForm, self).save(commit=False)
        saved_instance = []
        if commit:
            pl = self.cleaned_data.get('pl')
            cl = self.cleaned_data.get('cl')
            half_day = self.cleaned_data.get('half_day')
            comp_off = self.cleaned_data.get('comp_off')
            for emp in employee:
                if instance.id:
                    instance.id = None
                instance.user_id = emp.id
                instance.pl = pl
                instance.cl = cl
                instance.half_day = half_day
                instance.comp_off = comp_off
                instance.save()
                saved_instance.append(self.instance)
        return saved_instance





