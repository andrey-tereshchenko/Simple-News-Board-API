from rest_framework import serializers
from django.contrib.auth.models import User

from news_board_api.models import Post, Comment


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type': 'password'},
                                             write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        if password != password_confirm:
            raise serializers.ValidationError(
                {'password': 'Password must match.'})
        user.set_password(password)
        user.save()
        return user


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('title', 'link', 'author')


class PostListSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    amount_upvote = serializers.ReadOnlyField(source='user_upvote.count')

    class Meta:
        model = Post
        fields = ('title', 'link', 'creation_date', 'author_name',
                  'amount_upvote')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'link')


class PostUpvoteSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ('user_id',)

    def update(self, instance, validated_data):
        user = User.objects.filter(id=validated_data['user_id']).first()
        if user not in instance.user_upvote.all():
            instance.user_upvote.add(user)
            instance.save()
        return instance


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('content', 'author', 'post')


class CommentListSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('content', 'author_name', 'creation_date')


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
