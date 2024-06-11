from rest_framework import serializers
from .models import Book
from django.forms import ValidationError


'''class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    no_of_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()
    def create(self,data):
        return Book.objects.create(**data)
    def update(self,instance,data):
        instance.title = data.get('title',instance.title)
        instance.no_of_pages = data.get('no_of_pages',instance.no_of_pages)
        instance.publish_date = data.get('publish_date',instance.publish_date)
        instance.quantity = data.get('quantity',instance.quantity)
        instance.save()
        return instance'''
class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"
    def get_description(self,data):
        return "This book is called "+ data.title
    