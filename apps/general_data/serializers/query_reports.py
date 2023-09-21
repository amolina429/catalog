from rest_framework import serializers
from ..models.query_reports import QueryReports

class QueryReportsSerializers(serializers.ModelSerializer):

      class Meta:
            model = QueryReports
            fields = '__all__'
  
      def validate(self, data):
          print("data: ",self.initial_data)
          return data