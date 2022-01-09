from django import forms

class schedule(forms.Form):
    OPTIONS = (
        (11,""),
        (21, ""),
        (31, ""),
        (41, ""),
        (51, ""),

        (12,""),
        (22, ""),
        (32, ""),
        (42, ""),
        (52, ""),

        (13,""),
        (23, ""),
        (33, ""),
        (43, ""),
        (53, ""),

        (14,""),
        (24, ""),
        (34, ""),
        (44, ""),
        (54, ""),

        (15,""),
        (25, ""),
        (35, ""),
        (45, ""),
        (55, ""),

        (16,""),
        (26, ""),
        (36, ""),
        (46, ""),
        (56, ""),

        (17,""),
        (27, ""),
        (37, ""),
        (47, ""),
        (57, ""),

        (18,""),
        (28, ""),
        (38, ""),
        (48, ""),
        (58, ""),
        
    )
    selection = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'form'}),
                                          choices=OPTIONS)
    
    def __init__(self, *args, **kwargs):
        super(schedule, self).__init__(*args, **kwargs)
        self.fields['selection'].label = ''
