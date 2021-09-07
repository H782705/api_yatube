from rest_framework import serializers
from posts.models import Post, Group, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        fields = (
            "id",
            "text",
            "author",
            "image",
            "group",
            "pub_date",
            "comments",
        )
        read_only_fields = ("author",)
        model = Post
