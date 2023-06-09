from django import forms
from comments_and_rating.models import CommentsAndRatings


class CommentsAndRatingsForm(forms.ModelForm):
    class Meta:
        model = CommentsAndRatings
        fields = [
            'rating',
            'comment_text',
            'car_working'
        ]
        labels = {
            'rating': 'Рейтинг',
            'comment_text': 'Коментар'
        }
        widgets = {'car_working': forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        story_id = kwargs.pop('car_story_id')
        super().__init__(*args, **kwargs)
        self.initial['car_working'] = story_id

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating not in range(1, 6):
            raise forms.ValidationError('Enter a whole number.')

        return rating
