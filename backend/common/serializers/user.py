from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="article-detail",
    )
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="comment-detail",
    )

    portfolio = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="portfolio-detail",
    )
    # usstock = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="usstock-detail",
    # )
    # kostock = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="kostock-detail",
    # )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "portfolio",
            "articles",
            "comments",
            # "usstock",
            # "kostock",
        ]
        ordering = ["id"]
