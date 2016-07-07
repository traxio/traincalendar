from rest_framework import serializers
from .models import Album, Vpe, Mozdony

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        #fields = ('id', 'vnev', 'indulas', 'indulas_ido', 'belepes', 'belepes_ido', 'erkezes', 'kilepes', 'rakomany_fajta', 'rakott', 'brutto_tonna', 'user')
        fields = '__all__'

class VpeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vpe
        fields = '__all__'

class MozdonySerializer(serializers.ModelSerializer):

    class Meta:
        model = Mozdony
        fields = '__all__'