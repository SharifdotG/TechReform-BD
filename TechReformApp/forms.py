from django.forms import ModelForm
from .models import CPU, Cooler, Motherboard, HDD, GPU, Casing, Keyboard, Headphone


class CPUForm(ModelForm):
    class Meta:
        model = CPU
        fields = "__all__"


class CoolerForm(ModelForm):
    class Meta:
        model = Cooler
        fields = "__all__"


class CasingForm(ModelForm):
    class Meta:
        model = Casing
        fields = "__all__"


class MotherboardForm(ModelForm):
    class Meta:
        model = Motherboard
        fields = "__all__"


class HDDForm(ModelForm):
    class Meta:
        model = HDD
        fields = "__all__"


class GPUForm(ModelForm):
    class Meta:
        model = GPU
        fields = "__all__"


class KeyboardForm(ModelForm):
    class Meta:
        model = Keyboard
        fields = "__all__"


class HeadphoneForm(ModelForm):
    class Meta:
        model = Headphone
        fields = "__all__"
