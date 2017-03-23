# Django Imports:
from django import forms

# Model Imports:
from rules.models import Race, Subrace, Class, Alignment, Background, PrestigeClass
from equipment.models import Weapon, Armor, Item, Tool


class SearchDatabase(forms.Form):
    """Provides an interface to search the database with."""

    query = forms.CharField(max_length=256, label='Search')

# class CharacterCreationGuided(forms.Form):
#     """Does the member want help with creating their character, or do they want to do free-for-all?"""
#
#     guided = forms.BooleanField(widget=forms.Select)


class AbilityScoresChoice(forms.Form):
    """Setting ability scores."""

    Strength = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Dexterity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Constitution = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Intelligence = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Wisdom = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))
    Charisma = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'droppable', 'readonly': 'true'}))


class CCRace(forms.Form):
    """Choose a race."""

    race = forms.ModelChoiceField(queryset=Race.objects.all())

    subrace = forms.ModelChoiceField(queryset=Subrace.objects.all())


class CCClass(forms.Form):
    """Choose a class."""

    klass = forms.ModelChoiceField(queryset=Class.objects.all())
    cleric_prestige = forms.ModelChoiceField(queryset=Class.objects.get(name='Cleric').prestige_classes.all(), required=False)
    sorcerer_prestige = forms.ModelChoiceField(queryset=Class.objects.get(name='Sorcerer').prestige_classes.all(), required=False)
    warlock_prestige = forms.ModelChoiceField(queryset=Class.objects.get(name='Warlock').prestige_classes.all(), required=False)
    hp = forms.IntegerField()


class CCPersonality(forms.Form):
    """Choose an alignment."""

    alignment = forms.ModelChoiceField(queryset=Alignment.objects.all())
    ideals = forms.CharField(widget=forms.Textarea, required=False)
    bonds = forms.CharField(widget=forms.Textarea, required=False)
    flaws = forms.CharField(widget=forms.Textarea, required=False)


class CCBackground(forms.Form):
    """Choose a background."""

    background = forms.ModelChoiceField(queryset=Background.objects.all())


class CCEquipment(forms.Form):
    """Choose equipment."""

    weapons = forms.ModelMultipleChoiceField(queryset=Weapon.objects.all(), required=False)
    armor = forms.ModelMultipleChoiceField(queryset=Armor.objects.all(), required=False)
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), required=False)
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all(), required=False)


class NCResolve(forms.Form):
    """Final form for new character creation."""

    next_page = forms.CharField(max_length=128, widget=forms.TextInput, required=False)

