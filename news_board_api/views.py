from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from news_board_api.models import Post, Comment
from news_board_api.serializers import UserRegistrationSerializer, \
    PostDetailSerializer, PostListSerializer, \
    PostCreateSerializer, PostUpvoteSerializer, CommentCreateSerializer, \
    CommentListSerializer, CommentDetailSerializer
from news_board_api.permissions import IsOwnerOrReadOnly


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered new user'
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)


class PostCreateView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostDetailSerializer


class PostUpvoteView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        post = Post.objects.filter(pk=pk).first()
        data = {}
        if post is None:
            return Response({'error': 'Not found this post'})
        if request.user.is_authenticated:
            data['user_id'] = request.user.id
            serializer = PostUpvoteSerializer(instance=post, data=data,
                                              partial=True)
            if serializer.is_valid():
                upvoted_post = serializer.save()
                return Response({'success': 'Post #{} upvoted by {}'.format(
                    upvoted_post.id, request.user)})
            else:
                return Response(serializer.errors)
        else:
            return Response({'error': 'User is not authenticated'})


class CommentCreateView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer


class CommentListForChosenPostView(generics.ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        post = Post.objects.filter(id=self.kwargs['pk']).first()
        return Comment.objects.filter(post=post)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
