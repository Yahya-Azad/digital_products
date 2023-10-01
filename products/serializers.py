from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('id', 'title', 'file', 'file_type')

    def get_file_type(self, obj):
        return obj.get_file_type_display()
        #  واسه اینکه مدل فایل تایپ به عدد نباشه و اسمش بیاد که ویدئو عه یا پی دی افه یا ویس


# واسه اینکه هر پروداکت زیرش یه url باشه برای دیدن دیتیل اون پست و GET کردنش از هایپرلینک استفاده میکنیم و تو fields
# اضافه میکنیم url رو و تو پوشه urls.py فیلد name اضافه میکنیم
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)  # واسه اینکه کتگوری ها کامل بیان اسمشونو اینا و فقط آیدی کتگوری نیاد
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'categories', 'files', 'url')
