from rest_framework import serializers
from .models import Project,Order,Register
from django.contrib.auth import authenticate


class Projectserializers(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields= ['id','project_name','text','translated_to_language','created_at','updated_at']


class Orderserializers(serializers.ModelSerializer):
    project_id=Projectserializers()
    class Meta:
        model=Order
        fields=['id','project_id','status','translated_tex','created_at','updated_at']

class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['id','firstname','latname','email','username','date_of_birth','mobile_number','password']
        def create(self, validated_data):
            user = Register.objects.create_register(validated_data['id'],
                                                    validated_data['firstname'],
                                                    validated_data['latname'],
                                                    validated_data['email'],
                                                    validated_data['username'],
                                                    validated_data['date_of_birth'],
                                                    validated_data['mobile_number'],
                                                    validated_data['password'])
            user.set_password(validated_data['password'])
            user.save()
            return user
class Loginserializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model=Register
        fields=['email','password']
        def validate(self, data):
            email = data.get('email', None)
            password = data.get('password', None)
            if email and password:
                user = authenticate(username=email, password=password)
                if user:
                    data['user'] = user
                data['user'] = user
            return data

