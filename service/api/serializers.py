from rest_framework import serializers
from api.models import MicroServico
from unidecode import unidecode
import pytz

class MicroServicoSerializer(serializers.ModelSerializer):
    data_criacao = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S %Z", default_timezone=pytz.timezone('America/Sao_Paulo'))
    
    class Meta:
        model = MicroServico
        fields = [
            'codigo',
            'produto',
            'valor',
            'data_criacao'
        ]
        
    def validate(self, data):
        codigo = data.get('codigo')
        produto = data.get('produto')
        codigo = unidecode(codigo).lower()
        if MicroServico.objects.filter(produto__iexact=produto).exists():
            raise serializers.ValidationError("Já existe um produto cadastrado com esse nome.")
        if MicroServico.objects.filter(codigo__iexact=codigo).exists():
            raise serializers.ValidationError("Já existe um produto cadastrado com esse codigo.")
        return data
