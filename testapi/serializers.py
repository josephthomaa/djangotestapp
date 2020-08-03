from rest_framework import serializers
from testapi.models import UserRatings, User, Movie


class UserRatingsSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.userId.name

    class Meta:
        model = UserRatings
        fields = ["userId", "user_name", "rating"]


class MovieRatingsSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField(read_only=True)

    def get_ratings(self, obj):
        user_ratings = UserRatings.objects.filter(movieId=obj.id)
        print(user_ratings)
        return UserRatingsSerializer(user_ratings, many=True, context=self.context).data

    class Meta:
        model = Movie
        fields = ["id", "title", "ratings"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id", "title", "genres"]
